import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.bbc.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    for item in soup.find_all("a"):
        title = item.get_text().strip()
        link = item.get("href")

        if title and link and "/news" in link:
            full_link = "https://www.bbc.com" + link if link.startswith("/") else link

            articles.append({
                "title": title,
                "url": full_link,
                "source": "BBC"
            })

    return articles