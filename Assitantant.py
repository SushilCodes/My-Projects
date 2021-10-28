import pyttsx3
import datetime

import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning:")

    elif  hour>=12 and hour<=17:
        speak("Good afternoon:")
    else:
        speak("Good evening:")
    speak("I am assist 1 point o ,How may i help you")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')

        print("user said=",query)
    except Exception as e:
        #print(e)
        print("Say something please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sushiljadhav0604@gmail.com','9359256767')
    server.sendmail('sushiljadhav0604@gmail.com',to,content)
    server.close()



if __name__=="__main__":
    speak("Welcome")
    wishme()
    #while True:
    if 1:
        query=  takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            resultss = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(resultss)
            speak(resultss)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'play music' in query:
            music_dir='D:\Songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"OK,The time is {strTime}")

        elif 'open vs' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("What should i say ")
                content = takecommand()
                to="sushiljadhav0604@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfuly:")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send email:")

        elif 'weather' in query:
            try:
                search="weather in pune"
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,'html.parser')
                temp=data.find("div",class_="BNeawe").text
                speak(f"current {search}" is {temp})
            except Exception as e:
                print(e)
                speak("Sorry i cant get you,Please say it again:")



