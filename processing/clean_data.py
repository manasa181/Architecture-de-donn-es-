import json
import re

with open("data/bronze/articles.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []

for article in data:
    title = article["title"]

    if len(title) > 5:
        clean_title = re.sub(r"\s+", " ", title)

        cleaned.append({
            "title": clean_title,
            "url": article["url"],
            "source": article["source"]
        })

with open("data/silver/clean_articles.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=4, ensure_ascii=False)

print("Nettoyage terminé ✔")