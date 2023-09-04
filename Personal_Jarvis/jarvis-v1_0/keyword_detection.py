import pyaudio
import wave
import speech_recognition as sr
from dotenv import load_dotenv
import os

load_dotenv()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

microphone = sr.Microphone(chunk_size=CHUNK)
recognizer = sr.Recognizer()

KEYWORD = os.getenv("KEYWORD")

OUTPUT_FILE_PATH = os.getenv("WAV_FILE_PATH")

p = pyaudio.PyAudio()
    
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

def keyword_detection():
    keyword_found = False
   
    print("Listening for keyword ...")
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)
        
        try:
            recognized_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {recognized_text}")
            if KEYWORD in recognized_text:
                keyword_found = True
            else:
                keyword_found = False
            
        except sr.UnknownValueError:
            print("No Audible Audio Detected.")
        except sr.RequestError as e:
            print(f"Error requesting results from Google Speech Recognition service , {e}")
    
    if keyword_found :
        print("Keyword Detected!")
        print("Recording in progress ...")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            audio_data = stream.read(CHUNK)
            frames.append(audio_data)
        
        print("Recording Finished!")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        save_audio_to_file(p, frames)

    return keyword_found

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
    

    