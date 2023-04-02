from pydub import AudioSegment
import time

# Load the audio file
audio_file = AudioSegment.from_wav('audio.wav')

# Get the length of the audio file in milliseconds
audio_length = len(audio_file)

# Calculate the split point at half of the audio file length
parts = 6
split_point = audio_length // parts

# Split the audio file into two
for i in range(parts):
    n = i + 1
    audio_part = audio_file[split_point*i:split_point*n]
    audio_part.export(f'audio_{n}.wav', format='wav')
    time.sleep(1)
