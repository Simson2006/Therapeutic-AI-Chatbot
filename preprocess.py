import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import pickle as pkl

lemma= WordNetLemmatizer()
with open(r'D:\Sim_Projects\Personal_Experiments\Chatbot\all_words.pkl','rb') as file:
    all_words=pkl.load(file)

with open(r'D:\Sim_Projects\Personal_Experiments\Chatbot\tags.pkl','rb') as file:
    tags=pkl.load(file)

def bagofwords(tokens, all_words):
    vector = np.zeros(len(all_words), dtype=np.float32)
    for idx, word in enumerate(all_words):
        if word in tokens:
            vector[idx] = 1.0
    return vector


def process_user_query(user_query):
    tokens = word_tokenize(user_query)
    tokens = [lemma.lemmatize(word.lower()) for word in tokens
              if word.isalpha() and word not in stopwords.words('english')]
    bow = bagofwords(tokens, all_words)  # pass tokens list, not joined string
    return bow.reshape(1, -1)
