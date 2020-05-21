import pyttsx3
import os
# author @getsetcode
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
remember = open('input.txt','r')
# author @getsetcode
speak(remember.read())
# author @getsetcode
