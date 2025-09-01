# test_tts.py
import pyttsx3

engine = pyttsx3.init()

print("Voices available on your system:")
voices = engine.getProperty('voices')
for voice in voices:
    print(f" - ID: {voice.id}")

# Let's try to set a specific voice
# On Windows, you might see a 'Zira' or 'David' voice. Let's try Zira.
# Replace the ID below with one from your list if this doesn't work.
try:
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
except Exception as e:
    print(f"Could not set Zira's voice, using default. Error: {e}")


print("\nSpeaking a test sentence...")
engine.say("Hello world, can you hear me now?")
engine.runAndWait()
print("Test finished.")