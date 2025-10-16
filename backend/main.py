from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from .env

app = FastAPI()
conversation_history = []
client = OpenAI()  # automatically reads your key

class Prompt(BaseModel):
    text: str

@app.post("/ask")
def talk_to_GPT(prompt: Prompt):
    conversation_history.append({"role": "user", "content": prompt.text})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return {"reply": reply}
