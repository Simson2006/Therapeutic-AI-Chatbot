# Therapist Chatbot

A conversational AI chatbot designed to provide helpful, empathetic, and context-aware responses. The chatbot is trained on therapist-style data and uses natural language processing (NLP) techniques combined with a **deep learning model (ANN)** to understand user queries and provide appropriate responses.

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
   - Text is converted into numerical vectors using a **Bag of Words (BoW) implementation**, allowing the ANN model to process and understand the input.

4. **Model Training (ANN)**:  
   - A deep learning **Artificial Neural Network (ANN)** is trained to classify user queries into intents.  
   - The model achieves **about 90% accuracy** on the training and validation datasets.  
   - Training is done in `chatbot_model_training.ipynb`.

5. **Response Generation**:  
   - Once the ANN predicts the intent of a user query, the chatbot selects an appropriate response from the dataset.

6. **Web Interface (Streamlit)**:  
   - `app.py` contains the **Streamlit app** for the chatbot interface.  
   - Users can type questions, and the chatbot responds instantly in the browser.

7. **Preprocessing New Queries**:  
   - `preprocess.py` module processes new text entered by the user:
     - Cleans and tokenizes the input
     - Converts it into a vector using **Bag of Words**
     - Prepares data for the ANN to predict the intent

---

## 🗂 File Overview

| File Name | Purpose |
|-----------|---------|
| `all_words.pkl` | Contains all words from the dataset for indexing and vectorization. |
| `tags.pkl` | Contains all intent tags from the dataset for mapping predictions to responses. |
| `model_dl.h5` | Trained **ANN deep learning model** for intent classification (~90% accuracy). |
| `intent.json` | Therapy-related dataset for training. |
| `intents.json` | College-related dataset for training. |
| `chatbot_model_training.ipynb` | Jupyter notebook used to create and train the ANN model. |
| `app.py` | Streamlit app file that runs the interactive chatbot interface. |
| `preprocess.py` | Module to preprocess and vectorize new user input using **Bag of Words** before passing it to the model. |
| `utils/` | Helper scripts for preprocessing, tokenization, and other functions. |

---

## 🎯 Features

- Conversational AI for therapy and college-related queries.
- Converts words to vectors manually using **Bag of Words (BoW)**.
- **Artificial Neural Network (ANN)** for intent classification with ~90% accuracy.
- Preprocessing includes tokenization, stopwords removal, and text normalization.
- Interactive Streamlit interface for real-time chatting.
- Easily extendable with new intents and datasets.
