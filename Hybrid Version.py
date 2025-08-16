#working full but without neo4j login. instead uses sqlalchemy.
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import os
import aiml
import nltk
from textblob import TextBlob
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, ne_chunk
import re
from neo4j import GraphDatabase, exceptions

# Initialize nltk for sentence parsing
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

app = Flask(__name__)
app.secret_key = os.urandom(24)

# --- START: NEO4J INTEGRATION SETUP ---

# Neo4j connection details
# --- Neo4j Connection ---
from config import NEO4J_PASSWORD # <-- IMPORT YOUR SECRET
# The password is now loaded securely from the other file
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"


# Initialize Neo4j driver
driver = None
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    driver.verify_connectivity()
    print("✅ Neo4j connection successful.")
except exceptions.AuthError:
    print("❌ NEO4J AUTH ERROR: Please check your username and password in the script.")
except exceptions.ServiceUnavailable:
    print("❌ NEO4J CONNECTION ERROR: Could not connect to the database. Is it running?")
except Exception as e:
    print(f"❌ An unexpected error occurred with Neo4j: {e}")

# UPDATED: Using execute_write to avoid deprecation warnings
def _create_emergency_number_tx(tx, situation, number):
    query = (
        "MERGE (s:Situation {name: $situation}) "
        "MERGE (n:EmergencyNumber {number: $number}) "
        "MERGE (s)-[:HAS_NUMBER]->(n)"
    )
    tx.run(query, situation=situation, number=number)
    print(f"✅ Neo4j transaction successful for number: '{number}' for situation: '{situation}'")

def _create_emergency_advice_tx(tx, situation, advice):
    query = (
        "MERGE (s:Situation {name: $situation}) "
        "MERGE (a:Advice {text: $advice}) "
        "MERGE (s)-[:HAS_ADVICE]->(a)"
    )
    tx.run(query, situation=situation, advice=advice)
    print(f"✅ Neo4j transaction successful for advice for situation: '{situation}'")

# --- END: NEO4J INTEGRATION SETUP ---


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# User model (Unchanged)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    def __init__(self, email, password, name):
        self.name, self.email = name, email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

# AIML Setup (Unchanged)
def load_aiml_files(kernel, directory):
    if os.path.exists(directory):
        files = [f for f in os.listdir(directory) if f.endswith(".aiml")]
        for filename in files: kernel.learn(os.path.join(directory, filename))
bot_primary = aiml.Kernel()
primary_aiml_directory = os.getenv("PRIMARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\Aimldata")
load_aiml_files(bot_primary, primary_aiml_directory)


# Prolog Reader (Unchanged)
def get_info_from_prolog_file(situation, info_type="number"):
    prolog_file_path = os.getenv("PROLOG_FILE_PATH",
                               r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PrologFiles\EmergencyContacts.pl")
    fact_name, response_template = "", ""
    if info_type == "number":
        fact_name, response_template = "get_emergency_number", "The emergency number for {0} is {1}."
    elif info_type == "advice":
        fact_name, response_template = "get_emergency_advice", "For {0}, here is some advice: {1}."
    else:
        return "Internal error: Invalid info_type.", None
    try:
        with open(prolog_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('%') or not line.strip(): continue
                match = re.search(rf"{fact_name}\('{situation}',\s*'?(.*?)'?\)\.", line)
                if match:
                    value = match.group(1).strip()
                    print(f"💡 Found in Prolog file: '{value}' for situation '{situation}'")
                    return response_template.format(situation, value), value
        print(f"⚠️ Could not find info for '{situation}' in Prolog file.")
        return f"Sorry, I couldn't find any information for '{situation}'.", None
    except FileNotFoundError:
        print(f"❌ ERROR: Prolog file not found at path: {prolog_file_path}")
        return "ERROR: The chatbot's knowledge base file is missing.", None
    except Exception as e:
        print(f"❌ An error occurred while reading the Prolog file: {e}")
        return "An error occurred while reading the knowledge base.", None

# NLP Functions (Unchanged)
def get_definition(word):
    try: return wn.synset(word + '.n.01').definition()
    except Exception: return f"Definition not found for '{word}'."
def get_sentence_type(sentence):
    if sentence.endswith("!"): return "an exclamation"
    if sentence.endswith("?"): return "a question"
    return "a statement"
def get_sentiment(sentence):
    polarity = TextBlob(sentence).sentiment.polarity
    if polarity > 0.1: return "positive"
    if polarity < -0.1: return "negative"
    return "neutral"
def get_named_entities_and_pos(sentence):
    sentence, pos_tags_list, named_entities = sentence.title(), [], []
    for sent in sent_tokenize(sentence):
        words, pos_tags = word_tokenize(sent), pos_tag(word_tokenize(sent))
        pos_tags_list.append(pos_tags)
        for chunk in ne_chunk(pos_tags):
            if hasattr(chunk, 'label'):
                named_entities.append(" ".join(c[0] for c in chunk))
    return {"POS Tags": pos_tags_list, "Named Entities": ", ".join(named_entities) if named_entities else "No named entities detected"}

# Flask Routes (Unchanged)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name, email, password = request.form['name'], request.form['email'], request.form['password']
        db.session.add(User(name=name, email=email, password=password))
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email, password = request.form['email'], request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')
@app.route("/")
def home():
    if 'email' not in session: return redirect('/login')
    return render_template("home.html")

# --- CORRECTED CHATBOT RESPONSE ROUTE ---
@app.route("/get")
def get_bot_response():
    user_query = request.args.get('msg', '').strip()

    if not user_query:
        return "Please provide a message."

    print(f"\n--- New Query Received ---")
    print(f"User Query: '{user_query}'")

    # --- STEP 1: ALWAYS RUN NLP ANALYSIS FOR EVERY QUERY ---
    print("--- Running NLP Analysis ---")
    sentence_type = get_sentence_type(user_query)
    sentiment = get_sentiment(user_query)
    named_entities = get_named_entities_and_pos(user_query)

    if sentiment == "positive": mood = "happy"
    elif sentiment == "negative": mood = "sad"
    else: mood = "neutral"

    print(f"Sentence Type: {sentence_type}")
    print(f"Sentiment: {sentiment}")
    print(f"Mood: {mood}")
    print(f"Named Entities: {named_entities['Named Entities']}")
    print("--------------------------")

    # --- STEP 2: CHECK FOR SPECIFIC QUERY TYPES (e.g., emergency) ---
    lower_query = user_query.lower()
    if "emergency number for" in lower_query:
        situation = lower_query.replace("emergency number for", "").strip()
        print(f"Recognized 'emergency number' query for situation: '{situation}'")
        response_text, number = get_info_from_prolog_file(situation, info_type="number")
        if number and driver:
            print("Attempting to write to Neo4j...")
            try:
                with driver.session() as neo4j_session:
                    # UPDATED to execute_write
                    neo4j_session.execute_write(_create_emergency_number_tx, situation, number)
            except Exception as e:
                print(f"❌ Failed to write to Neo4j: {e}")
        elif not driver:
            print("⚠️ Neo4j driver not available. Skipping database write.")
        return response_text # Return the emergency response

    elif "emergency advice for" in lower_query:
        situation = lower_query.replace("emergency advice for", "").strip()
        print(f"Recognized 'emergency advice' query for situation: '{situation}'")
        response_text, advice = get_info_from_prolog_file(situation, info_type="advice")
        if advice and driver:
            print("Attempting to write to Neo4j...")
            try:
                with driver.session() as neo4j_session:
                    # UPDATED to execute_write
                    neo4j_session.execute_write(_create_emergency_advice_tx, situation, advice)
            except Exception as e:
                print(f"❌ Failed to write to Neo4j: {e}")
        elif not driver:
            print("⚠️ Neo4j driver not available. Skipping database write.")
        return response_text # Return the emergency response

    # --- STEP 3: IF NOT AN EMERGENCY QUERY, PROCEED WITH GENERAL AIML LOGIC ---
    if "define" in lower_query:
        word = lower_query.replace("define", "").strip()
        if word:
            definition = get_definition(word)
            bot_primary.setPredicate("define_word", word)
            bot_primary.setPredicate("definition", definition)
            return bot_primary.respond(user_query) or f"Definition not found for '{word}'."
        else:
            return "Please specify a word to define."

    # Store NLP results in AIML predicates for general conversation
    bot_primary.setPredicate("sentence_type", sentence_type.lower())
    bot_primary.setPredicate("sentiment", sentiment.lower())
    bot_primary.setPredicate("user_mood", mood)
    bot_primary.setPredicate("ner_tags", str(named_entities))

    # Get bot response from primary AIML kernel
    bot_response = bot_primary.respond(user_query)

    # Fallback to secondary AIML if needed
    if not bot_response.strip():
        secondary_aiml_directory = os.getenv("SECONDARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PemaAimlfiles")
        temp_bot = aiml.Kernel()
        load_aiml_files(temp_bot, secondary_aiml_directory)
        bot_response = temp_bot.respond(user_query)
        print("Secondary AIML files loaded temporarily for this query.")

    return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    if driver:
        driver.close()
        print("\nNeo4j connection closed.")


#run "MATCH (n) RETURN n" in neo4j
