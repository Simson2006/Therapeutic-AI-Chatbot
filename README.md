# Therapist Chatbot

A conversational AI chatbot designed to provide helpful, empathetic, and context-aware responses. The chatbot is trained on therapist-style data and uses natural language processing (NLP) techniques combined with deep learning to understand user queries and provide appropriate responses.

---

## 📝 Project Overview

This project demonstrates how to build a simple AI chatbot that can interact with users like a virtual therapist or answer college-related questions. The main steps involved are:

1. **Data Preparation**:  
   - The chatbot is trained on datasets:
     - `intent.json` → Therapy-related conversations
     - `intents.json` → College-related questions and intents

2. **Text Preprocessing**:  
   - Clean and prepare text data:
     - Tokenization (splitting sentences into words)
     - Removing stopwords
     - Normalization (lowercasing, removing punctuation)

3. **Converting Words to Vectors**:  
   - Text data is converted into numerical vectors using **TF-IDF, CountVectorizer, or Word2Vec**.  
   - Vectorization allows the deep learning model to understand and learn patterns from the text.

4. **Model Training**:  
   - A deep learning model (`model_dl.h5`) is trained using the processed dataset.
   - `chatbot_model_training.ipynb` notebook is used for creating and training this model.

5. **Response Generation**:  
   - Once the model predicts the intent of a user query, the chatbot selects an appropriate response from the dataset.

6. **Web Interface (Streamlit)**:  
   - `app.py` contains the **Streamlit app** for the chatbot interface.
   - Users can type questions, and the chatbot responds instantly in the browser.

7. **Preprocessing New Queries**:  
   - `preprocess.py` module processes new text entered by the user:
     - Tokenizes and cleans the input
     - Converts words to vectors using the saved vectorizer
     - Prepares data for the model to predict the intent

---

## 🗂 File Overview

| File Name | Purpose |
|-----------|---------|
| `all_words.pkl` | Contains all words from the dataset for indexing and vectorization. |
| `tags.pkl` | Contains all intent tags from the dataset for mapping predictions to responses. |
| `model_dl.h5` | Trained deep learning model for intent classification. |
| `intent.json` | Therapy-related dataset for training. |
| `intents.json` | Someother related dataset for training.(for training with more words)|
| `chatbot_model_training.ipynb` | Jupyter notebook used to create and train the deep learning model. |
| `app.py` | Streamlit app file that runs the interactive chatbot interface. |
| `preprocess.py` | Module to preprocess and vectorize new user input before passing it to the model. |
| `utils/` | Helper scripts for preprocessing, tokenization, and other functions. |

---

## 🎯 Features

- Conversational AI for therapy and college-related queries.
- Converts words to vectors using NLP techniques (TF-IDF, CountVectorizer, Word2Vec).
- Preprocessing includes tokenization, stopwords removal, and text normalization.
- Deep learning model for intent classification.
- Interactive Streamlit interface for real-time chatting.
- Easily extendable with new intents and datasets.

---
