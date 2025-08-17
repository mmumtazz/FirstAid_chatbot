# Flask & Neo4j First-Aid Chatbot 🧠💡

A smart first-aid and emergency preparedness chatbot built with Flask, Neo4j, and a multi-layered AI approach.

---

## About The Project

Welcome to the RescueReady Chatbot project! This is a full-stack chatbot built using Python, AIML (Artificial Intelligence Markup Language), and the Flask framework. Initially inspired by the work of Pema Gurung and the capabilities of prize-winning bots like kuki.ai, this project demonstrates a powerful hybrid AI model.

The core of the chatbot is **rule-based**, using AIML and a Prolog knowledge base to provide accurate, scripted responses for specific first-aid and emergency scenarios. This foundation is then enhanced with a **Natural Language Processing (NLP)** pipeline to understand user sentiment and context, creating a more dynamic and intelligent conversational experience.

## Project Stages Explained

### 📁 `01-SQLAlchemy-Version`
-   **Description:** The initial version of the chatbot.
-   **Authentication:** User login and registration are handled by **SQLAlchemy** with a SQLite database.
-   **Features:** Includes the full AIML, NLP, and Prolog-reading capabilities.

### 📁 `02-Hybrid-Version`
-   **Description:** A transitional version exploring graph database integration.
-   **Authentication:** User login remains on **SQLAlchemy**.
-   **Neo4j Integration:** The chatbot now writes emergency situation and contact data to **Neo4j**, demonstrating a hybrid database architecture.

### 📁 `03-Final-Neo4j-Version` (Recommended)
-   **Description:** The final and most advanced version of the application.
-   **Authentication:** **SQLAlchemy is completely removed.** The entire user authentication system (login/registration) is now handled natively by **Neo4j**.
-   **Features:** A fully integrated system where all persistent data, from user accounts to chatbot-learned facts, resides in the graph database.

### 📁 `04-Neo4j-Practice-Scripts`
-   **Description:** Contains standalone Python scripts used for practicing and testing Cypher queries with the `neo4j` driver.


## Features 🌟

-   **Secure User Authentication:** A complete login and registration system built purely with **Neo4j**, using bcrypt for secure password hashing.
-   **Rule-Based Core:** Utilizes AIML with a primary and secondary kernel structure. If the primary "first-aid" brain doesn't have an answer, it dynamically falls back to a secondary, more general knowledge base.
-   **NLP Pipeline:** Integrates **NLTK** and **TextBlob** to analyze user input for:
    -   **Sentiment Analysis:** Detects if the user's mood is positive, negative, or neutral.
    -   **Named Entity Recognition:** Identifies proper nouns like names and locations.
    -   **Sentence Typing:** Understands if a message is a statement, question, or exclamation.
-   **External Knowledge Base:** Connects to a **Prolog** (`.pl`) file to instantly retrieve critical information like emergency numbers and advice, which is then stored in Neo4j.
-   **Custom Web Interface:** A responsive and stylish chat UI built with HTML, CSS, and jQuery, personalized with the logged-in user's name.

## Technology Stack 🛠️

-   **Backend:** Flask
-   **Database:** Neo4j
-   **Conversational AI:** `py-aiml`
-   **NLP:** NLTK, TextBlob
-   **Password Hashing:** bcrypt

## Installation

To run this project locally, please follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install Flask neo4j py-aiml nltk textblob bcrypt
    ```

4.  **Set up the Neo4j Database:**
    -   Make sure your Neo4j Desktop application is running.
    -   Open the Neo4j Browser and run this one-time command to ensure unique users:
        ```cypher
        CREATE CONSTRAINT FOR (u:User) REQUIRE u.email IS UNIQUE
        ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```

6.  The application will be available at **`http://127.0.0.1:5001/`**. Navigate to the `/register` page to create your first account.

## Future Plans 

-   **Save Chat History:** Implement functionality to save conversation logs to Neo4j, linked to user nodes.
-   **Speech Integration:** Add Speech-to-Text and Text-to-Speech capabilities for a hands-free user experience.
-   **Expand Knowledge Base:** Greatly expand the AIML and Prolog files to cover a wider range of first-aid and emergency scenarios.

## Acknowledgments

-   Inspired by the foundational AIML chatbot project by **[Pema Gurung](https://github.com/pemagrg1)**..
-   Thanks to **[kuki.ai](https://www.kuki.ai/)** for being a benchmark in the world of rule-based chatbots.
