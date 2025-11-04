import os
import time

# 🎞 Google Drive video link (converted to direct link)
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1TDKD9ZrzdhqcjUqai5-TeHRadmVsLKdg"

# 🔑 YOUTUBE STREAM KEY (apni nayi key yaha daalo)
YOUTUBE_STREAM_KEY = "z33m-9y0h-z7w0-4qhy-9vgd"

while True:
    os.system(f'ffmpeg -re -stream_loop -1 -i "{VIDEO_URL}" -c:v libx264 -c:a aac -f flv "rtmp://a.rtmp.youtube.com/live2/{z33m-9y0h-z7w0-4qhy-9vgd}"')
    time.sleep(5)
