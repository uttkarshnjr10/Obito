# core/tts.py

import pyttsx3

engine = None

try:
    print("Initializing TTS engine...")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"  Voice {i}:")
        print(f"    - ID: {voice.id}")
        print(f"    - Name: {voice.name}")

    # --- VOICE SELECTION ---
    # Change the number in voices[...] to select a different voice.
    # For example, use voices[0].id for the first voice in the list.
    if len(voices) > 1:
        # Set to the second voice (often female) if available
        engine.setProperty('voice', voices[1].id) 
    elif len(voices) > 0:
        # Otherwise, use the first available voice
        engine.setProperty('voice', voices[0].id)
    else:
        print("No TTS voices found on this system.")
        engine = None

    if engine:
        engine.setProperty('rate', 180)
        print(f"\nSelected Voice: {engine.getProperty('voice')}")
        print("TTS engine initialized successfully.\n")

except Exception as e:
    print(f"Failed to initialize TTS engine: {e}")
    engine = None


def speak(text):
    if engine:
        # No need to print here, main.py will handle it
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Obito (TTS UNAVAILABLE): {text}")