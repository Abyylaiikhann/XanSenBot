# Project Report: TikTok Video Helper Bot

## 1. Problem Statement

Many users want a simple way to process public TikTok video links directly inside Telegram. Usually, users need to open different websites, copy links, deal with advertisements, or install extra applications. This can be uncomfortable and time-consuming.

The problem of this project is to create a Telegram bot that can receive a public TikTok video link, check whether the link is valid, download the video, and send it back to the user inside Telegram. The project also needs to demonstrate Python programming concepts such as Object-Oriented Programming, JSON file storage, exception handling, modular code structure, and teamwork using GitHub commits.

## 2. Solution Overview

Our solution is a Python Telegram bot called TikTok Video Helper Bot. The user sends a TikTok link to the bot. The bot checks if the message contains a valid TikTok link. If the link is valid, the bot downloads the video using the `yt-dlp` library and sends the downloaded video back to the user.

The bot supports both long TikTok links and short TikTok links such as `vt.tiktok.com` and `vm.tiktok.com`. It also saves the user’s download history in a JSON file. The user can view the history using the `/history` command and clear it using `/clear_history`.

The bot includes error handling, so if the link is invalid or the video cannot be downloaded, the program does not crash. Instead, the bot sends a clear error message to the user.

## 3. Main Features

The main features of the project are:

- Telegram bot interface
- `/start` and `/help` commands
- TikTok link validation
- Support for long and short TikTok links
- TikTok video downloading
- Sending video back to the user
- JSON download history storage
- `/history` command
- `/clear_history` command
- Exception handling for errors
- Unit tests for the history storage manager

## 4. System Design

The project uses a modular structure. Each part of the program has its own responsibility.

```text
tiktok_downloader_bot/
│
├── main.py
├── config.py
├── bot/
│   ├── handlers.py
│   └── keyboards.py
├── services/
│   └── tiktok_downloader.py
├── storage/
│   └── history_storage.py
├── utils/
│   └── link_validator.py
├── data/
│   └── history.json
└── tests/
    └── test_history_storage.py

## 5. Arsen Defense Notes

Arsen can explain the technical backend part of the project.

Main points to explain:

- how the `TikTokDownloader` class works
- why the project uses `yt-dlp`
- how short TikTok links are resolved before downloading
- how browser cookies help with TikTok downloading
- how `DownloadError` prevents the bot from crashing
- how JSON download history is saved and loaded
- how unit tests check the history storage manager

Example defense answer:

“In my part, I worked on the downloader and data storage. I created the TikTokDownloader class, which uses yt-dlp to download public TikTok videos. I also added support for short TikTok links and used exception handling with DownloadError. For data persistence, I created HistoryStorage, which saves user download history in a JSON file. I also added unit tests to check that the history manager works correctly.”