import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services.doc_services import DocContentProssecing, RequestData, CustomResponse
from services.entities_utils import EntitiesModel, TextRequest, EntityResponse

app = FastAPI()

# Charger le modèle NER au démarrage de l'application
model_name = os.getenv("HF_MODEL_NAME")
hf_token = os.getenv("HF_TOKEN")
ner_model = EntitiesModel(model_name, hf_token)

@app.post("/doc-content")
async def chat(request_data: RequestData):
    try:
        # Ici, vous pouvez ajouter la logique de traitement du message
        extrated_data = DocContentProssecing.extract_information(request_data.content)
        response = CustomResponse(
            message="Success",
            data = extrated_data
        )
        # Retourner la réponse avec le code HTTP 200
        return JSONResponse(content=response.model_dump(), status_code=200)
    except Exception as e:
        # En cas d'erreur, retourner une réponse d'erreur
        raise HTTPException(
            status_code=500,
            detail="Error",
            headers={"X-Error": str(e)},
        )

@app.post("/extract-entities")
async def extract_entities(request: TextRequest):
    print(request.text)
    try:
        # Extraire les entités nommées
        entities = ner_model.extract_entities(request.text)
        response = CustomResponse(
            message="Success",
            data = {'entities': entities}
        )
        return JSONResponse(content=response.model_dump(), status_code=200)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error",
            headers={"X-Error": str(e)},
        )