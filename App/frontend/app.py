import streamlit as st
import requests
import os
from docx import Document


from docx import Document


def read_docx_clean(file_path):
    doc = Document(file_path)
    content = []
    
    # Iterate over document elements while preserving order
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Paragraphs
            para = element.xpath('.//w:t')
            text = ''.join([node.text for node in para if node.text])
            if text.strip():
                content.append(text +"\n")
        elif element.tag.endswith('tbl'):  # Tables
            table = next((t for t in doc.tables if t._element == element), None)
            if table:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells)  # Join table cells
                    content.append(row_text+"\n")  # Append each row separately
    
    return "\n".join(content)  # Ensure structure is preserved
   
    


# Titre de l'application
st.title("CA-CIB Conding test")
st.header("Word Document Extraction")

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
            content = read_docx_clean(uploaded_file)
            # Afficher le contenu du fichier (optionnel)
            st.success("Successfull extraction of the document content")

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
            st.error(f"Errorwhen reading the file : {e}")
    elif file_extension == ".pdf":
        st.success(f"Erreur : Le fichier {filename} n'est pas un fichier PDF.")
    else:
        st.error(f"Erreur : Le fichier {filename} n'est pas prise en charge")

st.header("Chat: NER")

# Text input field
user_input = st.text_area("Enter chat text for NER:", "")

# Button to submit
if st.button("Submit"):
    response = requests.post(
        "http://backend:8000/extract-entities",  # Remplacez par l'URL de votre API
        json={"text": user_input}
    )

    if response.status_code == 200:
        st.success("Contenu envoyé avec succès à l'API !")
        st.json(response.json())  # Afficher la réponse de l'API
    else:
        st.error(f"Erreur lors de l'envoi à l'API : {response.status_code}")
st.header("PDF: Entities Extraction")