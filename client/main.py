# client/main.py

import sys
import threading
import requests
import webbrowser
import json  # <-- Add this import
from PyQt5.QtWidgets import QApplication

from interface.gui import ObitoGUI
from core.wakeword import listen_for_wake_word
from core.speech_recog import listen_for_command

# --- New Configuration Loading ---
def load_config():
    """Loads the server URL from the config.json file."""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config.get("server_url", "http://127.0.0.1:5000/api/command")
    except FileNotFoundError:
        print("Warning: config.json not found. Using default server URL.")
        return "http://127.0.0.1:5000/api/command"

comm = None
SERVER_URL = load_config() # <-- Load the URL from the function

def handle_server_response(response_data):
    """Parses the server's response and acts on it."""
    if not response_data:
        return

    if 'speak' in response_data and comm:
        comm.text_to_speak.emit(response_data['speak'])

    if response_data.get('action') == 'open_url' and 'url' in response_data:
        webbrowser.open(response_data['url'])

def process_command(command):
    """Sends command to server and handles the response."""
    if comm:
        comm.update_label.emit("Thinking...")

    try:
        response = requests.post(SERVER_URL, json={'command': command})
        if response.status_code == 200:
            handle_server_response(response.json())
        else:
            print(f"Error from server: {response.status_code}")
            if comm:
                comm.text_to_speak.emit("Sorry, I got an error from my brain.")
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to server at {SERVER_URL}. Error: {e}")
        if comm:
            comm.text_to_speak.emit("I can't seem to connect to the server.")

def start_assistant_logic():
    print("Obito client logic thread started.")
    print(f"Connecting to server at: {SERVER_URL}")
    while True:
        try:
            if comm:
                comm.update_label.emit("Listening...")
            if listen_for_wake_word():
                if comm:
                    comm.update_label.emit("Wake word detected!")
                    comm.text_to_speak.emit("Yes?")

                command = listen_for_command()
                if command:
                    if comm:
                        comm.update_label.emit(f'You said: "{command}"')
                    process_command(command)
        except Exception as e:
            print(f"An error occurred in assistant logic: {e}")
            break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obito_gui = ObitoGUI()
    comm = obito_gui.comm

    assistant_thread = threading.Thread(target=start_assistant_logic, daemon=True)
    assistant_thread.start()

    sys.exit(app.exec_())

