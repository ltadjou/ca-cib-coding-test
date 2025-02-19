import spacy
from spacy.matcher import Matcher
import re
from transformers import pipeline

nlp=spacy.load('en_core_web_trf')
matcher = Matcher(nlp.vocab)

# Regular expressions for financial information
money_pattern = r'\$\d+(\.\d{2})?'  # Matches dollar amounts, e.g., $50, $50.25
percentage_pattern = r'\b\d+(\.\d+)?%'  # Matches percentages, e.g., 10%, 10.5%
from flair.models import SequenceTagger
from flair.data import Sentence

text = """11:49:05 I'll revert regarding BANK ABC to try to do another 200 mio at 2Y
FR001400QV82	AVMAFC FLOAT	06/30/28
offer 2Y EVG estr+45bps
estr average Estr average / Quarterly interest payment"""
tagger = SequenceTagger.load("flair/ner-english")

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

if __name__ == "__main__":

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(text)
    print(ner_results)
    exit()

    # Process the text with SpaCy
    doc = nlp(text.lower())

    # Extract named entities
    financial_entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Print the results
    # print("Money Matches:", money_matches)
    # print("Percentage Matches:", percentage_matches)
    print("Financial Entities:", financial_entities)
    exit()

    ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
    results = ner_pipeline(text.lower())
    print(results)
    
    
    
    sentence = Sentence(text.lower())
    tagger.predict(sentence)
    print(sentence.to_tagged_string())
    exit()

   

     # Find matches using regular expressions
    money_matches = re.findall(money_pattern, text)
    percentage_matches = re.findall(percentage_pattern, text)
    
    

    
    

    

    text = "BlackRock Innovation and Growth Trust (BIGZ) will begin trading ex-dividend on November 12, 2021. A cash dividend payment of $0.1 per share is scheduled to be paid on November 30, 2021. Shareholders who purchased BIGZ prior to the ex-dividend date are eligible for the cash dividend payment. This marks the 6th quarter that BIGZ has paid the same dividend. At the current stock price of $17.99, the dividend yield is 6.67%."
    
   

    