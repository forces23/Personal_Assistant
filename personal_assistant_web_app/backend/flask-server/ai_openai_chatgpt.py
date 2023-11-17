from openai import OpenAI, AsyncOpenAI
from google.cloud import texttospeech
import os
import pygame
from dotenv import load_dotenv

# Errors to handle in the future
# openai.error.ServiceUnavailableError

# Set the google cloud application acredtials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\google cloud stuff\jarvis-jenhvc-cdecde3fb66c.json"

load_dotenv()

# Set your OpenAI API key
API_KEY = os.getenv("ChatGPT_API_KEY")
client = OpenAI(
    api_key = API_KEY
)

ai_response_path = "backend\\flask-server\\output_wav_files\\ai_response.wav"

def chat_with_bot(user_input):
    # print("Hello! I'm your AI chatbot. You can start chatting. Type 'exit' to quit.")
    
    # while True:
        # user_input = input("You: ")
        
    # if user_input.lower() == 'exit':
    #     print("Chatbot: Goodbye!")
    #     break
    
    ai_response = generate_response(user_input)
    # print("Chatbot:", ai_response.choices[0].message.content)

    # Convert the text response to speecan you ch
    # text_to_speech(ai_response.choices[0].message.content)

    # Play the audio file that was created 
    # play_audio()

    return ai_response.choices[0].message.content
    

def generate_response(user_input):
    response = client.chat.completions.create(
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
        # max_tokens=150
    )
    return response

def text_to_speech(response):
    # Initialize the TextToSpeechClient
    client_tts = texttospeech.TextToSpeechClient()

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

    response = client_tts.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio to a file
    with open(ai_response_path, "wb") as out:
        out.write(response.audio_content)

def play_audio():
    # Initialize pygame
    pygame.init()

    # Load the sound file 
    sound = pygame.mixer.Sound(ai_response_path)

    # play the sound
    sound.play()

    # waits for sound playback to finish
    pygame.time.delay(int(sound.get_length() * 1000))

    # Quit pygame (might not need till program is finished )
    pygame.quit()


    


# def main():
#     # Start the chat with the chatbot
#     chat_with_bot()

# if __name__ == '__main__':
#     main()