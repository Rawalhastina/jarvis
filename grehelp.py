import JarvisListen as jl

word = []
meaning = []
wordnumber=["first" , "second" , "third" ," fourth"," fifth"," sixth"," seventh" ," eighth "," ninth ", " tenth "]
def wordlist():
    jl.speak("Welcome to learning new words for gre")
    jl.speak("First tell me the word u wanna learn ")
    jl.speak("Then tell me what is the meaning of the word")
    jl.speak("I will repeat the word for u 4 times then i will ask u word 2 times")
    jl.speak("we will do this for 10 words then i will randomly ask u all 10 words")
    jl.speak("so lets start")
    takeword()
    jl.speak("entery of word is done now its time to listen them ")
    speakagain()

def takeword():
    i=0
    while (i <= 1):
        jl.speak("tell me " + wordnumber[i] + "word")
        qry = jl.takeCommand()
        word.append(qry)
        jl.speak("tell me  meaning of" + word[i])
        qry = jl.takeCommand()
        meaning.append(qry)
        print(word[i])
        print(meaning[i])
        i = i + 1
    return

    

def speakagain():
    i = 0
    while(i <= 1):
        j = 0
        while(j < 4) :
            jl.speak(wordnumber[i] + "word is   ")
            jl.speak(word[i])
            jl.speak("    meanig of the word is ")
            jl.speak(meaning[i])
            j = j+1
        askword(word[i] ,meaning[i] )
        i = i+1
def askword(word1 , meaning1):
    jl.speak("Tell me the word you listend")
    w = jl.takeCommand()
    if w == word1 :
        jl.speak("Good         ,   Tell me ,   the meaning of the word")
        m = jl.takeCommand()
        if m == meaning1 :
            jl.speak("Good        ,    lets        , learn other word")
        else :
            jl.speak("No the meaning of " + word1 + " is " + meaning1)
            jl.speak("try again")
            askword(word1 , meaning1)
    else : 
        jl.speak("No the word is " + word1)
        jl.speak("try again")
        askword(word1 , meaning1)

