# core/wakeword.py

import speech_recognition as sr
from config import WAKE_WORD

def listen_for_wake_word():
    """
    Listens continuously for the wake word.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening for wake word: '{WAKE_WORD}'...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            try:
                audio = recognizer.listen(source)
                # Using Google recognizer for better accuracy even for the wake word
                phrase = recognizer.recognize_google(audio, language='en-in')
                print(f"Heard: {phrase}") # Debug print
                if WAKE_WORD in phrase.lower():
                    print("Wake word detected!")
                    return True
            except sr.UnknownValueError:
                # This is expected when there is silence
                pass
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")