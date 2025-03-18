###📰 Project Overview

This application scrapes news articles related to a company, analyzes sentiment, performs comparative analysis, and generates a Hindi audio summary.

🔹 Tech Stack: Python, FastAPI, Streamlit, BeautifulSoup, NLTK, gTTS
🔹 Key Features: News extraction, sentiment analysis, Hindi Text-to-Speech (TTS), and comparative analysis.
🛠️ Installation and Setup

Follow these steps to set up the project on your local machine.
🔹 1. Install Python

Ensure Python 3.8+ is installed.
🔗 Download: https://www.python.org/downloads/

Verify installation:

python --version

🔹 2. Clone the Repository (If Available)

git clone https://github.com/your-username/news-summarization-app.git
cd news-summarization-app

OR manually create a project folder Sumarize and place all Python files in it.
🔹 3. Create and Activate Virtual Environment

python -m venv venv

✅ For Windows

venv\Scripts\activate

✅ For macOS/Linux

source venv/bin/activate

🔹 4. Install Required Dependencies

pip install -r requirements.txt

(If requirements.txt is missing, manually install dependencies below.)

pip install requests beautifulsoup4 nltk gtts fastapi uvicorn streamlit

🚀 Running the Project
✅ Step 1: Test Individual Scripts

1️⃣ Test Web Scraping (scraper.py)

python scraper.py

✅ Expected Output: A list of news titles and links.

2️⃣ Test Sentiment Analysis (sentiment_analysis.py)

python sentiment_analysis.py

✅ Expected Output: Positive / Negative / Neutral for sample text.

3️⃣ Test Text-to-Speech (tts.py)

python tts.py

✅ Expected Output: Audio summary in Hindi should play.
✅ Step 2: Start FastAPI Backend

uvicorn api:app --reload

✅ The API will be available at:
👉 http://127.0.0.1:8000

Test API in browser:
👉 http://127.0.0.1:8000/news/Tesla
✅ Expected Output: JSON response with news, sentiment, and summary.
✅ Step 3: Start Streamlit Web App

streamlit run app.py

✅ Open http://localhost:8501 in your browser.
✅ Enter a company name → Click Analyze.
✅ Expected Output:

    News articles with sentiment classification.
    Comparative analysis results.
    Hindi audio summary played automatically.
