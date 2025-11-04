import os
import time

# 🎞 Dropbox video link (direct link form)
VIDEO_URL = "https://www.dropbox.com/scl/fi/ym9z7i7qupuf2vc1x8hhb/ram.mp4.mp4?rlkey=io2vz85n3rh6psjdh0g15afqi&st=ut3bo8im&dl=1"

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
