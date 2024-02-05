import whisper

def transcribe_audio(audio_path):
    """
    Transcribe speech from an audio file to text using OpenAI's Whisper model.

    Parameters:
    - audio_path: Path to the audio file to transcribe.

    Returns:
    - The transcribed text.
    """
    # Load the model
    model = whisper.load_model("base")  # You can choose different model sizes depending on your needs

    # Load and transcribe the audio file
    result = model.transcribe(audio_path)

    # Extract the text from the result
    text = result["text"]

    print("Transcribed Text:", text)
    return text

# Example usage
audio_file_path = "./data/parkinson/B1AGNUTGOL52F100220171041.wav"
transcribe_audio(audio_file_path)
