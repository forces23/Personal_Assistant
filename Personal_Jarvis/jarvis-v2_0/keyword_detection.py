import pyaudio
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

KEYWORD = os.getenv('KEYWORD_1')

OUTPUT_FILE_PATH = os.getenv('WAV_FILE_PATH')

def keyword_detection():
    keyword_found = False
    p = pyaudio.PyAudio()
    
    stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)
   
    print("Listening for keyword ...")
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        kw_audio = recognizer.listen(source, phrase_time_limit=None)
        
        try:
            recognized_text = recognizer.recognize_google(kw_audio).lower()
            print(f"Recognized: {recognized_text}")
            if KEYWORD in recognized_text:
                keyword_found = True
            else:
                keyword_found = False
            
        except sr.UnknownValueError:
            print("No Audible Audio Detected - kw.")
            keyword_found = False
        except sr.RequestError as e:
            print(f"Error requesting results from Google Speech Recognition service - kw - , {e}")
            keyword_found = False
    
        if keyword_found :
            print("Keyword Detected!")
            try:
                q_audio = recognizer.listen(source, phrase_time_limit=None)
                recognized_question = recognizer.recognize_google(q_audio).lower()
                print(f"Recognized Question: {recognized_question}")
            except sr.UnknownValueError as e:
                print(f"No Audible Audio Detected - q , {e}")
            except sr.RequestError as e:
                print(f"Error requesting results from Google Speech Recognition service - q - , {e}")                
            
            stream.stop_stream()
            stream.close()
            p.terminate()
            
        else:
            recognized_question = None
        
        
    return keyword_found, recognized_question



    

    