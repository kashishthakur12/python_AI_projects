import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import traceback

#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<your key here>"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def processCommand(c):
    c = c.lower()
    if "open google " in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook " in c.lower():    
        webbrowser.open("https://facebook.com")
    elif "open linkedin " in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chatgpt " in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().starswith("play")  :
        song = c.lower().spilt(" ")[1]
        link=musicLibrary.music[song]  
        webbrowser.open(link)
    else:
        speak("sorry,I didn't understand the command.")

# Main block
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Listen for wake word and input
        recognizer = sr.Recognizer()

                    
        print("recognizing.............")
        try:
            with sr.Microphone() as source:
               print("Listening...")
               audio = recognizer.listen(source,timeout=2, phrase_time_limit=2)
            
            word= recognizer.recognize_google(audio)
            if(word.lower() == "hey jarvis"):
                speak("ya")
            #listen for command
            with sr.Microphone() as source:
               print("jarviss active...")
               audio = recognizer.listen(source)
               command = recognizer.recognize_google(audio)
               print("You said:", command)
               
               if "exit" in command.lower() or "quit" in command.lower():
                        speak("Shutting down. Goodbye!")
                        break
               processCommand(command)
            
        except Exception as e:
            print("Error:",e)
            traceback.print_exc()
                            