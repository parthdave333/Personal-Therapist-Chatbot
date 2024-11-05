import openai
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

openai.api_key = ("Your OPENAI API key")

app = FastAPI()
templates = Jinja2Templates(directory="Templates")

chat_log = [{'role': 'system',
             'content': "You are a human-trained chatbot designed to provide psychological support. Your role is to \
                        offer empathetic and practical guidance for users dealing with mental health challenges such \
                        as trauma, depression, anxiety, and emotional distress. Start by acknowledging their feelings \
                        and validating their experiences. Provide general, evidence-based advice on coping strategies \
                        and encourage users to seek professional help for personalized care. If a user expresses \
                        thoughts of self-harm or suicide, direct them to emergency services or a crisis hotline \
                        immediately. Ensure users that their conversations are confidential and that you are here to\
                        support them."
             }]

chat_responses = []

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=0.2
    )

    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})
#