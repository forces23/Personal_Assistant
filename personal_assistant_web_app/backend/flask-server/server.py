from flask import Flask, request, jsonify
from flask_cors import CORS
# from ai_openai_chatgpt import chat_with_chatGPT
# from ai_google_bard import chat_with_Bard
from LLM_LLama2 import chat_with_LLama2


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('userMessage', '')

    # Always respond with a fixed message
    # bot_response = chat_with_chatGPT(user_message) # uses OpenAI chatGPT
    # bot_response = chat_with_Bard(user_message) # uses Google Bard
    bot_response = chat_with_LLama2(user_message) # uses LLama2 LLM

    print(f"bot_response: {bot_response}")
    return jsonify({'botResponse': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)




