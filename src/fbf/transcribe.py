import whisper


def transcribe_audio(audio_file_path: str) -> str:
    model = whisper.load_model("base.en", download_root="models/")
    result = model.transcribe(audio_file_path)
    return str(result["text"])
