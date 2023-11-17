import openai
from google.cloud import texttospeech
import os
import pygame

# Errors to handle in the future
# openai.error.ServiceUnavailableError

# Set the google cloud application acredtials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\google cloud stuff\jarvis-jenhvc-cdecde3fb66c.json"

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

def chat_with_bot():
    print("Hello! I'm your AI chatbot. You can start chatting. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = generate_response(user_input)
        print("Chatbot:", response['choices'][0]['message']['content'])

        # Convert the text response to speecan you ch
        text_to_speech(response['choices'][0]['message']['content'])

        # Play the audio file that was created 
        play_audio()

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" model.
        messages=[
            {"role": "system", "content": "You are Jarvis, a highly intelligent AI assistant, just like in the Marvel movies. "
                                          "You have been assigned to assist the user and address them in a manner similar to how you address Tony Stark."
                                          "The user is MALE."
                                          "Refer to the user as only boss or sir."
                                          "Do not use sir and boss in the same sentence."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2, # Can only set it in the range of 0.2 - 1. the lower the number the more straight forward the anwser is the higher the number the more creative the anwser is. also lower = less time to generate response
        max_tokens=150
    )
    return response

def text_to_speech(response):
    # Initialize the TextToSpeechClient
    client = texttospeech.TextToSpeechClient()

    # Select a voice (e.g., British English)
    selected_voice = "en-GB-Neural2-B"  

    # Define a text to be synthesized with SSML for pitch and speaking rate adjustments
    text = f"""
    <speak>
    <voice name="{selected_voice}">
        <prosody rate="fast" pitch="normal">{response}</prosody>
    </voice>
    </speak>
    """

    # Synthesize speech
    synthesis_input = texttospeech.SynthesisInput(ssml=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-GB",  # Language code for British English
        name=selected_voice,  # Voice name you want to use
    )

    audio_config = texttospeech.AudioConfig(pitch=3.6, speaking_rate=1.2, audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio to a file
    with open(f"ai_response.wav", "wb") as out:
        out.write(response.audio_content)

def play_audio():
    # Initialize pygame
    pygame.init()

    # Load the sound file 
    sound = pygame.mixer.Sound("ai_response.wav")

    # play the sound
    sound.play()

    # waits for sound playback to finish
    pygame.time.delay(int(sound.get_length() * 1000))

    # Quit pygame (might not need till program is finished )
    pygame.quit()


    


def main():
    # Start the chat with the chatbot
    chat_with_bot()

if __name__ == '__main__':
    main()