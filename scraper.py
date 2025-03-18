import requests
from bs4 import BeautifulSoup

def get_news(company):
    url = f"https://www.bing.com/news/search?q={company}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("a"):  # Check all anchor tags
        title = item.text.strip()
        link = item.get("href")

        # Ensure link is valid
        if title and link and link.startswith("http"):
            articles.append({"title": title, "link": link})

    return articles if articles else {"error": "No news found"}

# Test the function
if __name__ == "__main__":
    news = get_news("Tesla")
    print(news)  # Check if titles and links are being fetched
