# Klasifikasi Teks Pada Judul Berita Menggunakan Long Short Term Memory (LSTM)
Berita merupakan hal yang senantiasa menjadi salah satu sumber fakta bagi masyarakat. Dalam hal mengklasifikasinya, diperlukan RNN dalam mengautomasi kerjanya. Klasifikasi data berita yang dilakukan berdasarkan isu dan tonalitas (positif, negatif, dan netral) dari berita tersebut. Sumber pengambilan data dilakukan dari Jakarta Open Data (https://data.jakarta.go.id/dataset?tags=Berita). Dengan metode LSTM, akurasinya sampai 90% untuk mengunggah judul berita yang ada. Hal ini menjadikan RNN sebagai alat yang layak untuk mengklasifikasikan berita sesuai isinya.

## Project Overview
Projek ini membahas penggunaan metode Long Short-Term Memory (LSTM) dalam klasifikasi teks untuk mengelompokkan berita berdasarkan isu dan tonalitas. Projek ini menggunakan data berita dari Jakarta Open Data dengan rentang waktu 2019-2020. Pra-pemrosesan data meliputi pelabelan berita, case folding, stopword removal, dan tokenisasi. Pemodelan data dilakukan dengan pembagian data latih dan tes, tokenisasi menggunakan LSTM, dan pengecekan akurasi dan loss.

Projek ini fokus pada klasifikasi berita berdasarkan tonalitas (Negatif, Netral, Positif) dengan menggunakan LSTM. Data pelatihan dibagi menjadi 80% untuk pelatihan dan 20% untuk pengujian. Model jaringan saraf dibangun dengan lapisan embedding, LSTM, dan lapisan dropout. Hasil pelatihan menunjukkan akurasi 93%. Model ini dapat mencapai akurasi terbaik dengan aktivasi Sigmoid dan optimizer Adam.

## Data
Pada tahap perolehan data, dilakukan pengumpulan data berita dari Jakarta Open Data dengan rentang waktu 2019-2020. Data tersebut berisikan informasi berita, tanggal, isu, tonalitas (Positif, Netral, dan Negatif), serta tautan. Tonalitas berita sudah disematkan label sesuai isinya, baik positif, negatif, maupun netral. Data ini menjadi dasar untuk analisis klasifikasi teks menggunakan metode Long Short-Term Memory (LSTM).

## Deployment
Implementasi dari projek ini telah di deploy pada **Streamlit** guna memfasilitasi penggunaan model menjadi lebih interaktif.

### Cara Penggunaan
1. Open link
```
https://klasifikasi-judul-berita.streamlit.app/
```

2. Pilih antara input teks atau input data CSV atau Excel dengan nama kolom 'teks'

3. Klik tombol 'Prediksi'

4. Lihatlah hasil yang ditemukan.

## Tim
Kelompok 5 RA Deep Learning
Anggota :
- Naomi Natasya 120450098
- Bane Rael Sharin 120450101
- Devri Zefanya 120450105
- Rayhan Octianto 120450085

