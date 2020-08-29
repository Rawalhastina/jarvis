import JarvisListen
import webbrowser
import requests
import smtplib #for email
import bs4
from bs4 import BeautifulSoup
from googlesearch import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def search_web(input): 
  


    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'youtube' in input.lower(): 
  
        JarvisListen.speak("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
  
    elif 'wikipedia' in input.lower(): 
  
        JarvisListen.speak("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
  
    elif 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
    elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:]
            JarvisListen.speak("searching") 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
   
    else: 
  
        driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
  
    return

def search_content(query):
    search = requests.get("https://www.google.com/search?q="+query)
    webbrowser.open("https://www.google.com/search?q="+query)
        

def playmusic(query) :
    for url in search(query, stop = 2):
        webbrowser.open(url)

def sendEmail(query):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hslovely1999@gmail.com', 'nayan@123')
    server.sendmail('hslovely1999@gmail.com', 'nayanmogra@gmail.com', "hello ")
    server.close()

