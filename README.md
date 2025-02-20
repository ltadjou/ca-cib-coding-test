# ca-cib-coding-test


**Description** : This repository contains the code of all documents requested as part of the CA-CIB coding game.

---

## Resquested Documentation 
1. [Global Architecture Document(GAD)](./Documentation/Global%20Architecture%20Document%20(GAD).pdf)

2. [Finuetuning model for NER](./Documentation/Global%20Methodology%20Document%20(GMD)-NER%20Finetuning.pdf)
3. [Entities Extrction with LLM](./Documentation/LLMs%20Entities%20ExtractionUSING%20FONCTIOnS_cALLING.pdf)


---

## How to Launch the Application

To launch the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ltadjou/ca-cib-coding-test

2. Navigate to the project directory:
   ```bash
   cd ca-cib-coding-test/App

3. Run the following command to build and start the Docker containers:
   ```bash
   docker-compose up --build

---

## Accessing the Application

Once the containers are up and running, you can access the homepage via the following link:

- **Homepage**: [http://localhost:8501/](http://localhost:8501/) (or the appropriate port if different)
Make sure to replace `8501` with the correct port number if your application uses a different one.
You will see the following home interface.

![Alt Text](./Documentation/images/Home.png)

## Upload docx/doc file and Apply NER on Chat txt
![Alt Text](/Documentation/images/wordDocProcess.png)

---
![Alt Text](/Documentation/images/NER.png)




## Used Technologies

- **Langages** : Python
- **Frameworks** : FastAPI, Streamlit, Transformers
- **Outils** : Docker, 

---
