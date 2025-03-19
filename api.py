from fastapi import FastAPI
from scraper import get_news
from sentiment_analysis import get_sentiment
from tts import text_to_speech
from collections import Counter

app = FastAPI()

@app.get("/news/{company}")
def fetch_news(company: str):
    articles = get_news(company)

    if not articles or "error" in articles:
        return {"error": "No news found"}

    for article in articles:
        article["sentiment"] = get_sentiment(article["title"])

    # Count sentiment distribution
    sentiment_counts = Counter(article["sentiment"] for article in articles)

    # Generate Final Sentiment Analysis
    if sentiment_counts["Positive"] > sentiment_counts["Negative"]:
        final_analysis = f"{company} की खबरें ज्यादातर सकारात्मक हैं। कंपनी की संभावनाएँ बढ़ सकती हैं।"
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"]:
        final_analysis = f"{company} की खबरें ज्यादातर नकारात्मक हैं। कंपनी को चुनौतियों का सामना करना पड़ सकता है।"
    else:
        final_analysis = f"{company} की खबरें मिश्रित हैं। स्थिति स्पष्ट नहीं है।"

    # Generate Hindi Speech
    text_to_speech(final_analysis)

    return {
        "company": company,
        "articles": articles,
        "sentiment_distribution": sentiment_counts,
        "Final Sentiment Analysis": final_analysis
    }
