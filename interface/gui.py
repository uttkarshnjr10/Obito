# interface/gui.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from core.tts import speak

class Communicate(QObject):
    # Create a signal that can carry a string
    text_to_speak = pyqtSignal(str)
    update_label = pyqtSignal(str)

class ObitoGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.comm = Communicate()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Obito Assistant")
        self.setGeometry(100, 100, 400, 400)

        # Make the window frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Main label for displaying text
        self.label = QLabel("Initializing...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            background-color: rgba(0, 20, 50, 0.8);
            color: white;
            font-size: 24px;
            font-family: Arial;
            border-radius: 200px;
        """)
        self.label.setGeometry(0, 0, 400, 400)

        # --- Connect Signals to Slots ---
        self.comm.update_label.connect(self.set_label_text)
        self.comm.text_to_speak.connect(self.speak_text)
        
        self.show()

    def set_label_text(self, text):
        """This function (slot) updates the GUI label."""
        self.label.setText(text)

    def speak_text(self, text):
        """This function (slot) calls the TTS engine."""
        speak(text)

# This is for testing the GUI independently
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ObitoGUI()
    sys.exit(app.exec_())