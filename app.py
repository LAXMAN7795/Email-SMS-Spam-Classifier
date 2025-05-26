import nltk
import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import warnings
warnings.filterwarnings('ignore')

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter your message:")

def trasform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text) #splitting words where space

  new_text = []
  for i in text:
    if i.isalnum():
      new_text.append(i) #removing special charecter

  text = new_text[:]
  new_text.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation: #remove punctuations
      new_text.append(i)

  text = new_text[:]
  new_text.clear()

  for i in text:
    new_text.append(ps.stem(i))# stemming

  return " ".join(new_text)
trasform_text('did you know the new iPhone is so awesome')

if st.button('Predict'):
  # Preprocess
  transformed_sms = trasform_text(input_sms)
  # Vectorize
  vector_input = tfidf.transform([transformed_sms])
  # Predict
  result = model.predict(vector_input)[0]
  # Display
  if result == 1:
    st.header("Spam")
  else:
    st.header("Not Spam")