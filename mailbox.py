import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import voice #Previous one file created by developer(me)

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voice_id)

def talk(text):
    voice.speak(text)
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('turthptl@gmail.com', 'ddit1234')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'tony': 'dhwanijmistry298@gmail.com',
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    #talk(name+' Is this correct one?')
    #if get_info()=='no':
     #   get_email_info
    if name in email_list:
        receiver = email_list[name]
        print(receiver)        
    else:
        talk('This name havent been saved')
        talk('Enter email address for that')
        receiver=input('Enter email address for that: ')
        talk('alright! i saved it for upcoming mails')
        email_list[name]=receiver
        print(receiver)
        print(email_list)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email has been successfully sent')
    talk('Do you want to send more email?')
    send_more ='no' #get_info()
    if 'yes' in send_more:
        get_email_info()