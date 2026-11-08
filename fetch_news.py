import urllib.request
import json

# Fetch top story IDs from Hacker News API
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
req = urllib.request.Request(top_stories_url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as response:
    story_ids = json.loads(response.read().decode())[:5]

stories = []
for item_id in story_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    with urllib.request.urlopen(item_url) as item_res:
        data = json.loads(item_res.read().decode())
        stories.append({
            "title": data.get("title", "No Title"),
            "url": data.get("url", "https://news.ycombinator.com")
        })

# Write formatted output to news.json
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(stories, f, indent=2)
