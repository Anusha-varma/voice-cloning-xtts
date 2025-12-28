from TTS.api import TTS
import torch

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using device:", device)

    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        progress_bar=True
    ).to(device)

    text = "I am always with you. You are not alone."

    tts.tts_to_file(
        text=text,
        speaker_wav="voice.wav",
        language="en",
        file_path="output.wav"
    )

    print("Voice cloning complete. Saved as output.wav")

if __name__ == "__main__":
    main()
