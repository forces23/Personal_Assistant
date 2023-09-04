import ascii_art
import keyword_detection as kd
import brains

def main():
    ascii_art.main_header1()
    while(True):
        keyword_found = kd.keyword_detection()
        if keyword_found:
            data = kd.transcribe_data()
            if data != []:
                transcript = data['alternative'][0]['transcript']
            else:
                transcript = "N/A"
                
            print(transcript,"\n\n")
            
            answer = brains.brain_power(transcript)
            
            print(answer['content'])
            
            
            
    
if __name__ == "__main__":
    main()