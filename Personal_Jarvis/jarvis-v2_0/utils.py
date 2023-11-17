
import wave
import os
import pyaudio
from dotenv import load_dotenv
import speech_recognition as sr
import requests

load_dotenv()

OUTPUT_FILE_PATH = os.getenv("WAV_FILE_PATH")

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Function to save the audio to a wave file format 
def save_audio_to_file(p, frames):
   wf = wave.open(OUTPUT_FILE_PATH, "wb")
   wf.setnchannels(CHANNELS)
   wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
   wf.setframerate(RATE)
   wf.writeframes(b''.join(frames))
   wf.close()
   
   
# transcribes the data from the audio file into plain text  
def transcribe_data():
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(OUTPUT_FILE_PATH) as source:
        existing_audio_data = recognizer.record(source)

    try:
        print("Converting audio file into text ...")   
        text = recognizer.recognize_google(audio_data= existing_audio_data, language= "en-US", show_all=True)

    except sr.UnknownValueError:
        print(text)
        print("Could not understand audio file")

    if text == "":
        return ""
    else:
        return text          


def choose_speaker():
    speakers = {
    'awb': 0,     # Scottish male
    'bdl': 1138,  # US male
    'clb': 2271,  # US female
    'jmk': 3403,  # Canadian male, favorite
    'ksp': 4535,  # Indian male
    'rms': 5667,  # US male
    'slt': 6799   # US female
    }
    
    return speakers['slt']


def internet_connection():
    try: 
        response = response.get('www.google.com', timeout=5)
        return True
    except requests.ConnectionError as e:
        return False
    
    