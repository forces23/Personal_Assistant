import speech_recognition as sr
import pyaudio
import wave


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
KEYWORD = "hey jarvis"
OUTPUT_FILE = "output_wav_files/trigger_word_test.wav"

# Saves the audio into a .wav file
def save_audio_to_file(pyaudio,frames):
    wf =  wave.open(OUTPUT_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close() 

# Listens for the keyword that is set by the variable KEYWORD
def keyword_detection(microphone, recognizer):    
    with microphone as source:
        
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=3)
        try:
            recognized_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {recognized_text}")
            if KEYWORD in recognized_text:
                return True
            else: 
                return False
        
        except sr.UnknownValueError:
            print("No Audio Detected")
            return False
        except sr.RequestError as e:
            print(f"Error requesting results from Google Speech Recognition Service; {e}")
            return False


def listening(microphone, recognizer):
    keyword_found = False
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)

    print("Listening for Keyword .... ")
    
    if keyword_detection(microphone, recognizer):
        keyword_found = True
        print("Keyword Detected! Recording ....")
        frames = []
        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            audio_data = stream.read(CHUNK)
            frames.append(audio_data)
        
        print("Recoring Finished!")
    
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        save_audio_to_file(p,frames)

    return keyword_found



def translate_data(recognizer):
    with sr.AudioFile(OUTPUT_FILE) as source:
        existing_audio_data = recognizer.record(source)
        
    try: 
        print("Trying to convert ...")
        text = recognizer.recognize_google(audio_data = existing_audio_data, language = 'en-US', show_all=True) # show_all=True, shows all the data
        # print(text)
        
    except sr.UnknownValueError:
        print(text)
        print("Could not Understand")
    
    if text == "":
        return ""
    else:
        return text
    
def main():
    microphone = sr.Microphone(chunk_size=CHUNK)
    recognizer = sr.Recognizer()
    while True:
        keyword_found = listening(microphone, recognizer)
        if keyword_found:
            # save_audio_to_file(frames)
            data = translate_data(recognizer)
            
            if data != []:
                transcript = data['alternative'][0]['transcript']
            else:
                transcript = "NA"
            
            print(transcript)
    
    
if __name__ == "__main__":
    main()