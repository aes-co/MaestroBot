<p align="center">
  <img src="https://github.com/images/mona-whisper.gif" alt="MaestroBot Cat Logo" width="150"/>
</p>

<h1 align="center">
  <b>MaestroBot — The Ultimate Modular Telegram Music Bot</b>
</h1>

<p align="center">
  <i>A blazing-fast, feature-rich, and highly modular Telegram bot designed for seamless music playback in voice chats, built for everyone.</i>
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

## 🎶 **Overview**

**MaestroBot** is an advanced, open-source Telegram music bot built with a robust **modular architecture**. It's designed to provide a rich and interactive music experience in Telegram voice chats, supporting both groups and channels. With its **hybrid library approach** (Pyrogram for userbots/voice calls and python-telegram-bot for core bot interactions), MaestroBot offers unparalleled stability, speed, and a wide array of features for all users.

> Modular, hybrid Telegram music bot for voice chats — powered by Pyrogram + PTB, with a web app and multi-deploy support.

-----

## ✨ Key Features

  * **Real-time Music Playback**: Seamlessly stream audio in Telegram Voice Chats with **real-time "Now Playing" updates** and progress bars.
  * **Interactive Controls**: Full control over playback with inline buttons: `⏪ Rewind`, `⏹️ Stop`, `⏯️ Pause/Resume`, `⏩ Forward`, `⏭️ Skip`, `📜 Lyrics`, and `☰ Menu`.
  * **Automatic Lyrics Search**: Get lyrics for the currently playing song instantly.
  * **Voice Chat Moderation**: Admin commands to mute, unmute, or kick users from voice chats.
  * **Telegram Web App (Mini App)**: A rich, interactive web interface for managing queues, searching music, and controlling playback.
  * **Channel Support**: Deploy and use the bot directly in Telegram Channels.
  * **Music Recommendation Engine**: Get personalized song suggestions based on playback history.
  * **User-selectable Audio Quality**: Choose your preferred audio quality (low, medium, high) to save data or enjoy pristine sound.
  * **Global/Shared Queue Synchronization**: Create and manage synchronized music queues across multiple groups or users.
  * **Creator Support Button**: A dedicated button for users to show appreciation and support the bot's creator (you!).
  * **Mandatory Channel Membership**: Ensure users join your Telegram channel before using the bot, fostering community growth.
  * **Interactive Bot Settings (`/bs`, `/bset`, `/botsetting`)**: Manage bot configurations (like adding sudo users) through an intuitive, **menu-driven interface** directly in Telegram.
  * **Monitoring & Control Commands**: Essential commands like `/restart`, `/ping`, `/speedtest`, and `/status` for easy bot management and health checks.

-----

## 🚀 Supported Deployment Methods

MaestroBot is designed for maximum flexibility and can be deployed on various platforms:

  * [Heroku](https://www.google.com/search?q=%23deploy-to-heroku)
  * [Okteto](https://www.google.com/search?q=%23deploy-to-okteto)
  * [VPS (Docker Recommended)](https://www.google.com/search?q=%23deploy-to-vps)
  * [Local Machine (Docker Recommended)](https://www.google.com/search?q=%23deploy-locally)
  * [Termux](https://www.google.com/search?q=%23deploy-to-termux)
  * [Replit](https://www.google.com/search?q=%23deploy-to-replit)

-----

## 🔧 Necessary Variables

To run MaestroBot, you'll need to set up several environment variables. These are crucial for the bot's functionality and security.

  * `API_ID` - Your Telegram API ID. Get it from [my.telegram.org](https://my.telegram.org/).
  * `API_HASH` - Your Telegram API Hash. Get it from [my.telegram.org](https://my.telegram.org/).
  * `BOT_TOKEN` - Your bot's token from [@BotFather](https://t.me/BotFather).
  * `BOT_USERNAME` - Your bot's username (e.g., `MaestroBot`).
  * `OWNER_ID` - Your Telegram User ID. This user will have full control over the bot.
  * `SUDO_USERS` - (Optional) A space-separated list of Telegram User IDs who will have sudo access (e.g., `123456789 987654321`).
  * `MONGO_URI` - Connection URI for your MongoDB database. Get a free tier from [MongoDB Atlas](https://www.mongodb.com/atlas).
  * `REDIS_URI` - Connection URI for your Redis instance. Get a free tier from [RedisLabs](https://www.google.com/search?q=https://redislabs.com/try-free/).
  * `RABBITMQ_URI` / `KAFKA_URI` - Connection URI for your Message Broker (choose one). Used for inter-service communication.
  * `CREATOR_CHANNEL_ID` - The numeric ID of your mandatory Telegram channel (e.g., `-1001234567890`).
  * `CREATOR_CHANNEL_LINK` - The invite link to your mandatory Telegram channel (e.g., `https://t.me/your_channel_username`).
  * `DONATION_LINK` - (Optional) Your personal donation link (e.g., `https://saweria.co/yourname`).

-----

## ⚙️ Deployment Guides

### Deploy to Heroku

Get the [Necessary Variables](#-necessary-variables) and then click the button below!

<details>
<summary>Deploy to Heroku</summary>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/aes-co/MaestroBot/tree/main">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</details>

### Deploy to Okteto

Get the [Necessary Variables](#-necessary-variables) and then click the button below!

<details>
<summary>Deploy to Okteto</summary>
<br>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/aes-co/MaestroBot">
  <img src="https://img.shields.io/badge/Deploy%20to-Okteto-blue?style=for-the-badge&logo=okteto" alt="Deploy to Okteto">
</a>
</details>

### Deploy to VPS (Docker Recommended)

This is the recommended method for stable, production-grade deployments.

1. **Install Docker & Docker Compose**: Follow official Docker documentation for your VPS OS.
2. **Clone the repository**:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
3. **Create `.env` file**: Copy `.env.sample` to `.env` and fill in your [Necessary Variables](https://www.google.com/search?q=%23necessary-variables).
    ```bash
    cp .env.sample .env
    # Edit .env file with your variables
    ```
4. **Build and run with Docker Compose**:
    ```bash
    docker-compose up --build -d
    ```
    This will build Docker images for each service, set up MongoDB, Redis, and your Message Broker, and run everything in detached mode.

### Deploy Locally

Ideal for development and testing. Docker Compose is highly recommended.

1. **Install Docker & Docker Compose**: Follow official Docker documentation.
2. **Clone the repository**:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
3. **Create `.env` file**: Copy `.env.sample` to `.env` and fill in your [Necessary Variables](https://www.google.com/search?q=%23necessary-variables).
    ```bash
    cp .env.sample .env
    # Edit .env file with your variables
    ```
4. **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    This will run all services in your local environment.

### Deploy to Termux

Suitable for light personal use and testing on Android. External DB/Cache is highly recommended.

1. **Install Termux**: Download from F-Droid.
2. **Update packages and install Python & Git**:
    ```bash
    pkg update && pkg upgrade
    pkg install python git ffmpeg
    ```
3. **Clone the repository**:
    ```bash
    git clone https://github.com/aes-co/MaestroBot.git
    cd MaestroBot
    ```
4. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
5. **Install Python requirements**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Create `.env` file**: Manually create a `.env` file and fill in your [Necessary Variables](https://www.google.com/search?q=%23necessary-variables). Use cloud-hosted MongoDB/Redis.
7. **Run the bot (simplified for Termux)**: You might need to run individual services or a combined script.
    ```bash
    # Example for Core Bot (assuming it's the main entry point)
    python -m maestrobot.__main__
    # Use 'nohup' or 'tmux' to keep it running in background
    ```

### Deploy to Replit

Good for quick demos and small-scale usage. External DB/Cache is mandatory.

1. **Create a new Repl**: Select Python as the language.
2. **Clone the repository**: Use the Replit shell to `git clone https://github.com/aes-co/MaestroBot.git .` (note the dot for current directory).
3. **Install FFmpeg**: Add `apt-get update && apt-get install -y ffmpeg` to your `.replit` file's `run` command or a setup script.
4. **Install Python requirements**: `pip install -r requirements.txt` in the shell.
5. **Set Environment Variables**: Use Replit's "Secrets" tab to add all your [Necessary Variables](https://www.google.com/search?q=%23necessary-variables).
6. **Run the bot**: Configure the `run` command in `.replit` to start your main bot script (e.g., `python -m maestrobot.__main__`). You might need to use a web server (like Flask/FastAPI) to keep the Repl "Always On".

-----

## 📂 Project Structure

.
├── app.json
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── heroku.yml
├── installer.sh
├── install-termux
├── LICENSE
├── okteto-pipeline.yml
├── README.md
├── requirements.txt
├── maestrobot/
│ ├── init.py
│ ├── main.py # Main entry point for the bot application
│ ├── configs.py # Handles loading and accessing environment variables
│ ├── db/ # Database models and interaction logic (MongoDB)
│ │ ├── init.py
│ │ ├── users.py # User profiles, channel membership status
│ │ ├── settings.py # Bot-wide and group-specific settings, sudo users
│ │ ├── queues.py # Music queues (per group and shared/global)
│ │ └── playback_history.py # Stores song playback history for recommendations
│ ├── handlers/ # Core bot command and callback handlers (python-telegram-bot)
│ │ ├── init.py
│ │ ├── start_help.py # /start, /help commands
│ │ ├── music_commands.py # /play, /queue, /nowplaying
│ │ ├── admin_commands.py # Moderation, promote/demote (e.g., /mute, /kick)
│ │ ├── settings_commands.py # /bs, /bset, /botsetting menu interactions
│ │ └── utility_commands.py # /id, /userinfo, /linkchannel, /support, /donate
│ ├── assistant/ # Userbot core logic and orchestration (Pyrogram)
│ │ ├── init.py
│ │ ├── client.py # Pyrogram client setup
│ │ ├── orchestrator.py # Manages the userbot pool, assigns tasks, handles status
│ │ ├── voice_chat.py # PyTgCalls integration for audio streaming in voice chats
│ │ └── userbot_handlers.py # Userbot-specific event handlers (e.g., voice chat join/leave)
│ ├── plugins/ # Modular features, similar to a plugin system
│ │ ├── init.py
│ │ ├── music_controls.py # Handles inline button actions for playback control
│ │ ├── lyrics.py # Lyrics search integration
│ │ ├── recommendations.py # Music recommendation logic and commands
│ │ ├── shared_queue.py # Commands and logic for global/shared queues
│ │ ├── moderation_vc.py # Voice chat specific moderation commands
│ │ ├── monitoring.py # /ping, /speedtest, /status commands
│ │ └── restart.py # /restart command handler
│ ├── media/ # Media processing and downloading
│ │ ├── init.py
│ │ ├── downloader.py # Integrates with yt-dlp for media fetching
│ │ └── transcoder.py # Uses FFmpeg for audio quality conversion and formatting
│ ├── utils/ # General utility functions and helpers
│ │ ├── init.py
│ │ ├── helpers.py # Generic helper functions, decorators
│ │ ├── filters.py # Custom python-telegram-bot filters
│ │ └── web_app.py # Utilities for Telegram Web App integration
│ ├── web_app_backend/ # Backend service for the Telegram Mini App
│ │ ├── init.py
│ │ ├── app.py # Main FastAPI/Flask application for the Web App API
│ │ └── routes.py # Defines API endpoints for the Web App frontend
│ ├── startup/ # Scripts for initial application setup and client connections
│ │ ├── init.py
│ │ ├── bot_client.py # Initializes the python-telegram-bot client
│ │ ├── userbot_clients.py # Initializes Pyrogram clients for the userbot pool
│ │ └── db_connections.py # Handles connections to MongoDB and Redis
│ └── strings/ # Localization files for multi-language support
│ ├── init.py
│ ├── en.yml # English language strings
│ ├── id.yml # Indonesian language strings
│ └── ... (other languages)
├── resources/ # Static assets like logos, fonts, etc.
│ ├── logo.png # Main logo for the bot
│ ├── extras/ # Additional images or markdown files (e.g., tutorials)
│ │ └── mona-whisper.gif # The cat logo
│ └── fonts/ # Custom fonts for image generation (if applicable)
└── scripts/ # Helper scripts for deployment or session generation
├── session_generator.py # Script to generate Pyrogram session strings
└── setup.sh # General setup script for local/Termux deployments


-----

## 📊 Commands & Features

Here's a comprehensive list of commands and features available in MaestroBot:

### 🎵 Music Playback & Control

  * `/play <query>`: Play a song from YouTube/Spotify/etc.
  * `/queue`: Show the current song queue.
  * `/nowplaying`: Display the currently playing song with real-time progress and controls.
  * `/lyrics`: Get lyrics for the current song.
  * `/pause`, `/resume`: Pause or resume playback.
  * `/skip`: Skip to the next song in the queue.
  * `/stop`: Stop playback and clear the queue.
  * `/forward <seconds>`, `/rewind <seconds>`: Seek forward/backward in the current song.
  * `/volume <0-200>`: Adjust bot's volume.
  * `/quality <low/medium/high>`: Set preferred audio quality.

### 🔗 Shared/Global Queue

  * `/createqueue`: Create a new shared queue and get its ID.
  * `/joinqueue <id>`: Join an existing shared queue.
  * `/leavequeue`: Leave the current shared queue.
  * `/myqueue`: View your current shared queue (if joined).

### 🤖 Admin & Moderation

  * `/mute @user`: Mute a user in the voice chat.
  * `/unmute @user`: Unmute a user in the voice chat.
  * `/kick @user`: Kick a user from the voice chat.
  * `/admins`: List group admins.
  * `/promote`, `/demote`: Promote/demote users (if bot is admin with rights).
  * `/lock`, `/unlock`: Lock/unlock certain message types.
  * `/rules`: Set/get group rules.
  * `/welcome`: Set/get welcome message.

### 🛠️ Utilities

  * `/id`: Get your Telegram ID or chat ID.
  * `/userinfo <reply/username>`: Get information about a user.
  * `/groupinfo`: Get information about the current group.
  * `/linkchannel`: Get the mandatory channel link.
  * `/support`, `/donate`: Get information on how to support the creator.

### ⚙️ Bot Settings (Admin Only)

  * `/bs`, `/bset`, `/botsetting`: Access the interactive bot settings menu.
      * `Add Sudo User`: Add a new sudo user by ID.
      * `Remove Sudo User`: Remove a sudo user by ID.
      * `Set Creator Channel`: Update mandatory channel link/ID.
      * `Set Default Volume`: Configure default playback volume.
      * `Manage API Keys`: Update various API keys (e.g., lyrics API).
      * And more... (all managed interactively)

### 📈 Monitoring & Control (Admin Only)

  * `/ping`: Check bot's responsiveness and API latency.
  * `/speedtest`: Run an internet speed test from the bot's server.
  * `/status`: Get detailed status of all bot services (CPU, RAM, service health, assistant status).
  * `/restart`: Gracefully restart the bot's core services.

### 🧠 AI Tools (Future Expansion)

  * `/recommend`: Get music recommendations based on playback history.

-----

## 💡 Technologies

  * **Python 3.10+**: The core programming language for all services.
  * **Pyrogram**: For powerful Userbot (assistant) interactions and native PyTgCalls integration.
  * **python-telegram-bot (PTB)**: For robust Bot API handling and user-friendly command/conversation management.
  * **PyTgCalls**: The official library for Telegram Voice Chat streaming.
  * **MongoDB**: Primary persistent database for all bot data.
  * **Redis**: High-performance cache and Pub/Sub for real-time communication.
  * **RabbitMQ / Kafka**: Message Broker for asynchronous inter-service communication.
  * **Docker / Docker Compose**: For containerization and easy multi-service deployment.
  * **FFmpeg**: Essential media processing tool for audio handling.
  * **HTML / CSS / JavaScript**: For the Telegram Web App (Mini App) frontend.
  * **yt-dlp**: For downloading media from various platforms.

-----

## ❤️ Credits & Acknowledgments

This project stands on the shoulders of giants and is made possible by various open-source contributions and inspirations:

  * **Team Ultroid**: The structure and organizational style of this `README.md` and the overall project directory layout are heavily inspired by the [TeamUltroid/Ultroid](https://github.com/TeamUltroid/Ultroid) project. Their comprehensive userbot design provided invaluable reference.
  * **aes-co/modcore**: The initial `README.md` style, aesthetic, and the foundational idea of a modular Telegram bot framework were inspired by the [aes-co/modcore](https://github.com/aes-co/modcore) project.
  * **Pyrogram**: The robust and modern Telegram MTProto API client library for Python.
  * **python-telegram-bot**: The excellent and user-friendly library for the Telegram Bot API.
  * **PyTgCalls**: The powerful Python library for Telegram Group Calls, developed by MarshalX.
  * **yt-dlp**: The versatile command-line program to download videos and audio from various websites.
  * **FFmpeg**: The leading multimedia framework for handling audio and video.
  * **MongoDB, Redis, RabbitMQ/Kafka**: Essential open-source database and message broker technologies that power the distributed architecture.

We are immensely grateful to the creators and maintainers of these projects and all open-source contributors for their hard work. This project would not be possible without them.

-----

## 🗓️ License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it with proper attribution.

-----

<p align="center">
  <i>Made with ❤️ by <a href="https://t.me/aesneverhere">@aes-co</a></i>
</p>
<p align="center">
  <img src="https://github.com/images/mona-whisper.gif" width="100" alt="mona">
</p>