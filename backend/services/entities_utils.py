import os
from transformers import pipeline
from pydantic import BaseModel


# Modèle Pydantic pour la requête
class TextRequest(BaseModel):
    text: str

# Modèle Pydantic pour la réponse
class EntityResponse(BaseModel):
    entities: list[tuple[str, str]]


class EntitiesModel:
    def __init__(self, model_name: str, hf_token: str):
        # Télécharger et charger le modèle Hugging Face
        self.nlp = pipeline(
            "ner",
            model=model_name,
            token=hf_token,
            aggregation_strategy="simple"
        )

    def extract_entities(self, text: str):
        # Appliquer le modèle NER sur le texte
        entities = self.nlp(text)
        
        # Formater les entités nommées
        formatted_entities = [(ent["word"], ent["entity_group"]) for ent in entities if ent["score"] >=0.80]
        return formatted_entities
    

