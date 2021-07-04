#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3


# In[ ]:


import os
import time
import subprocess
import json


# In[ ]:


print('LOADING YOUR AI PERSONAL ASSISTANT JARVIS')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


# In[ ]:


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[ ]:


def WishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('hello, good morning Deepak')
        print('hello,good morning Deepak')
    elif hour>=12 and hour<=18:
        speak('hello,good afternoon Deepak')
        print('hello,good afternoon Deepak')
    else:
        speak('its already late better go to bed')
        print('its already late better go to bed')

        
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LISTENING")
        audio=r.listen(source)
    try:
        statement=r.recognize_google(audio,language='en-in')
        print(f'user said:{statement}\n')
    except Exception as e:
        speak('pardon me,please say that again')
        return "none"
    return statement


# In[ ]:


speak('LOADING YOUR PERSONAL AI ASSISTANT JARVIS')
WishMe()

if __name__=='__main__':
    while True:
        speak("How can i help you?")
        statement=takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak("Your personal AI assistant JARVIS is shutting down,good bye")
                print("Your personal AI assistant JARVIS is shutting down,good bye")
                break
            
        if 'wikipedia' in statement:
            speak('searching wikipedia......')
            statement=statement.replace("wikipedia","")
            results=wikipedia.summary(statement,sentences=3)
            speak("According to wikipedia.....")
            print(results)
            speak(results)
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open for you")
            time.sleep(5)
        elif "open google" in statement:
            webbrowser.open_new_tab('https://www.google.com')
            speak("google search is open for you")
            time.sleep(5)
        elif "open gmail" in statement:
            webbrowser.open_new_tab('gmail.com')
            speak("your gmail is open for you")
            time.sleep(5)
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak('whats the city name?')
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q"+city_name
            response=requests.get(complete_url)
            x=response.json()
            if x['cod'] !='404':
                y=x['main']
                current_temperature=y["temp"]
                current_humidity=y["humidity"]
                z=x['weather']
                weather_description=z[0]['description']
                speak("the temparature in kelvin units is" + str(current_temperature)+ "\n humidity in percentage is" +str(current_humidity)+"\n weather description"+str(weather_description))
                print("the temparature in kelvin units is" +str(current_temperature)+"\n humidity in percentage is"+str(current_humidity)+"\n weather description"+str(weather_description))
            
            else:
                speak("city not found")
                print("city not found")
                
        elif "time" in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
    
        elif "who are you" in statement or "what can you do" in statement:
                  speak("IAM JARVIS YOUR PERSONAL AI ASSISTANT WHO CAN DO ANY TASK YOU ASK ME TO DO!!!")
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                  speak("I was built by Deepak")
                  print("I was built by Deepak")
        elif "open stack overflow" in statement:
                  webbrowser.open_new_tab("https://stackoverflow.com/login")
                  time.sleep(5)
        elif "news" in statement:
                  news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                  speak("here are some headlines for you from TOI, happy reading!")
                  time.sleep(5)
                  
        elif "search" in statement:
                  statement=statement.replace("search"," ")
                  webbrowser.open_new_tab("statement")
                  time.sleep(5)
                  
        elif "ask" in statement:
                  speak("I can answer to computational and geographical questions too just try me!! what do you want to ask")
                  question=takeCommand()
                  app_id="R2K75H-7ELALHR35X"
                  client=wolframalpha.client("R2K75H-7ELALHR35X")
                  res=client.query(question)
                  answer=next(res.results).text
                  speak(answer) 
                  print(answer)
        elif "log off" in statement or "sign off" in statement or "shut dowm" in statement:
                  speak("your pc will shut down in 10 seconds make sure you have saved and logged off from all applications")
                  subprocess.call(['shut dowm',"/1"])
                  time.sleep(3)

