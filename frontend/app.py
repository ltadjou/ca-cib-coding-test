import streamlit as st
import requests

# Titre de l'application
st.title("Mon Application de Chat avec Upload de Fichier")

# Upload de fichier
uploaded_file = st.file_uploader("Choisissez un fichier", type=["txt", "pdf", "png", "jpg"])
if uploaded_file is not None:
    st.write("Fichier uploadé avec succès!")

# Chat
user_input = st.text_input("Entrez votre message")
if st.button("Envoyer"):
    response = requests.post("http://backend:8000/chat", json={"message": user_input})
    st.write(f"Réponse du serveur: {response.json()['response']}")