# Chatbot with GPT-3.5 Turbo

This is a simple chatbot built using Flask and the OpenAI GPT-3.5 turbo model. The chatbot allows users to interact with a language model powered by GPT-3.5 turbo and get responses based on their input.




https://github.com/Hk669/Openai-Chatbot/assets/96101829/edbe003f-0f60-4209-b46d-d5c80d517859



## Prerequisites

Before running the chatbot, make sure you have the following installed:

- Python 
- Flask
- OpenAI Python SDK (`openai`)

You also need to obtain an API key from OpenAI to access the GPT-3.5 turbo model. Save your API key in a file named `apikey.py`, and define the API key as a variable named `OPEN_AI_KEY` in that file.

## Getting Started

1. Clone the repository to your local machine:

```shell
git clone https://github.com/Hk669/Chatbot-gpt3.5.git
```

2. Run the Flask app:

```shell
python app.py
```

The chatbot server will start running on `http://localhost:5000`.

3. Access the Chatbot

Open your web browser and navigate to `http://localhost:5000`. You will see the chat interface, and you can start interacting with the chatbot.

## How the Chatbot Works

The Flask app uses the OpenAI Python SDK (`openai`) to interact with the GPT-3.5 turbo model. The GPT-3.5 turbo model is a chat model, so it can handle back-and-forth conversations like a chatbot.

The `/ask` route in the Flask app takes user input from the frontend and sends it to the `ask_gpt3()` function, which uses the `openai.ChatCompletion.create()` method to interact with the GPT-3.5 turbo model and get a response.

## Customizing the Chatbot

You can customize the behavior of the chatbot by modifying the `ask_gpt3()` function and the initial `messages` provided to the `openai.ChatCompletion.create()` method. You can add more messages to set up the context or change the system and user roles to influence the chatbot's responses.

## Deployment

To deploy the chatbot to a production environment, consider using a production-ready WSGI server like Gunicorn or deploying it on cloud platforms like Heroku, AWS, or Azure.

Remember to keep your API key and other sensitive information secure when deploying to production.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to enhance and improve this chatbot based on your requirements. If you have any questions or need further assistance, feel free to reach out!


