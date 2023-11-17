from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    # In a real scenario, you would process this message and generate a response
    bot_response = f"Bot: I received '{user_message}'"
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)