import pyttsx3
import speech_recognition as sr
import os
import smtplib
import tempfile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    query = takeinput()
    query = query.replace(" ","")
    ans = ask(query)
    if ans == "yes" :
        return query
    elif ans == "no":
        takeinput()
    else :
        ask(query)
    return query
def takeinput():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.dynamic_energy_threshold = 1000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        print(e)
        speak("Say that again please...")
        query = takeinput()
    return query

def start():
    welcome = ['hi','hello','jarvis']
    for x in range(len(welcome)):
        while takeCommand() in  welcome[x]:
            speak(welcome[x])
            break
        break
    return

def ask(qu):
    speak(qu)
    speak(",,,did i heard correct   ,  yes or no")
    ans = takeinput()
    return ans
    
