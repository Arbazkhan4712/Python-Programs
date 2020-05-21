# author @getsetcode
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import os
# author @getsetcode
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# author @getsetcode
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def get():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('say something!')
		audio = r.listen(source)
		print("done")
	try:
		text = r.recognize_google(audio)
		print('google think you said:\n' +text)
	except Exception as e:
		print(e) 
	remember = open('output.txt','w')
	remember.write(text)
	remember.close()
get()
# author @getsetcode