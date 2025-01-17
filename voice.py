import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voice_id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def greet():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak('Good Morning')
	elif hour>=12 and hour<16:
		speak("Good Afternoon")
	else:
		speak("Good Evening!")

	speak("Python Assistnt here! Please tell me how may I help you?")

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_thresold=1
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print("Say that again please...")
		return "None"
	return query 
	


