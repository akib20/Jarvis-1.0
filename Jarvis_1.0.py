# from ast import main
# from email.mime import audio
from ast import main
from cgitb import reset, text
from http import server
from math import remainder
from msilib.schema import Directory
from pydoc import cli
from unicodedata import name
from unittest.mock import seal
from urllib.parse import SplitResult
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import psutil # pip install psutil
import pyjokes # pip install pyjokes
import os
import pyautogui # pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha # pip install wolframalpha
import time


engine = pyttsx3.init()
wolframalpha_app_id = 'VLLG45-P5882W62YL'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    # Time = datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("The current time is")
    speak(Time)

def date_():
    year =  datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir!")
    time_()
    date_()

    # Greetings

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    
    speak("Jarvis is at your service. Please tell me how can I help you today? ")
    
def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #for this function, you must enable low security in your gmail which you are going to use as sender

    server.login('youremail@gmail.com','yourpassword')
    server.sendmail('youremail@gmail.com',to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    # battery = psutil.sensors_battery()
    # speak('Battary is at')
    # speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Iftakher/Desktop/JARVIS 1.0/screenshot.png')

if __name__ == '__main__':
    
    wishme()

    while True:
        query = TakeCommand().lower()

        # All commands will be stored in the lower case in query
        # for easy recognition

        if 'time' in query:
            time_()
        
        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 3)
            speak('According to wikipedia')
            print(reset)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                # provide reciever email address
                speak("Who is the receiver?")
                receiver = input("Enter Receiver's Email : ")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent')

            except Exception as e:
                print(e)
                speak('Unable to send Email.')


        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # chromepath is location of chrome's installation on computer

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') # only open website with '.com at end.
        
        elif 'search youtube' in query:
            speak("What should I search?")
            search_term =  TakeCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open("https://www.youtube.com/results?search_query="+search_term)
        
        elif 'search google' in query:
            speak("What should I search?")
            search_term = TakeCommand().lower()
            speak("Searching")
            wb.open('https://www.google.com/search?q='+search_term)

        elif 'cpu' in query:
            cpu()
        
        elif "joke" in query:
            joke()

        elif 'go offline' in query:
            speak("Going Offline Sir!")
            quit()

        elif 'word' in query:
            speak("Opening MS Word.....")
            ms_word = r'D:/Office/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I write, Sir?")
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak('Sir should I include Date and Time')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                StrTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(StrTime)
                file.write(':-')
                file.write(notes)
                speak("Done Talking Notes, Sir!")
            else:
                file.write(notes)

        elif 'show note' in query:
            speak('Showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        # elif 'play music' in query:
        #     song_dir = 'C:/Users/Iftakher/Desktop/JARVIS 1.0/Song'
        #     music = os.listdir(song_dir)
        #     speak("What should I play?")
        #     speak('select a number...')
        #     ans = TakeCommand().lower()
        #     if 'number' in ans:
        #         no = int(ans.replace('number',''))
        #     elif 'random' or 'you choose' in ans:
        #         no = random.randint(1, 100)

        #     os.startfile(os.path.join(song_dir, music[no]))


        elif 'play music' in query:
    
            video ='C:/Users/Iftakher/Desktop/JARVIS 1.0/Song'

            audio = 'C:/Users/Iftakher/Desktop/JARVIS 1.0/Audio'

            speak("What songs should i play? Audio or Video")

            ans = (TakeCommand().lower())

            while(ans != 'audio' and ans != 'video'):

                speak("I could not understand you. Please Try again.")

                ans = (TakeCommand().lower())

       

            if 'audio' in ans:

                    songs_dir = audio

                    songs = os.listdir(songs_dir)

                    print(songs)

            elif 'video' in ans:

                    songs_dir = video

                    songs = os.listdir(songs_dir)

                    print(songs)

               

            speak("select a random number")

            rand = (TakeCommand().lower())

            while('number' not in rand and rand != 'random'):

                speak("I could not understand you. Please Try again.")

                rand = (TakeCommand().lower())

                if 'number' in rand:

                    rand = int(rand.replace("number ",""))

                    os.startfile(os.path.join(songs_dir,songs[rand]))

                    continue            

                elif 'random' in rand:

                    rand = random.randint(1,219)

                    os.startfile(os.path.join(songs_dir,songs[rand]))

                    continue

        elif 'remember that' in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember= open('memory.txt', 'r')
            speak('You asked me to remember that'+ remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4398f41ab82c41b28ea8aebf0a1ddf4d')
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headlines from the business world')
                print("===========TOP HEADLINES==============="+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
  

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is "+answer)
            speak("The answer is "+answer)

        elif 'what is' in query or 'who is' in query:
            # Same wolframalpha API as before
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No Results")

        elif 'stop listening' in query:
            speak("For how many second you want me to stop listening to your commands?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        