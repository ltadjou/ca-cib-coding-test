from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ChatMessage(BaseModel):
    message: str

@app.post("/doc-content")
async def chat(doc_content: str):
    # Ici, vous pouvez ajouter la logique de traitement du message
    response = f"Vous avez dit: {doc_content}"
    return {"response": response}

