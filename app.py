from flask import Flask, jsonify, render_template, request
import openai
from apikey import OPEN_AI_KEY
from dataset import dataset
# from Advanatge import services, mission, company_name


# with open(r"C:\Users\hrush\OneDrive\Desktop\chatmodel\fine_tuned_model_id.txt", "r") as f:
#     fine_tune_model_id = f.read().strip()

default_response = "This information is not available at the moment.For more queries can contact our executive"

# intitalizing the flask app
app = Flask(__name__)

# api key from openai
openai.api_key = OPEN_AI_KEY

# function for model prompt and query
def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": "You're an AI assistant who answers user questions from the dataset."},
            {"role": "user", "content": prompt}
        ],
        model='gpt-3.5-turbo',
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response['choices'][0]['message']['content']
    return answer
    

# this renders a html template for the user 
@app.route("/")
def index():
    return render_template("index.html")

# post method to request the gpt model to answer the question asked by user
@app.route("/ask",methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = ask_gpt3(user_input)
    return jsonify({"response": response})



if __name__ == "__main__":
    app.run(debug=True)
