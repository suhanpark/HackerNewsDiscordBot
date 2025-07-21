# Hackernews Discord Bot

This project posts the top 3 stories from Hacker News to a Discord channel every day using a GitHub Actions workflow.

## Features
- Fetches the top 3 stories from Hacker News daily.
- Posts story titles and direct links to a specified Discord channel via webhook.
- Automated using GitHub Actions.

## Setup
1. **Discord Webhook**: Add your Discord webhook URL as a GitHub secret named `DISCORD_WEBHOOK`.
2. **Workflow**: The workflow runs daily at 9:00 UTC and can also be triggered manually.

## How it Works
- The workflow runs `fetch_and_notify_hn.py`, which:
  - Fetches the top 3 stories from Hacker News.
  - Formats their titles and links.
  - Posts them to Discord using the webhook.

Feel free to clone and do what you will with this!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

