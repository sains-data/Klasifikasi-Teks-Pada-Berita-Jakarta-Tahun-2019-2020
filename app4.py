import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Fungsi untuk memuat model dan tokenizer
def load_model_and_tokenizer(model_path, tokenizer_path):
    model = tf.keras.models.load_model(model_path)
    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer

# Fungsi untuk melakukan prediksi
def predict_sentiment(text, tokenizer, model, max_length):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_length, padding='pre', truncating='pre')
    prediction = model.predict(padded)
    return prediction

# Memuat model dan tokenizer (ganti dengan path yang benar)
model, tokenizer = load_model_and_tokenizer("my_model.h5", "tokenizer.pickle")

# Mengatur panjang maksimal berdasarkan training set
max_length = 250  # Contoh, ganti dengan panjang yang sesuai

# Membuat UI dengan Streamlit
st.title('Aplikasi Prediksi Sentimen Berita')

# Define labels
labels = ['NEGATIF', 'NETRAL', 'POSITIF']

# Pilihan input data: Teks atau File CSV/Excel
data_input = st.radio("Pilih jenis input data:", ('Teks', 'File CSV/Excel'))

if data_input == 'Teks':
    # Input teks dari pengguna
    input_text = st.text_area("Masukkan teks berita:")
    
    # Tombol prediksi
    if st.button('Prediksi'):
        if input_text:
            # Melakukan prediksi
            prediction = predict_sentiment(input_text, tokenizer, model, max_length)
            st.write(f"Hasil Prediksi: {labels[np.argmax(prediction)]}")
        else:
            st.write("Silakan masukkan teks berita terlebih dahulu.")

else:
    # Input dari file CSV atau Excel
    uploaded_file = st.file_uploader("Upload file CSV atau Excel", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Membaca data dari file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                st.write("Format file tidak didukung.")
                st.stop()

            # Melakukan prediksi untuk setiap baris data
            predictions = []
            for index, row in df.iterrows():
                text = row['teks']  # Ganti dengan nama kolom teks yang sesuai
                prediction = predict_sentiment(text, tokenizer, model, max_length)
                label = labels[np.argmax(prediction)]
                predictions.append(label)

            # Menambahkan kolom prediksi ke DataFrame
            df['Hasil Prediksi'] = predictions

            # Menampilkan DataFrame hasil prediksi
            st.write("Hasil Prediksi:")
            st.dataframe(df)

        except Exception as e:
            st.write(f"Terjadi kesalahan: {e}")
