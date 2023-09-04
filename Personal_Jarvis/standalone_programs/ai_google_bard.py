import os 
import sys
from dotenv import load_dotenv
from bardapi import Bard

load_dotenv()

API_KEY = os.getenv("BARD_API_KEY")

bard = Bard(token = API_KEY)


def main():
    while(True):
        query = input("Enter a query: ")
        print("")
        if query == "Q":
            print("terminating Program ...")
            sys.exit(0)
        else:
            result = bard.get_answer(query)
            # print(result)
            
            print(result["content"],"\n\n\n")
    
    
if __name__ == "__main__":
    main()
        
        
        