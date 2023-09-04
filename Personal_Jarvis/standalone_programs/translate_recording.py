import pyaudio
import speech_recognition as sr
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice_test.wav"

def record_audio():
    
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)

    print("**** RECORDING IN PROGRESS ****")

    frames=[]

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        frames.append(audio_data) # Appends all streams into a list
        
    print("*** DONE RECORDING ***")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def translate_data():
    r = sr.Recognizer()
    with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
        existing_audio_data = r.record(source)
        
    try: 
        print("Trying to convert ...")
        text = r.recognize_google(audio_data = existing_audio_data, language = 'en-US', show_all=True) # show_all=True, shows all the data
        print(text)
        
    except sr.UnknownValueError:
        print(text)
        print("Could not Understand")
    
    if text == "":
        return ""
    else:
        return text


def main():
    while True:
        record_audio()
        data = translate_data()
        if data != []:
            transcript = data['alternative'][0]['transcript']
        else:
            transcript = "NA"
        
        print(transcript)
    
if __name__ == "__main__":
    main()