import os
import time

# 🎞 Google Drive video link (direct link format)
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1TDKD9ZrzdhqcjUqai5-TeHRadmVsLKdg"

# 🔑 YouTube Stream Key (Render Environment Variable se lega)
YOUTUBE_STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY")

if not YOUTUBE_STREAM_KEY:
    raise SystemExit("⚠️ Please set YOUTUBE_STREAM_KEY in Render Environment Variables.")

# 🔁 Stream loop
while True:
    os.system(
        f'ffmpeg -re -stream_loop -1 -i "{VIDEO_URL}" '
        f'-c:v libx264 -c:a aac -f flv '
        f'"rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_STREAM_KEY}"'
    )
    time.sleep(5)
