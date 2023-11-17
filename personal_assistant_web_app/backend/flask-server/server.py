from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_openai_chatgpt import chat_with_bot
from ai_google_bard import chat_with_bot


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('userMessage', '')

    # Always respond with a fixed message
    # bot_response = chat_with_bot(user_message) # uses OpenAI chatGPT
    bot_response = chat_with_bot(user_message) # uses Google Bard

    print(f"bot_response: {bot_response}")
    return jsonify({'botResponse': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)




