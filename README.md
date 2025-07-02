<p align="center">
  <img src="https://github.com/images/mona-whisper.gif" alt="MaestroBot Cat Logo" width="150"/>
</p>

<h1 align="center">
  <b>MaestroBot — The Ultimate Modular Telegram Music Bot</b>
</h1>

<p align="center">
  <i>A blazing-fast, feature-rich, and highly modular Telegram bot for seamless music playback in voice chats, designed for everyone.</i>
</p>

<p align="center">
  <a href="https://github.com/aes-co/MaestroBot"><img src="https://img.shields.io/github/stars/aes-co/MaestroBot?style=flat-square&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/aes-co/MaestroBot/fork"><img src="https://img.shields.io/github/forks/aes-co/MaestroBot?style=flat-square&color=orange" alt="Forks"/></a>
  <a href="https://github.com/aes-co/MaestroBot"><img src="https://img.shields.io/github/repo-size/aes-co/MaestroBot?style=flat-square&color=green" alt="Repo Size"/></a>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square" alt="Python Version"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square" alt="Maintained"/>
  <a href="https://github.com/aes-co/MaestroBot/graphs/contributors"><img src="https://img.shields.io/github/contributors/aes-co/MaestroBot?style=flat-square&color=brightgreen" alt="Contributors"/></a>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/>
</p>

---

## 🎶 Overview

**MaestroBot** is an advanced, open-source Telegram music bot built with a robust **modular architecture**. It provides a rich and interactive music experience in Telegram voice chats for both groups and channels. Leveraging a **hybrid library approach** (Pyrogram for userbots/voice calls and PTB for core bot interactions), MaestroBot delivers outstanding stability, speed, and a comprehensive feature set.

> Modular, hybrid Telegram music bot for voice chats — powered by Pyrogram + PTB, with a web app and multi-deploy support.

---

## ✨ Key Features

- **Real-time Music Playback**: Stream audio in voice chats with "Now Playing" and progress bar.
- **Interactive Controls**: Playback control with inline buttons: ⏪ Rewind, ⏹️ Stop, ⏯️ Pause/Resume, ⏩ Forward, ⏭️ Skip, 📜 Lyrics, ☰ Menu.
- **Automatic Lyrics Search**: Instantly fetch lyrics for the current song.
- **Voice Chat Moderation**: Admin commands for muting/unmuting/kicking users.
- **Telegram Web App (Mini App)**: Manage queues and music via a modern web interface.
- **Channel Support**: Deploy and use directly in Telegram Channels.
- **Music Recommendation Engine**: Personalized suggestions based on playback history.
- **User-selectable Audio Quality**: Choose audio quality (low, medium, high).
- **Global/Shared Queue Sync**: Synchronized queues across groups/users.
- **Creator Support Button**: Dedicated button for user support.
- **Mandatory Channel Membership**: Require users to join your channel before using the bot.
- **Interactive Bot Settings**: Manage config (e.g., sudo users) with a Telegram menu.
- **Monitoring & Control**: `/restart`, `/ping`, `/speedtest`, `/status` commands for bot management.

---

## 🚀 Deployment Methods

MaestroBot can be deployed on several platforms, including:

- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [VPS (Docker Recommended)](#deploy-to-vps-docker)
- [Local Machine (Docker Recommended)](#deploy-locally)
- [Termux](#deploy-to-termux)
- [Replit](#deploy-to-replit)

---

## 🔧 Environment Variables

Set these variables for proper bot operation:

| Variable            | Description                                  | Required |
|---------------------|----------------------------------------------|----------|
| API_ID              | Telegram API ID ([my.telegram.org](https://my.telegram.org/)) | Yes      |
| API_HASH            | Telegram API Hash ([my.telegram.org](https://my.telegram.org/)) | Yes      |
| BOT_TOKEN           | Bot token from [@BotFather](https://t.me/BotFather) | Yes      |
| BOT_USERNAME        | Your bot's username (e.g., MaestroBot)       | Yes      |
| OWNER_ID            | Your Telegram User ID                        | Yes      |
| SUDO_USERS          | (Optional) Space-separated sudo user IDs     | No       |
| MONGO_URI           | MongoDB connection URI ([MongoDB Atlas](https://www.mongodb.com/atlas)) | Yes      |
| REDIS_URI           | Redis connection URI ([RedisLabs](https://redislabs.com/try-free/)) | Yes      |
| RABBITMQ_URI / KAFKA_URI | (Optional) Message Broker URI           | No       |
| CREATOR_CHANNEL_ID  | Numeric ID of your Telegram channel          | Yes      |
| CREATOR_CHANNEL_LINK| Invite link to your Telegram channel         | Yes      |
| DONATION_LINK       | (Optional) Donation link                     | No       |

---

## ⚙️ Deployment Guides

### Deploy to Heroku

1. Prepare [Environment Variables](#-environment-variables).
2. Click the button below:

<details>
<summary>Deploy to Heroku</summary>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/aes-co/MaestroBot/tree/main">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</details>

### Deploy to Okteto

1. Prepare [Environment Variables](#-environment-variables).
2. Click the button below:

<details>
<summary>Deploy to Okteto</summary>
<br>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/aes-co/MaestroBot">
  <img src="https://img.shields.io/badge/Deploy%20to-Okteto-blue?style=for-the-badge&logo=okteto" alt="Deploy to Okteto">
</a>
</details>

### Deploy to VPS (Docker)

**Recommended for production!**

1. Install Docker & Docker Compose.
2. Clone this repo:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
3. Copy `.env.sample` to `.env` and fill in your [environment variables](#-environment-variables).
    ```bash
    cp .env.sample .env
    # Edit .env with your variables
    ```
4. Build and run:
    ```bash
    docker-compose up --build -d
    ```

### Deploy Locally

1. Install Docker & Docker Compose.
2. Clone the repository:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
3. Fill `.env` as above.
4. Run:
    ```bash
    docker-compose up --build
    ```

### Deploy to Termux

1. Install Termux from F-Droid.
2. Update and install dependencies:
    ```bash
    pkg update && pkg upgrade
    pkg install python git ffmpeg
    ```
3. Clone the repo:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
4. (Optional) Create virtual env:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
5. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
6. Create `.env` and fill variables.
7. Run:
    ```bash
    python -m maestrobot.__main__
    ```

### Deploy to Replit

1. Create a new Repl (Python).
2. Clone repo in shell:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git .
    ```
3. Install ffmpeg and requirements.
4. Set environment variables in Secrets tab.
5. Set run command to:
    ```bash
    python -m maestrobot.__main__
    ```

---

## 📂 Project Structure

```
MaestroBot/
├── app.json
├── docker-compose.yml
├── Dockerfile
├── heroku.yml
├── okteto-pipeline.yml
├── requirements.txt
├── README.md
├── maestrobot/
│   ├── main.py
│   ├── configs.py
│   ├── db/
│   ├── handlers/
│   ├── assistant/
│   ├── plugins/
│   ├── media/
│   ├── utils/
│   ├── web_app_backend/
│   ├── startup/
│   └── strings/
├── resources/
│   ├── logo.png
│   └── extras/
└── scripts/
```

---

## 📊 Commands & Features

### Music Playback & Controls

- `/play <query>`: Play music from YouTube/Spotify/etc.
- `/queue`: Show current queue.
- `/nowplaying`: Show currently playing song with controls.
- `/lyrics`: Fetch lyrics for the current song.
- `/pause`, `/resume`: Pause or resume playback.
- `/skip`: Skip current song.
- `/stop`: Stop playback and clear queue.
- `/forward <seconds>`, `/rewind <seconds>`: Seek through current song.
- `/volume <0-200>`: Set playback volume.
- `/quality <low/medium/high>`: Set audio quality.

### Shared/Global Queue

- `/createqueue`: Create a shared queue.
- `/joinqueue <id>`: Join an existing queue.
- `/leavequeue`: Leave current shared queue.
- `/myqueue`: Show your shared queue.

### Admin & Moderation

- `/mute @user`: Mute user in VC.
- `/unmute @user`: Unmute user in VC.
- `/kick @user`: Remove user from VC.
- `/admins`: List group admins.
- `/promote`, `/demote`: Manage roles.
- `/lock`, `/unlock`: Control message types.
- `/rules`: Set/group rules.
- `/welcome`: Set welcome message.

### Utilities

- `/id`: Show your or chat ID.
- `/userinfo <username/reply>`: Show info about user.
- `/groupinfo`: Show group info.
- `/linkchannel`: Show channel link.
- `/support`, `/donate`: Show support/donation info.

### Bot Settings (Admin)

- `/bs`, `/bset`, `/botsetting`: Access settings menu (add/remove sudo, channel setup, volume, API keys, etc).

### Monitoring & Control (Admin)

- `/ping`: Check bot status.
- `/speedtest`: Run server speedtest.
- `/status`: Show service health.
- `/restart`: Restart bot.

### AI Tools (Planned)

- `/recommend`: Get music recommendations.

---

## 💡 Technologies

- **Python 3.10+**
- **Pyrogram** (userbot, PyTgCalls integration)
- **python-telegram-bot** (Bot API)
- **PyTgCalls** (Voice chat streaming)
- **MongoDB** (Database)
- **Redis** (Cache & Pub/Sub)
- **RabbitMQ/Kafka** (Message broker)
- **Docker/Docker Compose** (Containerization)
- **FFmpeg** (Media processing)
- **yt-dlp** (Media download)
- **HTML/CSS/JS** (Web App)

---

## ❤️ Credits & Acknowledgments

This project is built on and inspired by:

- [TeamUltroid/Ultroid](https://github.com/TeamUltroid/Ultroid)
- [aes-co/modcore](https://github.com/aes-co/modcore)
- Pyrogram, python-telegram-bot, PyTgCalls, yt-dlp, FFmpeg, MongoDB, Redis, RabbitMQ/Kafka, and all open-source contributors.

---

## 🗓️ License

MIT License — see [LICENSE](LICENSE).

---

<p align="center">
  <i>Made with ❤️ by <a href="https://t.me/aesneverhere">@aes-co</a></i>
</p>
<p align="center">
  <img src="https://github.com/images/mona-whisper.gif" width="100" alt="mona">
</p>
