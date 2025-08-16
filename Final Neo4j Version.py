# Final stable version with Neo4j login and user's exact NLP/AIML logic.
from flask import Flask, render_template, request, redirect, session, url_for
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

# --- Basic App Setup ---
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize NLTK
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)


# --- Neo4j Connection ---
from config import NEO4J_PASSWORD
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
driver = None
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    driver.verify_connectivity()
    print("✅ Neo4j connection successful.")
except Exception as e:
    print(f"❌ Failed to connect to Neo4j: {e}")


# --- AIML Kernel Setup (Primary Only) ---
def load_aiml_files(kernel, directory):
    if os.path.exists(directory):
        print(f"Loading AIML files from: {directory}")
        files = [f for f in os.listdir(directory) if f.endswith(".aiml")]
        for filename in files: kernel.learn(os.path.join(directory, filename))
        return True
    print(f"⚠️  Warning: AIML directory not found at {directory}")
    return False

print("\n--- Initializing AIML Kernel ---")
bot_primary = aiml.Kernel()
primary_aiml_directory = os.getenv("PRIMARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\Aimldata")
if load_aiml_files(bot_primary, primary_aiml_directory):
    print("✅ Primary AIML files loaded successfully.")
print("---------------------------------")


# --- Helper Functions (Neo4j, Prolog) ---
def create_user_in_neo4j(tx, name, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    tx.run("CREATE (u:User {name: $name, email: $email, password: $password})", name=name, email=email, password=hashed_password)
def find_user_in_neo4j(tx, email):
    result = tx.run("MATCH (u:User {email: $email}) RETURN u", email=email)
    return result.single()
def _create_emergency_number_tx(tx, situation, number):
    tx.run("MERGE (s:Situation {name: $situation}) MERGE (n:EmergencyNumber {number: $number}) MERGE (s)-[:HAS_NUMBER]->(n)", situation=situation, number=number)
def _create_emergency_advice_tx(tx, situation, advice):
    tx.run("MERGE (s:Situation {name: $situation}) MERGE (a:Advice {text: $advice}) MERGE (s)-[:HAS_ADVICE]->(a)", situation=situation, advice=advice)
def get_info_from_prolog_file(situation, info_type="number"):
    prolog_file_path = os.getenv("PROLOG_FILE_PATH", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PrologFiles\EmergencyContacts.pl")
    fact_name, response_template = "", ""
    if info_type == "number":
        fact_name, response_template = "get_emergency_number", "The emergency number for {0} is {1}."
    elif info_type == "advice":
        fact_name, response_template = "get_emergency_advice", "For {0}, here is some advice: {1}."
    else: return "Internal error.", None
    try:
        with open(prolog_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('%') or not line.strip(): continue
                match = re.search(rf"{fact_name}\('{situation}',\s*'?(.*?)'?\)\.", line)
                if match:
                    value = match.group(1).strip()
                    return response_template.format(situation.replace('_', ' '), value), value
        return f"Sorry, I couldn't find any information for '{situation.replace('_', ' ')}'.", None
    except FileNotFoundError: return "ERROR: The chatbot's knowledge base file is missing.", None
    except Exception: return "An error occurred reading the knowledge base.", None

# --- YOUR EXACT NLP FUNCTIONS (NO CHANGES) ---
def get_definition(word):
    try:
        synset = wn.synset(word + '.n.01')
        return synset.definition()
    except Exception as e:
        return f"Definition not found for '{word}'. Error: {str(e)}"

def get_sentence_type(sentence):
    if sentence.endswith("!"): return "an exclamation"
    elif sentence.endswith("?"): return "a question"
    else: return "a statement"

def get_sentiment(sentence):
    analysis = TextBlob(sentence)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1: sentiment = "positive"
    elif polarity < -0.1: sentiment = "negative"
    else: sentiment = "neutral"
    if sentence.endswith("!") or "!" in sentence: sentiment = "positive" if polarity > 0 else "negative"
    elif sentence.endswith("?"): sentiment = "neutral"
    if "?" in sentence and any(word in sentence.lower() for word in ["sad", "happy", "angry"]): sentiment = "neutral"
    return sentiment

def get_named_entities_and_pos(sentence):
    sentence = sentence.title()
    sentences = sent_tokenize(sentence)
    pos_tags_list, named_entities = [], []
    for sent in sentences:
        words = word_tokenize(sent)
        pos_tags = pos_tag(words)
        pos_tags_list.append(pos_tags)
        chunked_sentence = ne_chunk(pos_tags)
        for chunk in chunked_sentence:
            if hasattr(chunk, 'label'):
                entity_name = " ".join(c[0] for c in chunk)
                named_entities.append(entity_name)
    return {"POS Tags": pos_tags_list, "Named Entities": ", ".join(named_entities) if named_entities else "No named entities detected"}


# --- Authentication Routes ---
@app.route("/")
def home():
    if 'email' not in session: return redirect(url_for('login'))
    return render_template("home.html", user_name=session.get('name', 'Guest'))
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name, email, password = request.form['name'], request.form['email'], request.form['password']
        if not name or not email or not password: return render_template('register.html', error='All fields are required.')
        if driver:
            try:
                with driver.session() as db_session:
                    db_session.execute_write(create_user_in_neo4j, name, email, password)
                return redirect(url_for('login'))
            except exceptions.ConstraintError: return render_template('register.html', error='An account with this email already exists.')
        return render_template('register.html', error='Database connection is not available.')
    return render_template("register.html")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email, password = request.form['email'], request.form['password']
        if driver:
            with driver.session() as db_session:
                user_record = db_session.execute_read(find_user_in_neo4j, email)
                if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record['u']['password'].encode('utf-8')):
                    session['email'], session['name'] = user_record['u']['email'], user_record['u']['name']
                    print(f"✅ Login successful for '{email}'.")
                    return redirect(url_for('home'))
                else: return render_template('login.html', error='Invalid email or password.')
        return render_template('login.html', error='Database connection is not available.')
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))


# --- START: YOUR EXACT CHATBOT LOGIC (RESTORED) ---
@app.route("/get")
def get_bot_response():
    if 'email' not in session: return "Authentication required.", 401
    user_query = request.args.get('msg', '').strip()
    if not user_query: return "Please provide a message."
    session_id = session['email'] # Added for AIML session management

    # Process sentiment, sentence type, and named entities
    sentence_type = get_sentence_type(user_query)
    sentiment = get_sentiment(user_query)
    named_entities = get_named_entities_and_pos(user_query)
    mood = "happy" if sentiment == "positive" else "sad" if sentiment == "negative" else "neutral"

    print(f"\n--- New Query for {session_id} ---")
    print(f"User Query: '{user_query}'")
    print(f"Sentence Type: {sentence_type}")
    print(f"Sentiment: {sentiment}")
    print(f"Mood: {mood}")
    print(f"Named Entities: {named_entities}") # Prints the whole dictionary as per your code

    # Handle specific queries
    lower_query = user_query.lower()
    if lower_query.startswith("define"):
        word = user_query[len("define"):].strip()
        if word:
            definition = get_definition(word)
            # Directly return the definition instead of going through AIML
            return f"The definition of '{word}' is: {definition}"
        else:
            return "Please specify a word to define."

    if "sentence" in lower_query:
        bot_response = bot_primary.respond(user_query, session_id)
        return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

    if "mood" in lower_query:
        bot_response = bot_primary.respond(user_query, session_id)
        return bot_response if bot_response.strip() else "I'm not sure how you're feeling."

    if "entities" in lower_query:
        ner_tags = bot_primary.getPredicate("ner_tags", session_id)
        bot_response = bot_primary.respond(user_query, session_id)
        return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

    # Handle emergency queries
    if "emergency number for" in lower_query:
        situation_text = lower_query.replace("emergency number for", "").strip()
        situation_prolog = situation_text.replace(' ', '_')
        response_text, number = get_info_from_prolog_file(situation_prolog, info_type="number")
        if number and driver:
            with driver.session() as s: s.execute_write(_create_emergency_number_tx, situation_prolog, number)
        return response_text or "Could not find an emergency number."

    elif "emergency advice for" in lower_query:
        situation_text = lower_query.replace("emergency advice for", "").strip()
        situation_prolog = situation_text.replace(' ', '_')
        response_text, advice = get_info_from_prolog_file(situation_prolog, info_type="advice")
        if advice and driver:
            with driver.session() as s: s.execute_write(_create_emergency_advice_tx, situation_prolog, advice)
        return response_text or "Could not find any advice."

    # Store updated values in AIML predicates
    bot_primary.setPredicate("sentence_type", sentence_type.lower(), session_id)
    bot_primary.setPredicate("sentiment", sentiment.lower(), session_id)
    bot_primary.setPredicate("user_mood", mood, session_id)
    bot_primary.setPredicate("ner_tags", str(named_entities), session_id)

    # Get bot response from primary AIML kernel
    bot_response = bot_primary.respond(user_query, session_id)

    # If no response from primary AIML, temporarily load secondary AIML files
    if not bot_response.strip():
        print("⚠️  Primary AIML kernel had no answer. Temporarily loading secondary files...")
        temp_bot = aiml.Kernel()
        secondary_aiml_directory = os.getenv("SECONDARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PemaAimlfiles")
        load_aiml_files(temp_bot, secondary_aiml_directory)
        bot_response = temp_bot.respond(user_query, session_id)

    return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"
# --- END: YOUR EXACT CHATBOT LOGIC (RESTORED) ---


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    if driver:
        driver.close()