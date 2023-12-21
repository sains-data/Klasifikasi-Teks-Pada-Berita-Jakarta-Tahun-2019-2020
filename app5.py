import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import time

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

# Memuat model dan tokenizer
start_time = time.time()
loading_time = time.time() - start_time

def measure_accuracy(model, tokenizer, test_texts, test_labels, max_length):
    predictions = []
    for text in test_texts:
        prediction = predict_sentiment(text, tokenizer, model, max_length)
        label = np.argmax(prediction)
        predictions.append(label)

    # Menghitung akurasi
    accuracy = np.mean(np.array(predictions) == np.array(test_labels))
    return accuracy

# Membuat UI dengan Streamlit
st.title('Aplikasi Prediksi Sentimen Judul Berita')

# Define labels
labels = ['NEGATIF', 'NETRAL', 'POSITIF']

# Pilihan input data: Teks atau File CSV/Excel
data_input = st.radio("Pilih jenis input data:", ('Teks', 'Berkas CSV/Excel'))

if data_input == 'Teks':
    # Input teks dari pengguna
    input_text = st.text_area("Masukkan teks berita:")
    
    # Tombol prediksi
    if st.button('Prediksi'):
        if input_text:
            start_prediction_time = time.time()  # Waktu awal prediksi
            # Melakukan prediksi
            prediction = predict_sentiment(input_text, tokenizer, model, max_length)
            end_prediction_time = time.time()  # Waktu akhir prediksi
            prediction_time = end_prediction_time - start_prediction_time  # Waktu prediksi
            
            # Menampilkan hasil prediksi dan confidence score
            predicted_label = labels[np.argmax(prediction)]
            st.write(f"Hasil Prediksi: {predicted_label}")
            st.write(f"Waktu prediksi: {prediction_time:.2f} detik")
            
            # Menampilkan confidence score untuk setiap kelas sentimen
            confidence_scores = {label: f"{prediction[0][i]*100:.2f}%" for i, label in enumerate(labels)}
            st.write("Confidence Score:")
            st.write(confidence_scores)
        else:
            st.write("Silakan masukkan judul berita terlebih dahulu.")


# ... (bagian kode lainnya tetap sama)

else:
    # Input dari file CSV atau Excel
    uploaded_file = st.file_uploader("Unggah berkas CSV atau Excel", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Membaca data dari file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                st.write("Format berkas tidak mendukung.")
                st.stop()

            # Melakukan prediksi untuk setiap baris data
            predictions = []
            confidence_scores_list = []  # Menyimpan kepercayaan untuk setiap baris data
            start_prediction_time = time.time()  # Waktu awal prediksi
            for index, row in df.iterrows():
                text = row['teks']  # Ganti dengan nama kolom teks yang sesuai
                prediction = predict_sentiment(text, tokenizer, model, max_length)
                label = labels[np.argmax(prediction)]
                predictions.append(label)

                # Menghitung confidence score untuk setiap kelas sentimen
                confidence_scores = {label: f"{prediction[0][i]*100:.2f}%" for i, label in enumerate(labels)}
                confidence_scores_list.append(confidence_scores)

            # Menambahkan kolom prediksi dan kepercayaan ke DataFrame
            df['Hasil Prediksi'] = predictions
            for idx, label in enumerate(labels):
                df[f'Confidence {label}'] = [scores[label] for scores in confidence_scores_list]

            # Menampilkan DataFrame hasil prediksi
            st.write("Hasil Prediksi:")
            st.dataframe(df)

            # Menghitung dan menampilkan waktu prediksi
            end_prediction_time = time.time()  # Waktu akhir prediksi
            prediction_time = end_prediction_time - start_prediction_time  # Waktu prediksi
            st.write(f"Waktu prediksi: {prediction_time:.2f} detik")

            # Menghitung akurasi jika kolom label ada dalam DataFrame
            if 'labels' in df.columns:
                test_texts = df['teks'].tolist()  # Menggunakan teks dari DataFrame untuk pengujian
                test_labels = df['labels'].tolist()  # Ganti dengan nama kolom label yang sesuai
                accuracy = measure_accuracy(model, tokenizer, test_texts, test_labels, max_length)
            
        except Exception as e:
            st.write(f"Terjadi kesalahan: {e}")

