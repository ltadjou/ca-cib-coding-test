# Utiliser une image de base avec Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Télécharger le modèle Hugging Face lors de la construction de l'image
ARG HF_MODEL_NAME
ARG HF_TOKEN

# Définir les variables d’environnement
ENV HF_MODEL_NAME=${HF_MODEL_NAME}
ENV HF_TOKEN=${HF_TOKEN}

# Copier le code de l'application
COPY . .

# Exposer le port sur lequel FastAPI va tourner
EXPOSE 8000

# Commande pour lancer FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]