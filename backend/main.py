from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    # Ici, vous pouvez ajouter la logique de traitement du message
    response = f"Vous avez dit: {chat_message.message}"
    return {"response": response}