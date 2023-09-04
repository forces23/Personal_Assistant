from tkinter import *
from gtts import gTTS
from playsound import playsound
from io import BytesIO
import pygame
import time

root = Tk()
root.geometry("350x300")
root.configure(bg="ghost white")
root.title("DataFlair -TEXT TO SPEECH")

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)


def Text_to_speech():
    Message = entry_field.get()
    mp3_fo = BytesIO()
    speech = gTTS(Message)
    speech.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(mp3_fo)
        sound.play()
        # pygame.mixer.music.load(speech, 'mp3')
        # pygame.mixer.music.play()
        time.sleep(3)
    except AssertionError:
        print("There was no text in the text box to translate")
    except Exception as e:    
        print(f"Error playing audio, {e}")
        
def Exit():
    Msg.set("")
    
def Reset():
    Msg.set("")
    
Button(root, text = "PLAY", font = 'arial 15 bold', width = '4', command = Text_to_speech).place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()

