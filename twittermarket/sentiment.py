import pandas as pd
from keras.models import load_model
import time 
from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences 
from gensim.models import Word2Vec 
import pickle

# nltk
import nltk
from nltk.corpus import stopwords
from  nltk.stem import SnowballStemmer

# Word2vec
import gensim

# Utility
import re
import numpy as np
import os
from collections import Counter
import logging
import time
import pickle
import itertools


def run(file_len):

    nltk.download('stopwords')

    # DATASET
    DATASET_COLUMNS = ["ids", "date", "user", "text"]
    DATASET_ENCODING = "ISO-8859-1"
    # TEXT CLENAING
    TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

    #Providing the path of our products.csv(coffee,wine,snacks)
    dataset_path="./products.csv"
    print("Open file:", dataset_path)
    df = pd.read_csv(dataset_path, encoding =DATASET_ENCODING , names=DATASET_COLUMNS)

    stop_words = stopwords.words("english")
    stemmer = SnowballStemmer("english")

    def preprocess(text, stem=False):
        # Remove link,user and special characters
        text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
        tokens = []
        for token in text.split():
            if token not in stop_words:
                if stem:
                    tokens.append(stemmer.stem(token))
                else:
                    tokens.append(token)
        return " ".join(tokens)

        
    df.text = df.text.apply(lambda x: preprocess(x))
    # df.text DATA AFTER CLEANING

    w2v_model = Word2Vec.load('./ml/model.w2v')
    model = load_model('./ml/model.h5')
    
    with open('./ml/tokenizer.pkl', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    with open('./ml/encoder.pkl', 'rb') as handle:
        encoder = pickle.load(handle)
        
        
    SEQUENCE_LENGTH = 300
    EPOCHS = 8
    BATCH_SIZE = 1024
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    SENTIMENT_THRESHOLDS = (0.4, 0.7)


    def decode_sentiment(score, include_neutral=True):
        if include_neutral:
            label = NEUTRAL
            if score == SENTIMENT_THRESHOLDS[1]:
                label = POSITIVE
                return label
            else:
                return NEGATIVE if score < 0.5 else POSITIVE

        
    def predict(text, include_neutral=True):
        start_at = time.time()
        x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
        score = model.predict([x_test])[0]
        label = decode_sentiment(score, include_neutral=include_neutral)
        return {"label": label, "score": float(score)}
    
    
    predict("I love coffee")

    l=[]
    for x in range(file_len):
        a=predict(df.text[x])
        l.append(a)
    
    
    return l     
