from fastapi import FastAPI
from pydantic import BaseModel 
import openai, os 
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
conversation_history = [] 
client = OpenAI()

class Prompt(BaseModel):
    text: str 
    
@app.post("/ask")
def talk_to_GPT(prompt: Prompt):
    conversation_history.append({"role": "user", "content": prompt.text})
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = conversation_history
    )
    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return {"reply": reply}