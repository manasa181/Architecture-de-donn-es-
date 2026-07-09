import json
from collections import Counter

with open("data/silver/clean_articles.json", "r", encoding="utf-8") as f:
    data = json.load(f)

sources = [article["source"] for article in data]

stats = Counter(sources)

result = [{"source": k, "count": v} for k, v in stats.items()]

with open("data/gold/analytics.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("Transformation terminée ✔")