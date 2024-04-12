from openai import OpenAI
from dotenv import load_dotenv
import os



load_dotenv(dotenv_path='components/.env')

def openai_Find_Intention(question):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_TOKEN"),)

    gpt_input = "Si l'intention de ce message nécessite une recherche sur le net réponds 1 sinon réponds au message: " + question

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a genius of the web."},
        {"role": "user", "content": gpt_input}
    ]
    )

    return completion.choices[0].message.content


def openai_request(question, brave_input):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_TOKEN"),)

    gpt_input = "Answer this question: " + question + " taking in consideration this knowledge: " + brave_input

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a genius of the web."},
        {"role": "user", "content": gpt_input}
    ]
    )

    return completion.choices[0].message.content



