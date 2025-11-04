#!/bin/bash
set -e

# Update apt-get and install ffmpeg
apt-get update -y
apt-get install -y ffmpeg

# Install python dependencies
pip install --no-cache-dir -r requirements.txt

# Run the main script
python main.py
