import pickle
import os
# base dir 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
MODEL = pickle.load(open(BASE_DIR+"/classifier.pkl",'rb'))

TFDIF = pickle.load(open(BASE_DIR+"/tdif.pkl","rb"))

def classifier(text :str)-> str:
    tfidf = TFDIF.transform([text])
    predicted = MODEL.predict(tfidf)
    return predicted[0]