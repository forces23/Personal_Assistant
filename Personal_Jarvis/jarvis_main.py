import ascii_art
import keyword_detection as kd
import brains
import speaking
import utils
import pygame

def main():
    ascii_art.main_header1()
    while(True):
        # this check doesnt really work since it checks line 3 for brains import first. 
        # if theres no internet it cannot connect to the bard site which throws a conncetion error. (Check Notes)
        if utils.internet_connection:
            try:
                keyword_found, text = kd.keyword_detection()
            except UnboundLocalError as e:
                print(f'Question was empty - q, {e}')
                keyword_found = False
            if keyword_found:
                # print("\n\n")
                
                answer_all_data = brains.brain_power(text)
                answer = answer_all_data['content']
                print(f'anwser = {answer}')
                
                speaker = utils.choose_speaker()
                print(f'speaker = {speaker}')
                try:
                    print('saving text to speech ...')
                    speaking.save_text_to_speech(answer, speaker)
                    output_saved = True
                    print('done saving')
                except UnboundLocalError as e:
                    # logger.debug(f'{e}')
                    output_saved = False
                    print(f'\n{e}')
                
                print('getting ready to speak...')
                pygame.init()
                pygame.mixer.init()
                if output_saved == True:
                    print('loading..')
                    pygame.mixer.music.load("output_wav_files/answer.mp3")
                    print('speaking now...')
                    pygame.mixer.music.play()
                    print('done speaking')
                else:
                    pygame.mixer.music.load("output_wav_files\Bender-08.wav")
                    pygame.mixer.music.play()
        else:
            # logger.debug('internet is not connected')
            print('internet is not connected, Check connection.')
            
            
            
            
    
if __name__ == "__main__":
    main()