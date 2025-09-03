# server/core/commands.py

import datetime

# NOTE: We have removed 'speak', 'webbrowser', and 'pywhatkit' imports.
# The server only returns instructions, it does not perform actions.

def get_time():
    """Returns the current time in a dictionary format for the client."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return {"speak": f"The current time is {current_time}"}

def open_website(url):
    """Returns instructions to open a URL."""
    return {
        "speak": f"Opening {url}",
        "action": "open_url",
        "url": url
    }

def search_youtube(query):
    """Returns instructions to search YouTube."""
    # We construct the URL manually for the client to open
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    return {
        "speak": f"Searching YouTube for {query}",
        "action": "open_url",
        "url": url
    }

def search_google(query):
    """Returns instructions to search Google."""
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    return {
        "speak": f"Searching Google for {query}",
        "action": "open_url",
        "url": url
    }
