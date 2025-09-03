# server/server.py

from flask import Flask, request, jsonify
from waitress import serve  # <-- Import serve from waitress
from core.ai_chat import get_ai_response
import core.commands as commands

app = Flask(__name__)

@app.route('/api/command', methods=['POST'])
def process_command():
    data = request.json
    user_command = data.get('command')

    if not user_command:
        return jsonify({"error": "No command provided"}), 400

    print(f"Received command: {user_command}")
    ai_response = get_ai_response(user_command)
    print(f"AI Response: {ai_response}")

    response_data = {}

    if ai_response.startswith("ACTION:"):
        parts = ai_response.split('|')
        action_name = parts[0].replace("ACTION:", "").strip()
        action_param = parts[1].strip() if len(parts) > 1 else ""

        if action_name == "get_time":
            response_data = commands.get_time()
        elif action_name == "open_website":
            response_data = commands.open_website(action_param)
        elif action_name == "search_youtube":
            response_data = commands.search_youtube(action_param)
        elif action_name == "search_google":
            response_data = commands.search_google(action_param)
        else:
            response_data = {"speak": "Sorry, I don't know how to perform that action."}
    else:
        # It's a conversational response
        response_data = {"speak": ai_response}

    return jsonify(response_data)

if __name__ == "__main__":
    print("Starting Obito server with Waitress...")
    # Use waitress.serve to run the app in a production-ready way
    serve(app, host='0.0.0.0', port=5000)
