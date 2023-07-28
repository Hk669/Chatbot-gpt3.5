from langchain.chat_models import ChatOpenAI
from apikey import OPEN_AI_KEY

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import AIMessage,HumanMessage,SystemMessage
from flask import Flask,request,render_template

app = Flask(__name__)


#chat model intialization
chat = ChatOpenAI(
    temperature = 0.7,
    openai_api_key = OPEN_AI_KEY,
    openai_organization = ORG_KEY
    )


# function for the prompt and user_input
def user(prompt):
    messages = [
        SystemMessage(
            content = "You're the CEO of AdvantageAI, startup which provides AI services and SMM"
        ),
        HumanMessage(
            content = prompt
        )
    ]
    # returns the message as CEO of AdvantageAI
    response = chat(messages)

    return response.content

# API routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/ask",methods=['POST'])
def ask():
    user_input = request.form['user_input']
    return user(user_input)



if __name__ == "__main__":
    app.run(debug=True)
