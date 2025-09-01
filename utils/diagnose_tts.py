# diagnose_tts.py
import pyttsx3
import sys

print(f"Python version: {sys.version}")
print(f"pyttsx3 is being imported from: {pyttsx3.__file__}")

try:
    # We will try every available driver to see if any work.
    drivers = ['sapi5', 'nsss', 'espeak']
    working_driver = None
    
    for driver in drivers:
        try:
            print(f"\n--- Attempting to initialize with '{driver}' driver ---")
            engine = pyttsx3.init(driver)
            engine.say("Testing the " + driver + " driver.")
            engine.runAndWait()
            print(f"SUCCESS: The '{driver}' driver seems to be working.")
            working_driver = driver
            engine.stop()
            break # Stop after the first success
        except Exception as e:
            print(f"FAILED: The '{driver}' driver failed with error: {e}")

    if not working_driver:
        print("\n--- DIAGNOSIS ---")
        print("All TTS drivers failed to initialize.")
        print("This suggests an issue with your Windows Speech API (SAPI5) or missing speech packages.")
        print("Possible Solutions:")
        print("1. Ensure your Windows language pack includes Text-to-Speech features (Settings -> Time & Language -> Language).")
        print("2. Check if your system's audio output is working and not muted.")
        print("3. Reinstalling pyttsx3 might help: pip uninstall pyttsx3 then pip install pyttsx3")

except Exception as e:
    print(f"\nA critical error occurred: {e}")