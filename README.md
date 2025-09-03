# Obito Voice Assistant 🤖

Obito is a "Jarvis-like" voice assistant built with Python, designed to provide a seamless and interactive voice-controlled experience. Powered by Google's Gemini API for conversational AI, Obito listens for a wake word, executes tasks like opening websites and searching the web, and responds with a clear, computer-generated voice.

## ✨ Features

- **Wake Word Detection**: Activates when you say "Obito".
- **Client-Server Architecture**: Separates the AI "brain" (server) from the user interface (client), enabling flexibility to run on different machines.
- **Real-time Conversation**: Leverages Google's Gemini API for natural and intelligent responses.
- **Task Execution**: Supports commands like opening websites, searching Google/YouTube, and telling the time.
- **Voice Output**: Delivers responses using clear, computer-generated speech.
- **Siri-like Interface**: Features a clean, circular GUI with real-time visual feedback.

## 🛠️ Setup & Installation

Follow these steps to set up and run Obito on your local network.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/obito-assistant.git
cd obito-assistant
```

### 2. Create a Virtual Environment & Install Dependencies

Using a virtual environment is highly recommended to keep dependencies isolated.

```bash
# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows
# For macOS/Linux: source venv/bin/activate

# Install required libraries
pip install -r requirements.txt
```

### 3. Configure the Server

The server requires a Google Gemini API key to function.

1. Navigate to the `server/` directory.
2. Create a `.env` file in the `server/` directory.
3. Add your API key to the `.env` file as follows:

```plaintext
GEMINI_API_KEY="YOUR_SECRET_GEMINI_API_KEY"
```

You can obtain a free API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Configure the Client

The client needs the IP address of the machine running the server.

1. Navigate to the `client/` directory.
2. Open the `config.json` file.
3. Update the `server_url` to the local IP address of the server machine (find it using `ipconfig` on Windows or `ifconfig`/`ip addr` on macOS/Linux):

```json
{
    "server_url": "http://192.168.1.10:5000/api/command"
}
```

## ▶️ How to Run

Run the server and client in separate terminal windows.

### Start the Server

```bash
cd server
python server.py
```

### Start the Client

```bash
cd client
python main.py
```

Once the Obito GUI appears, it will display "Listening...". Say the wake word "Obito" to start issuing commands.

## 💻 Technologies Used

- **Python**: Core programming language.
- **Flask**: Powers the server-side API.
- **PyQt5**: Provides the client-side graphical user interface.
- **Google Gemini**: Enables natural language processing and AI responses.
- **SpeechRecognition**: Handles voice command recognition.
- **pyttsx3**: Converts text to speech for voice output.

## 📝 Notes

- Ensure both the client and server machines are on the same network for proper communication.
- The wake word "Obito" is case-sensitive and must be spoken clearly.
- For troubleshooting, check the console output in both terminals for error messages.