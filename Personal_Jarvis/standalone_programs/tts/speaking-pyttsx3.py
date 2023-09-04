import pyttsx3

engine = pyttsx3.init()

text = "hi how are you doing today?"

rate = engine.getProperty("rate")
print(rate)

engine.setProperty("rate", 100)

voices = engine.getProperty("voices")
print(voices)

engine.setProperty("voice", voices[0].id)

engine.say(text)

engine.runAndWait()
