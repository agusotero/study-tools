import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

LANGUAGE = 'es-ES'
FILENAME = 'video.mp4'
# Load the audio file
audio_file = AudioSegment.from_file(FILENAME, 'mp4')

# Split the audio file into chunks of silence
chunks = split_on_silence(audio_file, min_silence_len=1000, silence_thresh=-40)

# Initialize the recognizer
r = sr.Recognizer()

# Transcribe each chunk of audio
transcript = ''
for chunk in chunks:
    # Export the chunk to a WAV file
    chunk.export('chunk.wav', format='wav')

    # Open the WAV file and recognize the speech using the recognizer
    with sr.AudioFile('chunk.wav') as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language=LANGUAGE)
            transcript += ' ' + text
        except:
            pass

# Print the transcript
print(transcript)
