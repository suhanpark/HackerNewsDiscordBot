import os
import requests

# Get the Discord webhook URL from environment variable
webhook_url = os.environ.get("DISCORD_WEBHOOK")
if not webhook_url:
    raise Exception("DISCORD_WEBHOOK environment variable not set.")

# Fetch top stories from Hacker News
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
top_story_ids = response.json()[:10]

for story_id in top_story_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
    title = story.get("title", "(No Title)")
    hn_link = f"https://news.ycombinator.com/item?id={story_id}"
    message = f"{title}\n{hn_link}"
    payload = {"content": message}
    requests.post(webhook_url, json=payload) 