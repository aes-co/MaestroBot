#!/bin/bash

set -e

echo -e "\n🚀 MaestroBot Installer\n"

# Cek dependensi sistem
echo -e "📦 Memeriksa dan menginstal dependensi sistem...\n"

if command -v apt >/dev/null; then
  sudo apt update
  sudo apt install -y git python3 python3-venv python3-pip ffmpeg
elif command -v pkg >/dev/null; then
  pkg update -y
  pkg install -y git python ffmpeg
else
  echo "❌ Tidak dapat menentukan manajer paket. Instal secara manual."
  exit 1
fi

# Siapkan direktori kerja
WORKDIR="maestrobot"
if [ ! -d "$WORKDIR" ]; then
  echo -e "📁 Mengkloning repositori MaestroBot...\n"
  git clone https://github.com/aes-co/maestrobot.git "$WORKDIR"
fi

cd "$WORKDIR"

# Setup virtualenv
echo -e "\n🐍 Membuat dan mengaktifkan lingkungan virtual Python...\n"
python3 -m venv venv
source venv/bin/activate

# Instal dependensi Python
echo -e "📦 Menginstal dependensi Python...\n"
pip install --upgrade pip
pip install -r requirements.txt

# Siapkan file konfigurasi
if [ ! -f ".env" ]; then
  echo -e "\n⚙️ Menyalin konfigurasi default...\n"
  cp .env.example .env
  echo "📌 Edit file .env untuk mengisi TOKEN, MONGO_URL, dsb."
fi

# Jalankan bot
echo -e "\n✅ Instalasi selesai!"
echo "💡 Untuk menjalankan MaestroBot:"
echo "source venv/bin/activate && python -m maestrobot"
