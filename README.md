# 📩 Spam Message Classifier – Email/SMS Spam Detection

A machine learning-based web application that classifies messages as **Spam** or **Not Spam** using NLP techniques. The app is deployed using Streamlit for real-time predictions.

---

## 🚀 Live Demo
👉 [Click here to try the app](https://email-sms-spam-classifier-mjxewlb6rvsxaofryhwjjj.streamlit.app/)

---

## 📁 Dataset
- Source: SMS Spam Collection Dataset  
- Contains 5,500+ labeled messages  

| Label | Message |
|------|--------|
| ham | Go until jurong point... |
| spam | WINNER!! As a valued network... |

- Renamed columns:
  - `v1 → target`
  - `v2 → text`
- Encoding:
  - ham → 0  
  - spam → 1  

---

## 🧹 Text Preprocessing
Performed using NLTK:
- Lowercasing  
- Tokenization  
- Removing punctuation & stopwords  
- Stemming using PorterStemmer  

### 📊 Feature Engineering
- `num_characters`
- `num_words`
- `num_sentences`

---

## 📊 Vectorization
Used **TF-IDF Vectorizer** from `sklearn.feature_extraction.text`

---

## 🧠 Model Building
Tested multiple classifiers:
- GaussianNB  
- BernoulliNB  
- ✅ MultinomialNB (Best performing)

---

## ⚙️ Evaluation Metrics
- Accuracy Score  
- Precision Score  
- Confusion Matrix  

👉 MultinomialNB performed best in both accuracy and precision.

---

## 🖥️ Streamlit App
- Built using Streamlit  
- User inputs message → Model predicts spam/not spam in real-time  

---

## 💾 Model Deployment
- Model and vectorizer saved using `pickle`  
- Loaded in Streamlit app for predictions  

---

## 🛠 Tech Stack

| Tool | Purpose |
|-----|--------|
| Python | Programming |
| NLTK | Text preprocessing |
| scikit-learn | ML modeling |
| Pandas / NumPy | Data handling |
| Streamlit | Web app |
| Pickle | Model saving |

---

## 📸 Results

### ✅ Not Spam
![Not Spam](https://github.com/LAXMAN7795/Email-SMS-Spam-Classifier/blob/d6c292480c8e55a866a6f9b766db9a0505384ac1/EmalNotSpam.png)

### 🚨 Spam
![Spam](https://github.com/LAXMAN7795/Email-SMS-Spam-Classifier/blob/539c8d5f123ab966e4f2da54d0ed41f37bca6eac/EmailSpam.png)

---

## 🔮 Future Improvements
- Add deep learning models (LSTM)
- Deploy as REST API
- Improve UI/UX

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
