import re
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
import joblib


model = SentenceTransformer('all-MiniLM-L6-v2')
classifer_model = joblib.load('models/log_classifier.joblib')

def classify_with_bert(log_message):
    model_embeddings = model.encode(log_message)
    probability = classifer_model.predict_proba([model_embeddings])[0]
    print(probability)
    predicted_class = classifer_model.predict([model_embeddings])[0]

    return predicted_class


if __name__ == "__main__":
    # print(classify_with_bert('API returned 404 not found error'))
    # print(classify_with_bert('File uploaded successfully by user sadd'))
    # print(classify_with_bert('Account with ID 2324 created by manga'))
    print(classify_with_bert('Account with ID 2324 created by manga'))