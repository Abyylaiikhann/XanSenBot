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