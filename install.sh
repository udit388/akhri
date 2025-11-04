#!/usr/bin/env bash
set -e

# Update and install ffmpeg
apt-get update -y
apt-get install -y ffmpeg

# Install Python dependencies
pip install --no-cache-dir -r requirements.txt

# Run Python stream script
python main.py
