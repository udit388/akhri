#!/usr/bin/env bash
set -e

echo "🔧 Updating and installing FFmpeg..."
apt-get update -y
apt-get install -y software-properties-common
add-apt-repository ppa:jonathonf/ffmpeg-4 -y || true
apt-get update -y
apt-get install -y ffmpeg

echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

echo "🎬 Starting Stream..."
python3 main.py
