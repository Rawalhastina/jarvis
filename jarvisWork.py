import JarvisListen
import jarvisopen
import userdata
import userdata
import grehelp

if __name__ == "__main__":

    userdata.startup()
    
    
    while True:
       
        
        
        query = JarvisListen.takeCommand().lower().strip()
        
        # Logic for executing tasks based on query
        


        if 'open' in query:
            jarvisopen.search_web(query) 

        elif 'search' in query:
            jarvisopen.search_content(query)
            
        
        elif 'music' in query or 'song' in query:
                jarvisopen.playmusic(query)
        
        elif 'email' in query:
            jarvisopen.sendEmail(query)
  
        elif 'learngre' in query:
            grehelp.wordlist()
  