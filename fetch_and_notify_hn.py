import os
import requests

# Get the Discord webhook URLs from environment variable (comma-separated)
webhook_urls_str = os.environ.get("DISCORD_WEBHOOK")
if not webhook_urls_str:
    raise Exception("DISCORD_WEBHOOK environment variable not set.")

# Parse comma-separated webhook URLs and remove any whitespace
webhook_urls = [url.strip() for url in webhook_urls_str.split(',') if url.strip()]
if not webhook_urls:
    raise Exception("No valid webhook URLs found in DISCORD_WEBHOOK environment variable.")

print(f"Found {len(webhook_urls)} webhook URL(s)")

# Fetch top stories from Hacker News
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
top_story_ids = response.json()[:10]

for story_id in top_story_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
    title = story.get("title", "(No Title)")
    hn_link = f"https://news.ycombinator.com/item?id={story_id}"
    message = f"{title}\n{hn_link}"
    payload = {"content": message}
    
    # Send to all webhook URLs
    for webhook_url in webhook_urls:
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print(f"Successfully sent story '{title}' to webhook")
            else:
                print(f"Failed to send to webhook: {response.status_code}")
        except Exception as e:
            print(f"Error sending to webhook: {e}") 