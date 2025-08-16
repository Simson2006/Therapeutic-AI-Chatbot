# Therapist Chatbot

A conversational AI chatbot designed to provide helpful, empathetic, and context-aware responses. The chatbot is trained on therapist-style data and uses natural language processing (NLP) techniques combined with deep learning to understand user queries and provide appropriate responses.

---

## 📝 Project Overview

This project demonstrates how to build a simple AI chatbot that can interact with users like a virtual therapist. The main steps involved in building the chatbot are:

1. **Data Preparation**:  
   The chatbot is trained on a dataset containing therapist-style conversations, including questions, intents, and possible responses.

2. **Text Preprocessing**:  
   Before feeding text to the model, we clean it by:
   - Tokenizing sentences into words
   - Removing stopwords (common words like “the”, “is”)
   - Normalizing text (lowercasing, removing punctuation)

3. **Converting Words to Vectors**:  
   - Text data is converted into numerical vectors using **TF-IDF, CountVectorizer, or Word2Vec**.  
   - This allows the deep learning model to understand patterns in the text.

4. **Model Training**:  
   - A deep learning model (TensorFlow/Keras) is trained to classify user queries into intents.  
   - Each intent corresponds to a type of response the chatbot can provide.

5. **Response Generation**:  
   - Once the model predicts the intent of a user query, the chatbot selects an appropriate response from the dataset.

6. **Web Interface (Streamlit)**:  
   - The chatbot is deployed using **Streamlit** for a simple, interactive web interface.
   - Users can type questions, and the chatbot responds instantly in the browser.

---

## 🎯 Features

- Conversational AI capable of understanding user input in natural language.
- Empathetic and context-aware responses.
- Converts words to vectors using NLP techniques for better understanding.
- Preprocessing includes tokenization, stopwords removal, and text normalization.
- Deep learning model for intent classification.
- Easy-to-use interface built with Streamlit.
- Can be extended with new intents and responses.

---
