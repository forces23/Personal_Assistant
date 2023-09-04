''' 
    The Brains of JARVIS is powerd by Google Bard
    this can be changed to any AI with a API
'''

import os
from dotenv import load_dotenv
from bardapi import Bard

load_dotenv()

API_KEY = os.getenv("BARD_API_KEY")

bard = Bard(token = API_KEY)

def brain_power(query):
    result = bard.get_answer(query)
    
    return result
    
    