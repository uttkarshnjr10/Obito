# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Wake word
WAKE_WORD = "obito"

# Gemini API Key
# The key is now securely loaded from your .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Make sure you have set it in your .env file.")