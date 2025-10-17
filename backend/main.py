from fastapi import FastAPI, Depends
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from db.database import get_db
from sqlalchemy.orm import Session 
from db.models import Message
from db.utils import format_messages_for_gpt

load_dotenv()  # loads OPENAI_API_KEY from .env

app = FastAPI()
conversation_history = []
client = OpenAI()  # automatically reads your key

class Prompt(BaseModel):
    text: str

@app.post("/ask")

def talk_to_GPT(prompt: Prompt, db: Session = Depends(get_db)):
    
    # load conversatio history from DB 
    stored_messages = db.query(Message).order_by(Message.timestamp.asc()).all()
    conversation = format_messages_for_gpt(stored_messages)
    
    # Add new user message to DB
    conversation.append({"role": "user", "content": prompt.text})
    db.add(Message(role="user", content = prompt.text))
    
    
    # Call GPT with full conversation 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    reply = response.choices[0].message.content

    # Save response from GPT
    db.add(Message(role="assistant", content=reply))
    db.commit()
    
    return {"reply": reply}
