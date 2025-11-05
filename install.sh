#!/usr/bin/env bash
set -e

# 🛠 Install ffmpeg
apt-get update -y
apt-get install -y ffmpeg

# 🐍 Install Python requirements
pip install -r requirements.txt

# 🚀 Start the stream
python main.py
