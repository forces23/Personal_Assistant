import replicate
import os
from dotenv import load_dotenv
import time

load_dotenv()

try:
    api_key = os.getenv("REPLICATE_API_KEY")
    os.environ["Replicate_API_TOKEN"] = api_key
    key_pass = True
except Exception as e:
    print("API key is missing. Set the REPLICATE_API_KEY environment variable.")
    key_pass = False
    pass

def chat_with_LLama2(prompt):
    # prompt = "can you tell me the weather of columbia, MO?"
    endpoint = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
        # "https://api.replicate.io/v1/projects/meta/llama-2-70b-chat"
        # "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"

    print(f"You: {prompt}")

    output = replicate.run(
    endpoint,
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": prompt,
        "temperature": 0.5,
        "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
        "max_new_tokens": 500,
        "min_new_tokens": -1
    }
    )

    message_string = ""
    print(f"LLama 2: ")
    for message in output: 
        # print(message, end="", flush=True)
        message_string+=message

    print(message_string)   
    if key_pass:
        return message_string
    else:
        return "API key is missing. Set the REPLICATE_API_KEY environment variable."
