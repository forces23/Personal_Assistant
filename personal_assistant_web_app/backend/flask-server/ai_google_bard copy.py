import os 
import sys
from dotenv import load_dotenv
from bardapi import Bard
import traceback
import requests
# import browser_cookie3

load_dotenv()

API_KEY = os.getenv("BARD_API_KEY")

url = "https://bard.google.com/"

# cj = browser_cookie3.firefox()
# r = requests.get(url, cookies=cj)
# print(cj)

"""
    The proxy url forwards your connection requests to a randomly rotating IP address in a pool of proxies before reaching the target website. 
    https://crawlbase.com/docs/smart-proxy/?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api
    couldnt get rotating proxy to work 
"""
crawlbase_key = os.getenv("CRAWLBASE_KEY")
proxy_url = f"http://{crawlbase_key}:@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

print(f"proxies: {proxies}")

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
    # pass
    bard = Bard(token = API_KEY, proxies=proxies, verify=False, session=session, timeout=30, conversation_id="ai conversation")
    # bard = Bard(token = API_KEY, session=session, timeout=30)
    # bard = Bard(token_from_browser=True)
except Exception as e:
    print(f"there was an error trying to connect to Bard API: {str(e)}")
    traceback.print_exc()

def chat_with_bot(query):
    # result = bard.get_answer(query)    
    # print(result,"\n\n")

    # ai_response = result["content"]
    ai_response = "I need more information on what you want to repeat and in what context.\n\nHere are a few examples of what I could repeat:\n\n- I can repeat what you have said back to you.\n- I can repeat a sentence you have said in a different way.\n- I can repeat a pattern of behavior.\n- I can repeat a sequence of events.\n- I can repeat a piece of information.\n\nPlease let me know if any of these examples are what you are looking for. If not, please provide more details and I will try to fulfill your request.\n"
    parsed_ai_response = ai_response.replace("\n", "<br>")

    return ai_response


    

        
        
        