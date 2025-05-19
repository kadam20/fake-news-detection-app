from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import re
import string

# Load the SVM model
model = joblib.load('svm_model.pkl')

# Function to detect fake news
def detect_fake_news(input_text):
    input_text = [input_text] 
    text = clean_text(input_text)
    vectorize_text = vectorize_text(text)
    prediction = model.predict(vectorize_text)
    value = model.predict_proba(vectorize_text)
    return prediction[0], value[0][1]
    

# Function to remove punctuations from text
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

# Function to clean text data
def clean_text(text):
    text = text.lower()
    text = remove_punctuations(text)
    text = re.sub(r'\b[A-Z]+\b', '') 
    text = re.sub(r'http\S+|www\.\S+', '')
    text.replace('(Reuters) -', '') 
    text.replace('-', ' ')  
    return text

# Function to vectorize text data
def vectorize_text(text):
    text = clean_text(text)
    vectorized_text = model['tfidf'].transform([text])
    return vectorized_text
