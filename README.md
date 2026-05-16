# TikTok Video Helper Bot

## Project Description

TikTok Video Helper Bot is a Python Telegram bot that allows users to send a public TikTok video link and receive the downloaded video back in Telegram.

This project was created as a final Python project to demonstrate Telegram bot development, Object-Oriented Programming, JSON file storage, exception handling, modular code, and teamwork through GitHub commits.

## Team Members and Roles

- Abylaikhan — Telegram bot handlers, link validation, README
- Arsen — TikTok downloader class, JSON history storage, tests

## Main Features

- Telegram bot interface
- `/start` and `/help` commands
- TikTok link validation
- Support for long TikTok links
- Support for short TikTok links such as `vt.tiktok.com` and `vm.tiktok.com`
- TikTok video downloading using `yt-dlp`
- Sending downloaded video back to the user
- Download history saved in JSON file
- `/history` command to view recent downloads
- `/clear_history` command to clear user history
- Error handling for invalid links and failed downloads
- Unit tests for JSON history storage

## Usage Examples

Valid long TikTok link example:

```text
https://vt.tiktok.com/ZSxFe6exe/

## Technologies Used

- Python
- python-telegram-bot
- yt-dlp
- requests
- python-dotenv
- pytest
- JSON file storage
- Git and GitHub

## Project Structure

```text
tiktok_downloader_bot/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── bot/
│   ├── __init__.py
│   ├── handlers.py
│   └── keyboards.py
│
├── services/
│   ├── __init__.py
│   └── tiktok_downloader.py
│
├── storage/
│   ├── __init__.py
│   └── history_storage.py
│
├── utils/
│   ├── __init__.py
│   └── link_validator.py
│
├── data/
│   └── history.json
│
└── tests/
    └── test_history_storage.py
    
## Troubleshooting

If the bot cannot download a TikTok video, possible reasons are:

- The TikTok video is private.
- The link is restricted by region.
- TikTok blocks the request.
- Browser cookies are not available.
- The internet connection is unstable.

Possible solutions:

- Try a public TikTok video.
- Try a long TikTok link instead of a short link.
- Open TikTok in Google Chrome before running the bot.
- Update `yt-dlp`:

```bash
python3 -m pip install -U yt-dlp