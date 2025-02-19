import streamlit as st
import requests
import os
from docx import Document
from io import BytesIO

# Titre de l'application
st.title("Mon Application de Chat avec Upload de Fichier")

# Upload de fichier
uploaded_file = st.file_uploader("Choisissez un fichier", type=["pdf", "docx", "doc"])
if uploaded_file is not None:
    # Obtenir le nom du fichier
    filename = uploaded_file.name

    # Vérifier l'extension du fichier
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension in  [".docx", ".doc"]:
        # Lire le fichier DOCX
        try:
            doc = Document(uploaded_file)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])

            # Afficher le contenu du fichier (optionnel)
            st.write("Contenu du fichier :")
            st.write(content)

            # Envoyer le contenu à l'API
            if st.button("Envoyer à l'API"):
                response = requests.post(
                    "http://backend:8000/doc-content",  # Remplacez par l'URL de votre API
                    json={"content": content}
                )

                if response.status_code == 200:
                    st.success("Contenu envoyé avec succès à l'API !")
                    st.json(response.json())  # Afficher la réponse de l'API
                else:
                    st.error(f"Erreur lors de l'envoi à l'API : {response.status_code}")
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier : {e}")
    elif file_extension == ".pdf":
        st.success(f"Erreur : Le fichier {filename} n'est pas un fichier PDF.")
    else:
        st.error(f"Erreur : Le fichier {filename} n'est pas prise en charge")