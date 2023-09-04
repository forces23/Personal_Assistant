import openai
import os

# !!! need to purchase a plan or wait for the free credits to renew !!!

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

prompt = "when was the last worlds fair and where was it held at?"

response = openai.Completion.create(
    engine = "text-davinci-003", # see what other engines there are
    prompt = prompt,
    max_token=50 # Sets the max # of tokens in the response
)

print(response)