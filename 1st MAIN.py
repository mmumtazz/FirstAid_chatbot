#This is the aiml, prolog and login page code only(without neo4j)
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
import re  # Only for the new Prolog implementation

# Initialize nltk for sentence parsing
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create database tables
with app.app_context():
    db.create_all()

# Load AIML files
def load_aiml_files(kernel, directory):
    if os.path.exists(directory):
        files = [f for f in os.listdir(directory) if f.endswith(".aiml")]
        for filename in files:
            file_path = os.path.join(directory, filename)
            kernel.learn(file_path)

# Initialize AIML kernel for the primary bot
bot_primary = aiml.Kernel()
primary_aiml_directory = os.getenv("PRIMARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\Aimldata")
load_aiml_files(bot_primary, primary_aiml_directory)

# --- NEW: Manual Prolog File Reader Function ---
def get_info_from_prolog_file(situation, info_type="number"):
    prolog_file_path = os.getenv("PROLOG_FILE_PATH",
                               r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PrologFiles\EmergencyContacts.pl")

    fact_name = ""
    response_template = ""

    if info_type == "number":
        fact_name = "get_emergency_number"
        response_template = "The emergency number for {0} is {1}."
    elif info_type == "advice":
        fact_name = "get_emergency_advice"
        response_template = "For {0}, here is some advice: {1}."
    else:
        return "Internal error: Invalid info_type."

    try:
        with open(prolog_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('%') or not line.strip():
                    continue
                match = re.search(rf"{fact_name}\('{situation}',\s*'?(.*?)'?\)\.", line)
                if match:
                    value = match.group(1)
                    return response_template.format(situation, value)
        return f"Sorry, I couldn't find any information for '{situation}'."
    except FileNotFoundError:
        return "ERROR: The chatbot's knowledge base file is missing."
    except Exception as e:
        return f"An error occurred while reading the knowledge base."
# --- END of Manual Prolog File Reader ---

def get_definition(word):
    try:
        synset = wn.synset(word + '.n.01')
        return synset.definition()
    except Exception as e:
        return f"Definition not found for '{word}'. Error: {str(e)}"

# Function to analyze sentence type (question, exclamation, statement)
def get_sentence_type(sentence):
    if sentence.endswith("!"):
        return "an exclamation"
    elif sentence.endswith("?"):
        return "a question"
    else:
        return "a statement"

# Function to analyze sentiment (positive, negative, neutral)
def get_sentiment(sentence):
    analysis = TextBlob(sentence)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    if sentence.endswith("!") or "!" in sentence:
        sentiment = "positive" if polarity > 0 else "negative"
    elif sentence.endswith("?"):
        sentiment = "neutral"

    if "?" in sentence and any(word in sentence.lower() for word in ["sad", "happy", "angry"]):
        sentiment = "neutral"

    return sentiment

# Function to get named entities and POS tags
def get_named_entities_and_pos(sentence):
    sentence = sentence.title()
    sentences = sent_tokenize(sentence)
    pos_tags_list = []
    named_entities = []

    for sent in sentences:
        words = word_tokenize(sent)
        pos_tags = pos_tag(words)
        pos_tags_list.append(pos_tags)
        chunked_sentence = ne_chunk(pos_tags)

        for chunk in chunked_sentence:
            if hasattr(chunk, 'label'):
                entity_name = " ".join(c[0] for c in chunk)
                named_entities.append(entity_name)

    return {
        "POS Tags": pos_tags_list,
        "Named Entities": ", ".join(named_entities) if named_entities else "No named entities detected"
    }

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

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

# Main chatbot route with authentication check
@app.route("/")
def home():
    if 'email' not in session:
        return redirect('/login')
    return render_template("home.html")

# Chatbot response route
@app.route("/get")
def get_bot_response():
    user_query = request.args.get('msg', '').strip()

    if not user_query:
        return "Please provide a message."

    # Process sentiment, sentence type, and named entities (RESTORED ORIGINAL NLP FUNCTIONALITY)
    sentence_type = get_sentence_type(user_query)
    sentiment = get_sentiment(user_query)
    named_entities = get_named_entities_and_pos(user_query)

    if sentiment == "positive":
        mood = "happy"
    elif sentiment == "negative":
        mood = "sad"
    else:
        mood = "neutral"

    print(f"User Query: {user_query}")
    print(f"Sentence Type: {sentence_type}")
    print(f"Sentiment: {sentiment}")
    print(f"Mood: {mood}")
    print(f"Named Entities: {named_entities}")

    # Handle specific queries
    if "define" in user_query.lower():
        word = user_query.lower().replace("define", "").strip()
        if word:
            definition = get_definition(word)
            bot_primary.setPredicate("define_word", word)
            bot_primary.setPredicate("definition", definition)
            bot_response = bot_primary.respond(user_query)
            return bot_response if bot_response.strip() else f"Definition not found for '{word}'."
        else:
            return "Please specify a word to define."

    if "sentence" in user_query.lower():
        bot_response = bot_primary.respond(user_query)
        return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

    if "mood" in user_query.lower():
        bot_response = bot_primary.respond(user_query)
        return bot_response if bot_response.strip() else "I'm not sure how you're feeling."

    if "entities" in user_query.lower():
        ner_tags = bot_primary.getPredicate("ner_tags")
        bot_response = bot_primary.respond(user_query)
        return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

    # Handle emergency queries with the NEW Prolog implementation
    if "emergency number for" in user_query.lower():
        situation = user_query.replace("emergency number for", "").strip()
        return get_info_from_prolog_file(situation, info_type="number")

    elif "emergency advice for" in user_query.lower():
        situation = user_query.replace("emergency advice for", "").strip()
        return get_info_from_prolog_file(situation, info_type="advice")

    # Store updated values in AIML predicates
    bot_primary.setPredicate("sentence_type", sentence_type.lower())
    bot_primary.setPredicate("sentiment", sentiment.lower())
    bot_primary.setPredicate("user_mood", mood)
    bot_primary.setPredicate("ner_tags", str(named_entities))

    # Get bot response from primary AIML kernel
    bot_response = bot_primary.respond(user_query)

    # If no response from primary AIML, temporarily load secondary AIML files
    if not bot_response.strip():
        secondary_aiml_directory = os.getenv("SECONDARY_AIML_DIRECTORY", r"C:\Users\LENOVO\Pictures\Camera Roll\CameraRoll\AI4THSemester\firstaid\PemaAimlfiles")
        temp_bot = aiml.Kernel()
        load_aiml_files(temp_bot, secondary_aiml_directory)
        bot_response = temp_bot.respond(user_query)
        print("Secondary AIML files loaded temporarily for this query.")

    return bot_response if bot_response.strip() else "I'm here to help. Can you elaborate more?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,debug=True)
