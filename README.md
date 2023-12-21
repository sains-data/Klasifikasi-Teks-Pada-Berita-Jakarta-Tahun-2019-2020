
# (Indonesia - English)
# (ID) Klasifikasi Teks Pada Judul Berita Menggunakan Long Short Term Memory (LSTM)
Berita merupakan hal yang senantiasa menjadi salah satu sumber fakta bagi masyarakat. Dalam hal mengklasifikasinya, diperlukan RNN dalam mengautomasi kerjanya. Klasifikasi data berita yang dilakukan berdasarkan isu dan tonalitas (positif, negatif, dan netral) dari berita tersebut. Sumber pengambilan data dilakukan dari Jakarta Open Data (https://data.jakarta.go.id/dataset?tags=Berita). Dengan metode LSTM, akurasinya sampai 90% untuk mengunggah judul berita yang ada. Hal ini menjadikan RNN sebagai alat yang layak untuk mengklasifikasikan berita sesuai isinya.

## Deskripsi Proyek
Proyek ini membahas penggunaan metode Long Short-Term Memory (LSTM) dalam klasifikasi teks untuk mengelompokkan berita berdasarkan isu dan tonalitas. Proyek ini menggunakan data berita dari Jakarta Open Data dengan rentang waktu 2019-2020. Praproses data meliputi pelabelan berita, _case folding_, _stopword removal_, dan tokenisasi. Pemodelan data dilakukan dengan pembagian data latih dan tes, tokenisasi menggunakan LSTM, dan pengecekan akurasi dan _loss_.

Proyek ini fokus pada klasifikasi berita berdasarkan tonalitas (Negatif, Netral, Positif) dengan menggunakan LSTM. Data pelatihan dibagi menjadi 80% untuk pelatihan dan 20% untuk pengujian. Model jaringan saraf dibangun dengan lapisan _embedding_, LSTM, dan lapisan _dropout_. Hasil pelatihan menunjukkan akurasi 93%. Model ini dapat mencapai akurasi terbaik dengan aktivasi Sigmoid dan _optimizer_ Adam.

## Data
Pada tahap perolehan data, dilakukan pengumpulan data berita dari Jakarta Open Data dengan rentang waktu 2019-2020. Data tersebut berisikan informasi berita, tanggal, isu, tonalitas (Positif, Netral, dan Negatif), serta tautan. Tonalitas berita sudah disematkan label sesuai isinya, baik positif, negatif, maupun netral. Data ini menjadi dasar untuk analisis klasifikasi teks menggunakan metode _Long Short-Term Memory_ (LSTM).

## Penerapan
Implementasi dari proyek ini telah diterapkan pada **Streamlit** guna memfasilitasi penggunaan model menjadi lebih interaktif.

![ezgif com-animated-gif-maker](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/0fde50b9-4bb0-45be-863a-620050e63065)


### Cara Penggunaan
1. Buka Tautan
```
https://klasifikasi-judul-berita.streamlit.app/
```

2. Pilih antara input teks atau input data CSV atau Excel dengan nama kolom 'teks'




![Pemilihan Mode](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/d6721a4e-f3ef-4d99-9952-668189365e22)





3. Klik tombol 'Prediksi'



![Pemencetan Prediksi](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/667f11b4-12ac-4e1d-89c5-aae2d4b6b26e)


4. Lihatlah hasil yang ditemukan.


![Hasil Penginputan](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/970c167b-9e05-4f6a-bc50-7b55cc714653)

### Tips: Pastikan kepala kolom bernamakan "teks" dan bukan kata lain. Jangan lupa untuk menghapus tanda koma (,) pada _dataset_ Excelnya sebelum diinput.

# (EN) Text Classification on News Headlines Using Long Short Term Memory (LSTM)
News is something that has always been one of the sources of facts for society. In terms of classifying it, RNN is needed to automate its work. The classification of news data is based on the issue and tonality (positive, negative, and neutral) of the news. The source of data collection is from Jakarta Open Data (https://data.jakarta.go.id/dataset?tags=Berita). With the LSTM method, the accuracy is up to 90% for uploading existing news titles. This makes RNN a viable tool for classifying news according to its content.

## Project Overview
This project discusses the use of Long Short-Term Memory (LSTM) method in text classification to categorise news based on issues and tonality. This project uses news data from Jakarta Open Data with a time span of 2019-2020. Data pre-processing includes news labelling, case folding, stopword removal, and tokenisation. Data modelling is done by dividing training and test data, tokenisation using LSTM, and checking accuracy and loss.

## Data
In the data acquisition stage, news data was collected from Jakarta Open Data with a time span of 2019-2020. The data contains news information, date, issue, tonality (Positive, Neutral, and Negative), and link. News tonality has been labelled according to its content, either positive, negative, or neutral. This data is the basis for text classification analysis using the Long Short-Term Memory (LSTM) method.

## Deployment
The implementation of this project has been deployed on **Streamlit** to facilitate more interactive use of the model.

## How to Use
1. Open link
```
https://klasifikasi-judul-berita.streamlit.app/
```

2. Choose between text input or CSV or Excel data input with column name 'text'




![Pemilihan Mode](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/d6721a4e-f3ef-4d99-9952-668189365e22)





3. Click on "Prediksi" Button.



![Pemencetan Prediksi](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/667f11b4-12ac-4e1d-89c5-aae2d4b6b26e)


4. Look at the results found.


![Hasil Penginputan](https://github.com/sains-data/Klasifikasi-Teks-Pada-Judul-Berita/assets/105734822/970c167b-9e05-4f6a-bc50-7b55cc714653)

### Tips: Make sure the column head is "text" and not other words. Don't forget to remove the comma (,) in the Excel _dataset_ before inputting.



## Tim
Kelompok 5 RA Deep Learning
Anggota :
- Naomi Natasya 120450098
- Bane Rael Sharin 120450101
- Devri Zefanya 120450105
- Rayhan Octianto 120450085

