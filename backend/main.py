from fastapi import FastAPI
from pydantic import BaseModel 
import openai, os 
from dotenv import load_dotenv

# load .env variables 
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# initialize FastAPI app 
app = FastAPI()

# define request model 
class Prompt(BaseModel): 
    text:str 
    
class Prompt(BaseModel):
    num: int 

# define route 
@app.post("/ask")
async def ask_agent(prompt: Prompt): 
    return {"reply": f"You said {prompt.text}"}

@app.post("/arbitrayRoute")
async def some_random_function_name(prompt: Prompt):
        return {"reply": f"You gave the number {prompt.num}"}
