# core/commands.py

import webbrowser
import datetime
import pywhatkit
from core.tts import speak

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def open_website(url):
    speak(f"Opening {url}")
    webbrowser.open(url)

def search_youtube(query):
    speak(f"Searching YouTube for {query}")
    pywhatkit.playonyt(query)

def search_google(query):
    speak(f"Searching Google for {query}")
    pywhatkit.search(query)