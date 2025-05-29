📩 Spam Message Classifier – Email/SMS Spam Detection
A machine learning-based web application that classifies messages as Spam or Not Spam, using NLP techniques and deployed via Streamlit.

🚀 Demo
Try it locally to enter a message and see real-time classification.

📁 Dataset
Source: SMS Spam Collection Dataset
The dataset contains 5,500+ SMS messages labeled as ham (not spam) or spam.

| v1     | v2                              |
|--------|---------------------------------|
| ham    | Go until jurong point...        |
| spam   | WINNER!! As a valued network... |

Column v1 renamed to target and v2 to text
Target labels encoded: ham → 0, spam → 1

🧹 Text Preprocessing
Using NLTK, the following transformations were applied:
Lowercasing
Tokenization
Removing punctuation and stopwords
Stemming using PorterStemmer
Feature Engineering:
num_characters – total characters in message
num_words – total words
num_sentences – number of sentences

📊 Vectorization
Used TF-IDF Vectorizer from sklearn.feature_extraction.text

🧠 Model Building
Tested multiple classifiers from sklearn.naive_bayes:
GaussianNB
BernoulliNB
✅ MultinomialNB (selected)
⚙️ Evaluation Metrics
Used:
accuracy_score
confusion_matrix
precision_score
📈 MultinomialNB gave the best results in both accuracy and precision.

🖥️ Streamlit App
UI created using Streamlit
User inputs a message → Model classifies it in real time

💾 Model Deployment
Trained model and vectorizer saved using pickle
Easily reloadable for deployment.

🛠 Tech Stack
Tool/Library	         Purpose
Python	               Programming Language
NLTK	                  Text Preprocessing
scikit-learn	         ML Modeling & Evaluation
Pandas/NumPy	         Data Handling
Streamlit	            UI for Model Deployment
Pickle	               Model Serialization

Results:
1.Not Spam
![image alt](https://github.com/LAXMAN7795/Email-SMS-Spam-Classifier/blob/d6c292480c8e55a866a6f9b766db9a0505384ac1/EmalNotSpam.png)
2.Spam
![image alt](https://github.com/LAXMAN7795/Email-SMS-Spam-Classifier/blob/539c8d5f123ab966e4f2da54d0ed41f37bca6eac/EmailSpam.png)
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

