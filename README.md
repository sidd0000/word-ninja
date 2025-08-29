🥷 Word Ninja – Word Splitter App

A lightweight web application that splits concatenated words into individual words using a FastAPI backend and a Streamlit frontend.

🚀 Features

FastAPI Backend: Efficiently processes word splitting requests.

Streamlit Frontend: Provides an interactive user interface.

Real-time Results: Instantly see the split words as you type.

Easy Setup: Simple steps to get the app running locally.

🛠️ Getting Started
1. Clone or Download the Repository

Clone the repository using Git:

git clone https://github.com/sidd0000/word-ninja.git
cd word-ninja


Or download the ZIP file and extract it to a folder of your choice.



3. Install Dependencies

Install the required libraries:

pip install -r requirements.txt

4. Run the FastAPI Backend

Start the FastAPI backend:

python nlp2.py


The backend will run at: http://127.0.0.1:8000

5. Run the Streamlit Frontend

Open a new terminal in the same folder and start the Streamlit frontend:

streamlit run frontend.py


The frontend will open at: http://localhost:8501

🔄 How It Works

Input: Enter a concatenated word (e.g., wordninja).

Processing: The backend splits the word into individual words using a probabilistic algorithm.

Output: The frontend displays the split words in real-time.

📂 Project Structure
word-ninja/
├── nlp2.py           # FastAPI backend
├── frontend.py       # Streamlit frontend
├── requirements.txt  # Python dependencies
├── test_word_splitter.py  # Unit tests
└── README.md         # Project documentation
📌 Notes

Keep the backend running while using the frontend.

Restart the apps if you make changes to nlp2.py or frontend.py.

Using a virtual environment is recommended to avoid dependency conflicts.
