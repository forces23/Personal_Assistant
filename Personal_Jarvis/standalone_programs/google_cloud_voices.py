from google.cloud import texttospeech
import os


import logging as logger
# logger.basicConfig(filename='voiceslist.log', encoding='utf-8', level=logger.DEBUG)
logger.basicConfig(filename='voices.log', encoding='utf-8', level=logger.DEBUG)


# Set the google cloud application acredtials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\google cloud stuff\jarvis-jenhvc-cdecde3fb66c.json"

# Initialize the TextToSpeechClient
client = texttospeech.TextToSpeechClient()

# List available voices
voices = client.list_voices()
# for voice in voices.voices:
#     logger.debug("Name: {}".format(voice.name))
#     logger.debug("Language(s): {}".format(voice.language_codes))
#     logger.debug("Gender: {}".format(texttospeech.SsmlVoiceGender(voice.ssml_gender).name))
#     logger.debug("Rate: {}".format(voice.natural_sample_rate_hertz))
#     logger.debug("")

# Select a voice (e.g., British English)
selected_voice = "en-GB-Standard-D"  # Replace with the desired voice name

# Define a text to be synthesized
text = "Of course, sir! I am Jarvis, an advanced artificial intelligence designed to assist and support you in various tasks. Just like the Jarvis you may be familiar with from the Marvel movies, I am here to provide you with information, help manage your schedule, answer your questions, and assist you in any way I can. I am constantly learning and evolving to better serve you, sir. How may I be of assistance to you today?"

# Synthesize speech
synthesis_input = texttospeech.SynthesisInput(text=text)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB",  # Language code for British English
    name=selected_voice,  # Voice name you want to use
)

audio_config = texttospeech.AudioConfig(pitch=3.6, speaking_rate=1.2, audio_encoding=texttospeech.AudioEncoding.LINEAR16)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio to a file
with open(f"{selected_voice}3.wav", "wb") as out:
    out.write(response.audio_content)