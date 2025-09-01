# main.py

import sys
import threading
from PyQt5.QtWidgets import QApplication

from interface.gui import ObitoGUI
from core.wakeword import listen_for_wake_word
from core.speech_recog import listen_for_command
import core.commands as commands
from core.ai_chat import get_ai_response

# Global variable to hold reference to the GUI's communication object
comm = None

def process_command(command):
    ai_response = get_ai_response(command)

    if ai_response.startswith("ACTION:"):
        parts = ai_response.split('|')
        action_name = parts[0].replace("ACTION:", "").strip()
        action_param = parts[1].strip() if len(parts) > 1 else ""

        # Emit signal to update GUI before performing action
        if comm:
            comm.update_label.emit(f"Executing: {action_name}")

        # The action functions themselves call speak(), which is fine
        if action_name == "get_time":
            commands.get_time()
        elif action_name == "open_website":
            commands.open_website(action_param)
        elif action_name == "search_youtube":
            commands.search_youtube(action_param)
        elif action_name == "search_google":
            commands.search_google(action_param)
        else:
            if comm:
                comm.text_to_speak.emit("Sorry, I recognized an action but don't know how to perform it.")
    else:
        # For conversational responses, emit both signals
        if comm:
            comm.update_label.emit("Speaking...")
            comm.text_to_speak.emit(ai_response)

def start_assistant_logic():
    print("Obito logic thread started.")
    
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
                        comm.update_label.emit("Thinking...")
                    process_command(command)
        except Exception as e:
            print(f"An error occurred in assistant logic: {e}")
            break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obito_gui = ObitoGUI()
    
    # Set the global communicator object
    comm = obito_gui.comm
    
    assistant_thread = threading.Thread(target=start_assistant_logic)
    assistant_thread.daemon = True
    assistant_thread.start()
    
    sys.exit(app.exec_())