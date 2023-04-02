import sys
from moviepy.editor import *

# Extract audio from a video file

VIDEO_FILE = ""
AUDIO_FILE = ""

video = VideoFileClip(VIDEO_FILE)
video.audio.write_audiofile(VIDEO_FILE)