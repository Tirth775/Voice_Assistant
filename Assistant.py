# Code for virtual assistant with GUI
import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import os
from tkinter import *
from PIL import ImageTk,Image
import datetime
import wikipedia
import webbrowser
import voice #Previous one file created by developer(me)
from mailbox import get_email_info #Previous one file created by developer(me)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voice_id)
print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()
def record_audio(ask = False):
#user voice record
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice : '+ voice_data)
            #compText = StringVar()
            userText = StringVar()
            userText.set('voice_data')
        except Exception:
            print('Oops something went Wrong')
            #lee_voice('Oops something went Wrong')
        return voice_data

def lee_voice(audio_string):
    #Play audio text to voice
    voice.speak(audio_string)
class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS GIVEN
    def __init__(self):
        root = Tk()
        root.title('Lena')
        root.geometry('350x220')
        img = ImageTk.PhotoImage(Image.open('1.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Virtual Assistant')
        userFrame = LabelFrame(root, text='Desktop', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        # compFrame = LabelFrame(root, text="Lena", font=('Railways',10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
        bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        voice.greet()
        root.mainloop()
    def clicked(self):
    #BUTTON CALLING
        print("working...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            lee_voice('My name is Lena. Your Desktop assistant ')
            print('My name is Lena. Your Desktop assistant ')
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            lee_voice('Here is what i found' + search)
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location' + location)
        if 'what is the time' in voice_data:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            lee_voice("Sir the time is :" + strTime)
        if 'mail' in voice_data:
            get_email_info()        
        if 'wikipedia' in voice_data:
            lee_voice("Searching Wikipedia.. ")
            query=voice_data.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            voice.speak("According to wikipedia")
            print(results)
            lee_voice(results)
        if 'open google' in voice_data:
            webbrowser.open("google.com")
        if 'open youtube' in voice_data:
            webbrowser.open("youtube.com")
        if 'play music' in voice_data:
            music_dir="D:\\Songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        if 'open google classroom' in voice_data:
            webbrowser.open("classroom.google.com")
        if 'exit' in voice_data:
            lee_voice("Thanks have a good day ")
            exit()

if __name__== '__main__':
    widget = Widget()
    
time.sleep(1)
while 1:
    voice_data = record_audio()
    #respond(voice_data)

speaker.runAndWait()