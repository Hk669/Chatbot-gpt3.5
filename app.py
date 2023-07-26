from flask import Flask, jsonify, render_template, request
import openai
from apikey import OPEN_AI_KEY
app = Flask(__name__)

openai.api_key = OPEN_AI_KEY

def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
        {"role": "system","content": "You are AdvantageAI CEO, a startup which provides AI service and SMM"},
        {"role":"user","content":prompt}
        ]
    )
    return response['choices'][0]['message']['content']


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask",methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = ask_gpt3(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
