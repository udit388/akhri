import os
import time

# 🎞 Google Drive video link
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1TDKD9ZrzdhqcjUqai5-TeHRadmVsLKdg"

# 🔑 YouTube Stream Key (environment variable se lega)
YOUTUBE_STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY")

if not YOUTUBE_STREAM_KEY:
    raise SystemExit("⚠️ Set YOUTUBE_STREAM_KEY in Render Environment Variables.")

# 🔁 Loop stream forever
while True:
    os.system(f'ffmpeg -re -stream_loop -1 -i "{VIDEO_URL}" -c:v libx264 -c:a aac -f flv "rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_STREAM_KEY}"')
    time.sleep(5)


