import JarvisListen
import os
import database

def startup():
    count = database.dbcheck()
    JarvisListen.speak("hello")
    
    if count == "None":
        JarvisListen.speak("Jarvis here for you ,, Sir ,i am your Personal assistance ,, Let set a perfect beginning for you, Kindly enter some of your personal details.")
        database.newstart()
        JarvisListen.speak("Your registration is complete now when ever you say hi hello or jarvis i will be available for u")
         
    else:
        JarvisListen.speak("Good Morning sir how may i help youu??")
        return
    return
      


   
