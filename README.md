# Obito Voice Assistant 🤖

Obito is a "Jarvis-like" voice assistant built with Python. It uses Google's Gemini for conversational AI and can perform tasks like opening websites, searching YouTube, and answering questions.



## ✨ Features
- **Wake Word Detection**: Activates on hearing "Obito".
- **Real-time Conversation**: Powered by Google's Gemini for natural, intelligent responses.
- **Task Execution**: Can open websites, search Google/YouTube, and tell the time.
- **Voice Output**: Responds with a clear, computer-generated voice.
- **Siri-like Interface**: A clean, circular GUI that provides visual feedback.

## 🛠️ Setup & Installation

Follow these steps to get Obito running on your local machine.

### **1. Clone the Repository**
First, clone this repository to your computer:
```bash
git clone [https://github.com/YOUR_USERNAME/obito-voice-assistant.git](https://github.com/YOUR_USERNAME/obito-voice-assistant.git)
cd obito-voice-assistant
```

### **2. Create a Virtual Environment**
It is highly recommended to use a virtual environment to keep dependencies isolated.
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
Install all the required Python libraries using the `requirements.txt` file.
```bash
pip install -r requirements.txt
```
**Note for Windows Users:** If you run into an error with `PyAudio`, you may need to install it manually. Please follow the instructions from Phase 2 of the original guide.

### **4. Set Up Your API Key**
Obito uses the Google Gemini API. You need to provide your own API key to enable the conversational features.

1.  Create a file named `.env` in the root directory of the project.
2.  Inside the `.env` file, add your API key in the following format:
    ```
    GEMINI_API_KEY="YOUR_SECRET_GEMINI_API_KEY"
    ```
3.  You can get a free API key from [Google AI Studio](https://aistudio.google.com/).

### **5. Run the Assistant**
Once everything is set up, you can start the assistant by running:
```bash
python main.py
```
Say the wake word "Obito" and start giving it commands!