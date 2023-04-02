from pydub import AudioSegment
from moviepy.editor import *

parts = 6
# Load the video and audio files
video = VideoFileClip("movie.mp4")
audio = AudioSegment.from_wav('audio.wav')

# Get the length of the audio file in milliseconds
audio_length = len(audio)
split_point = audio_length // parts
audio_clips = [AudioSegment.from_wav(f"audio_{i}.wav") for i in range(1, parts+1)]

# Combine the audio clips with 75% volume and fade in/out
combined_audio = AudioSegment.empty()
for i in range(parts):
    audio_clip = audio_clips[i].fade(in_duration=1000, out_duration=1000).apply_gain(-6) # apply a 6dB volume decrease to achieve 75%
    combined_audio = combined_audio.append(audio_clip)

# Overlay the combined audio on top of the existing audio in the video
final_audio = CompositeAudioClip([combined_audio.set_start(split_point*i/1000) for i in range(parts)])
final_audio = final_audio.set_duration(video.duration)

result = video.set_audio(final_audio)
result.write_videofile("movie_with_audio.mp4")
