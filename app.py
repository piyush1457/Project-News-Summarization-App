import streamlit as st
import requests

st.title("News Summarization and Sentiment Analysis")

company = st.text_input("Enter Company Name")

if st.button("Analyze"):
    if company:
        response = requests.get(f"http://127.0.0.1:8000/news/{company}")
        if response.status_code == 200:
            data = response.json()

            st.write(f"### News Articles for {company}")
            for article in data["articles"]:
                st.write(f"**Title:** {article['title']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write(f"[Read more]({article['link']})")
                st.write("---")

            st.write(f"### Sentiment Distribution:")
            st.write(data["sentiment_distribution"])

            # ✅ Display Final Sentiment Analysis
            st.write(f"### 📊 Final Sentiment Analysis:")
            st.success(data["Final Sentiment Analysis"])

            # ✅ Trigger Hindi TTS
            st.write("🔊 Playing Hindi Summary...")
            tts_response = requests.get(f"http://127.0.0.1:8000/tts/{data['Final Sentiment Analysis']}")  # ✅ Call TTS API
            
            if tts_response.status_code == 200:
                st.success("✅ Audio Generated! Check your system audio.")
            else:
                st.error("❌ Failed to generate audio.")

        else:
            st.error("Failed to fetch news")
