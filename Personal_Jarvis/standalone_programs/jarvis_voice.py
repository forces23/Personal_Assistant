from google.cloud import texttospeech
import os

# Set the google cloud application acredtials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\google cloud stuff\jarvis-jenhvc-cdecde3fb66c.json"

# Initialize the TextToSpeechClient
client = texttospeech.TextToSpeechClient()

# Select a male voice (e.g., British English)
selected_voice = "en-GB-Neural2-B"  # Replace with the desired male voice name

# Define a text to be synthesized with SSML for pitch and speaking rate adjustments
text = """
<speak>
  <voice name="{}">
    <prosody rate="fast" pitch="normal">Sir, I must inform you that Thanos is indeed a formidable threat. His power and determination make him a force to be reckoned with. It is crucial that we prepare ourselves and gather all available resources to face this impending danger. Shall I assist you in formulating a plan to counter Thanos?</prosody>
  </voice>
</speak>
""".format(selected_voice)

# Synthesize speech
synthesis_input = texttospeech.SynthesisInput(ssml=text)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB",  # Language code for British English
    name=selected_voice,  # Male voice name you want to use
)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio to a file
with open("output.wav", "wb") as out:
    out.write(response.audio_content)
