import whisper
import os

BASE_MODEL = "base"
AUDIO_EXTENSION = '.wav'
TRANSCRIPTION_LANGUAGE = 'it'
RESULT_DIR = 'data'

def load_whisper_model(model=BASE_MODEL):
    """
    Load OpenAI's Whisper model.
    Parameters:
    - model: The model size. Default is "base".
    Returns:
    - The whisper model.
    """
    return whisper.load_model(model)

def extract_filename(audio_path):
    return os.path.basename(audio_path)


def transcribe_audio_using_model(audio_path, model=BASE_MODEL):
    """
    Transcribe speech from an audio file to text using OpenAI's Whisper model.
    Parameters:
    - audio_path: Path to the audio file to transcribe.
    - model: model to be used for transcription. Default is "base".
    Returns:
    - The transcribed text.
    """
    whisper_model = load_whisper_model(model)
    result = whisper_model.transcribe(audio_path, language=TRANSCRIPTION_LANGUAGE)
    filename = extract_filename(audio_path)
    return filename, result["text"]

def write_transcription_to_file(result_filename, transcribed_filename,  transcription):
    with open(result_filename, 'a') as output_file:
        output_file.write(f'{transcribed_filename}: {transcription}\n')

import os


def transcribe_all_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(AUDIO_EXTENSION):
                full_file_path = os.path.join(root, file)
                filename, transcription = transcribe_audio_using_model(full_file_path, "large")
                # derive the result filename from the current directory
                result_filename = os.path.join(RESULT_DIR, os.path.basename(root) + '_result.txt')
                write_transcription_to_file(result_filename, filename, transcription)


# Example usage
transcribe_all_files_in_directory("Italian_Parkinsons_Voice_and_Speech")
