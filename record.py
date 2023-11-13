import sounddevice as sd
import wavio as wv
from datetime import datetime as dt
import config
import os

# Specify recording frequency and recording duration
freq = 44100
duration = 5

while True:
    timestamp = dt.now().strftime("%Y%m%d-%H%M%S")
    
    # Create the Recording directory if it doesn't exist
    if not os.path.exists(config.RECORDING_DIRECTORY):
        os.makedirs(config.RECORDING_DIRECTORY)
    
    # Start Recording
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()

    # The recording is saved as a NumPy array, so we'll write it to an audio file as is
    wv.write(f"./{config.RECORDING_DIRECTORY}/tmp-{timestamp}.wav", recording, freq, sampwidth=2)
    print(f"Recording saved as {timestamp}.wav")