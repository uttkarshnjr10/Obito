Obito Voice Assistant 🤖
Obito is a "Jarvis-like" voice assistant built with Python. It uses a modern client-server architecture, with Google's Gemini API powering its conversational AI. It listens for a wake word, performs tasks like opening websites and searching the web, and responds with a clear voice.

✨ Features
Wake Word Detection: Activates on hearing "Obito".

Client-Server Architecture: The AI "brain" (server) is separate from the user interface (client), allowing it to run on different machines.

Real-time Conversation: Powered by Google's Gemini for natural, intelligent responses.

Task Execution: Can open websites, search Google/YouTube, and tell the time.

Voice Output: Responds with a clear, computer-generated voice.

Siri-like Interface: A clean, circular GUI that provides visual feedback.

🛠️ Setup & Installation
Follow these steps to get Obito running on your local network.

1. Clone the Repository
First, clone this repository to your computer:

git clone [https://github.com/YOUR_USERNAME/obito-assistant.git](https://github.com/YOUR_USERNAME/obito-assistant.git)
cd obito-assistant

2. Create a Virtual Environment & Install Dependencies
It is highly recommended to use a virtual environment to keep dependencies isolated.

# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows

# Install all required libraries
pip install -r requirements.txt

3. Configure the Server
The server needs your Google Gemini API key to function.

Navigate to the server/ directory.

Create a file named .env.

Inside the .env file, add your API key like this:

GEMINI_API_KEY="YOUR_SECRET_GEMINI_API_KEY"

You can get a free API key from Google AI Studio.

4. Configure the Client
The client needs to know the IP address of the computer running the server.

Navigate to the client/ directory.

You will find a file named config.json.

Open config.json and change the server_url to the local IP address of the server machine. (You can find this by running ipconfig on the server machine).

{
    "server_url": "[http://192.168.1.10:5000/api/command](http://192.168.1.10:5000/api/command)" 
}

▶️ How to Run
You need to run the server and client in two separate terminals.

Start the Server:
Open a terminal, navigate to the server directory, and run:

python server.py

Start the Client:
Open a new terminal, navigate to the client directory, and run:

python main.py

The Obito GUI will appear, and after it says "Listening...", you can say the wake word "Obito" to start giving it commands!

💻 Technologies Used
Python: Core programming language.

Flask: For the server-side API.

PyQt5: For the client-side graphical user interface.

Google Gemini: For the natural language processing and AI responses.

SpeechRecognition: For recognizing voice commands.

pyttsx3: For text-to-speech voice output.