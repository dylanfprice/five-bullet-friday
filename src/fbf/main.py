import argparse
import os
from pathlib import Path

from src.fbf.summarize import summarize_text
from src.fbf.transcribe import transcribe_audio

AUDIO_FILE_TYPES = (".mp3", ".mp4", "m4a", ".wav", ".ogg")


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe and summarize audio files in the style of five-bullet friday."
    )
    parser.add_argument("audio_folder", help="Path to a folder containing audio files")
    parser.add_argument(
        "transcript_folder", help="Path to a folder to write transcripts to"
    )
    args = parser.parse_args()
    print(transcribe_and_summarize(args.audio_folder, args.transcript_folder))


def transcribe_and_summarize(audio_folder: str, transcript_folder: str) -> str:
    """
    Transcribe untranscribed audio files in the `audio_folder` and write the
    transcripts to the `transcript_folder`. Then, return a summary of *all*
    transcripts in the `transcript_folder`.
    """
    audio_files = [
        name for name in os.listdir(audio_folder) if name.endswith(AUDIO_FILE_TYPES)
    ]
    audio_files_to_transcribe = [
        name
        for name in audio_files
        if not os.path.exists(os.path.join(transcript_folder, f"{Path(name).stem}.txt"))
    ]

    for name in audio_files_to_transcribe:
        transcription = transcribe_audio(os.path.join(audio_folder, name))
        transcript_path = os.path.join(transcript_folder, f"{Path(name).stem}.txt")
        with open(transcript_path, "w") as f:
            f.write(transcription)

    transcript_paths = [
        os.path.join(transcript_folder, name)
        for name in os.listdir(transcript_folder)
        if name.endswith(".txt")
    ]
    transcripts = [_read_file(path) for path in transcript_paths]
    concatenated_transcripts = "\n".join(transcripts)
    return summarize_text(concatenated_transcripts)


def _read_file(path):
    with open(path, "r") as f:
        return f.read()
