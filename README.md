🤖 AI Skill \& Job Workflow Assistant
An AI-powered career \& learning planner that generates a personalized 4-week workflow to help you achieve your career goals. Built with Streamlit \& Gemini AI.

🚀 Features
✅ Generates a 4-week learning \& job application workflow
✅ Suggests courses, projects, and interview prep
✅ Uses Google Gemini AI for smart recommendations
✅ Beginner-friendly and customizable

🖥️ Run Locally


1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Ashubegum-11/ai-workflow-assistant.git
cd ai-workflow-assistant

2️⃣ Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy
Edit
pip install streamlit google-generativeai

3️⃣ Set Your Gemini API Key
Create a folder and file:

markdown
Copy
Edit
ai-workflow-assistant/
└── .streamlit/
└── secrets.toml
Inside secrets.toml, add:

toml
Copy
Edit
GEMINI\_API\_KEY = "your\_gemini\_api\_key\_here"
(Your key will remain private and is ignored by GitHub because of .gitignore)



4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
Open the link shown in the terminal (usually http://localhost:8501).

<<<<<<< HEAD
=======
🤖 AI Skill & Job Workflow Assistant
An AI-powered career & learning planner that generates a personalized 4-week workflow to help you achieve your career goals. Built with Streamlit & Gemini AI.
🚀 Features
✅ Generates a 4-week learning & job application workflow
✅ Suggests courses, projects, and interview prep
✅ Uses Google Gemini AI for smart recommendations
✅ Beginner-friendly and customizable
🖥️ Run Locally

1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Ashubegum-11/ai-workflow-assistant.git
cd ai-workflow-assistant

2️⃣ Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:
bash
Copy
Edit
pip install streamlit google-generativeai

3️⃣ Set Your Gemini API Key
Create a folder and file:
markdown
Copy
Edit
ai-workflow-assistant/
└── .streamlit/
└── secrets.toml
Inside secrets.toml, add:
toml
Copy
Edit
GEMINI_API_KEY = "your_gemini_api_key_here"
(Your key will remain private and is ignored by GitHub because of .gitignore)

4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
Open the link shown in the terminal (usually http://localhost:8501).

