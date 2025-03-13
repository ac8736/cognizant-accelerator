from keras._tf_keras.keras.preprocessing.text import Tokenizer
import requests
import re

response = requests.get("https://www.gutenberg.org/files/100/100-0.txt")
text = response.text

def clean_text(text):
    text = text.lower() 
    text = re.sub(r'[^a-zA-Z.,!?; ]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip() 
    return text

text = clean_text(text)

tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts([text])
total_chars = len(tokenizer.word_index) + 1

sequences = tokenizer.texts_to_sequences([text])[0]

import numpy as np

seq_length = 40  
X, y = [], []

for i in range(len(sequences) - seq_length):
    X.append(sequences[i:i+seq_length])  
    y.append(sequences[i+seq_length])   

X, y = np.array(X), np.array(y)

import tensorflow as tf

X = tf.convert_to_tensor(X, dtype=tf.float32)
y = tf.convert_to_tensor(y, dtype=tf.int32)

from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Embedding, LSTM, Dense

model = Sequential([
    Embedding(input_dim=total_chars, output_dim=64, input_length=40),
    LSTM(128, return_sequences=True),
    LSTM(128),
    Dense(total_chars, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.summary()

history = model.fit(X, y, epochs=30, batch_size=64)
model.save("shakespeare_lstm.h5")
