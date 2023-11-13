import whisper
import os, glob
import config
import time

# Change this to Medium in production
model = whisper.load_model("base")

transcribed = []

# Service Loop
while True:
    files = sorted(glob.iglob(os.path.join(config.RECORDING_DIRECTORY, '*')), key=os.path.getctime, reverse=True)
    if len(files) < 1:
        continue

    latest_recording = files[0]
    latest_recording_filename = latest_recording.split('/')[0]

    if os.path.exists(latest_recording) and not latest_recording in transcribed:
        audio = whisper.load_audio(latest_recording)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(language='en', fp16=False)

        result = whisper.decode(model, mel, options)

        if result.no_speech_prob < 0.6:
            print(result.text)

            # We'll append the text to a transcript file for testing
            # REMOVE IN PRODUCTION

            if not os.path.exists(config.TRANSCRIPT_DIRECTORY):
                os.makedirs(config.TRANSCRIPT_DIRECTORY)

            # Create a new transcript file using the current time
            filename_base = "transcript_" + str(int(time.time()))
            filename = filename_base + ".txt"

            with open(os.path.join(config.TRANSCRIPT_DIRECTORY, filename), "w") as f:
                f.write(result.text)

            with open(os.path.join(config.SERVICE_DIRECTORY, "transcript.txt"), "w") as f:
                f.write(result.text)

            transcribed.append(latest_recording)

            print("Transcription Complete")
            exit(1)