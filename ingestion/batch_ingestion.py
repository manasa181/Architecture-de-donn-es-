import json
import os
from scraper.scraper import scrape

data = scrape()

# créer dossier automatiquement
os.makedirs("data/bronze", exist_ok=True)

with open("data/bronze/articles.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Données stockées en Bronze ✔")