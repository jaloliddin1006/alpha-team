
import pickle
MODEL = pickle.load(open("/home/ProLinux/Documents/GitHub/ict-job/user-agent/classifier.pkl",'rb'))

TFDIF = pickle.load(open("/home/ProLinux/Documents/GitHub/ict-job/user-agent/tdif.pkl","rb"))

def classifier(text :str)-> str:
    tfidf = TFDIF.transform([text])
    predicted = MODEL.predict(tfidf)
    return predicted[0]



# print(classifier("marketing"))