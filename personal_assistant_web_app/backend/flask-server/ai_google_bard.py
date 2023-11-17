import os 
import sys
from dotenv import load_dotenv
from bardapi import Bard
import traceback
import requests
# import browser_cookie3

# https://github.com/dsdanielpark/Bard-API

load_dotenv()

API_KEY = os.getenv("BARD_API_KEY")

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", API_KEY) 

try:
    bard = Bard(token = API_KEY, session=session, timeout=30)
except Exception as e:
    print(f"there was an error trying to connect to Bard API: {str(e)}")
    traceback.print_exc()

def chat_with_bot(query):
    result = bard.get_answer(query)    
    print(result,"\n\n")

    ai_response = result["content"]
    # ai_response = "I need more information on what you want to repeat and in what context.\n\nHere are a few examples of what I could repeat:\n\n- I can repeat what you have said back to you.\n- I can repeat a sentence you have said in a different way.\n- I can repeat a pattern of behavior.\n- I can repeat a sequence of events.\n- I can repeat a piece of information.\n\nPlease let me know if any of these examples are what you are looking for. If not, please provide more details and I will try to fulfill your request.\n"
    parsed_ai_response = ai_response.replace("\n", "<br>")

    return ai_response


    

        
        
        