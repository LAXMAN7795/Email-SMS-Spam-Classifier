**Email/SMS Spam Classifier**

A powerful and intuitive web application that detects whether a given message is **Spam** or **Not Spam** 
using Natural Language Processing (NLP) and a trained machine learning model. Built with Python, Streamlit, and NLTK, it's lightweight, fast, and user-friendly.

Features
✅ Classifies messages as **Spam** or **Not Spam**  
✅ Real-time prediction via Streamlit UI  
✅ Pre-trained ML model using **TF-IDF Vectorizer** and **Multinomial Naive Bayes**  
✅ Text preprocessing: lowercasing, stopword removal, punctuation stripping, stemming  
✅ Clean, minimal, and responsive interface

Tech Stack
- **Frontend:** Streamlit
- **Backend/NLP:** Python, NLTK, Scikit-learn
- **Model:** TF-IDF + Multinomial Naive Bayes (Pickled)

How It Works
1. User enters a message
2. Text is preprocessed:
   - Lowercasing
   - Tokenization
   - Removing punctuation and stopwords
   - Stemming
3. Transformed text is vectorized using TF-IDF
4. Model predicts whether it's spam or not

🧠 Model Training
The model was trained on a labeled dataset (e.g., SMS Spam Collection) using the following pipeline:
Preprocessing: lowercase, remove stopwords/punctuation, stemming
Feature Extraction: TF-IDF Vectorizer
Classification: Multinomial Naive Bayes

🌍 Future Enhancements
Deploy live on Streamlit Cloud or Heroku
Add confusion matrix and accuracy metrics
Dark mode UI option
Upload CSV support for bulk prediction
Mobile responsiveness

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

