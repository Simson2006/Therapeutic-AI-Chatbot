import streamlit as st
from preprocess import process_user_query
from tensorflow.keras.models import load_model
import numpy as np
import json
import pickle as pkl
import random
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Only show errors

# Load intents file
with open("intent.json", 'r') as file:
    data1 = json.load(file)
with open("intent.json", 'r') as file:
    data2 = json.load(file)

data = data1
data['intents'].extend(data2['intents'])

# Load trained model
model_dl = load_model('model_dl.h5')

# Load tags
with open("tags.pkl", 'rb') as file:
    tags = pkl.load(file)

# Streamlit UI
st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖Therapeutic AI Assitant")
st.write("Type your message and get a response. Type 'exit' to quit.")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    if user_input.lower() == "exit":
        st.write("Bot: See You!")
    else:
        # Process user input
        bow_input = process_user_query(user_input)
        predicted_prob = model_dl.predict(bow_input)[0]
        predicted_label = np.argmax(predicted_prob)
        predicted_tag = tags[predicted_label]

        # Get response
        response = "Sorry, I didn't get that."
        for intent in data['intents']:
            if intent['tag'] == predicted_tag:
                response = random.choice(intent['responses'])
                response=response.replace('Pandora',"Jarvis")
                break
        
        # Save chat history
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
