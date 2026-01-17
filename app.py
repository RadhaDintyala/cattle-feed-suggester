from flask import Flask, render_template, request, jsonify
from chatbot_logic import chatbot_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    gobar = data['gobar']
    eating = data['eating']
    activity = data['activity']
    milk = data['milk']
    temp = data['temp']
    dung = data['dung']
    body_cond = data['body_condition']

    response = chatbot_response(gobar, eating, activity, milk, temp, dung, body_cond)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run()
