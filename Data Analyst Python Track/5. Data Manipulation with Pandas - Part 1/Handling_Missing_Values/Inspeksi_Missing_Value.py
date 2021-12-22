# Value yang hilang/tidak lengkap dari dataframe akan membuat analisis atau
# model prediksi yang dibuat menjadi tidak akurat dan mengakibatkan keputusan salah yang diambil.
# Terdapat beberapa cara untuk mengatasi data yang hilang/tidak lengkap tersebut.

# Data COVID-19 yang akan digunakan ini diambil dari google big query,
# tetapi sudah disediakan datasetnya dalam format csv dengan nama "public data covid19 jhu csse eu.csv".
# Ini adalah studi kasus untuk meng-handle missing value. Bagaimanakah langkah-langkahnya?

# Di pandas data yang hilang umumnya direpresentasikan dengan NaN.

import pandas as pd
# Baca file "public data covid19 jhu csse eu.csv"
df = pd.read_csv(
    "CHAPTER+4+-+missing+value+-+public+data+covid19+.csv")

# Langkah pertama, harus tahu kolom mana yang terdapat data hilang dan berapa banyak dengan cara:
# Cara 1: menerapkan method .info() pada dataframe yang dapat diikuti dari kode berikut ini
# Cetak info dari df
print(df.info())

# Cara 2: mengetahui berapa banyak nilai hilang dari tiap kolom di dataset
# tersebut dengan menerapkan chaining method pada dataframe yaitu .isna().sum().
# Method .isna() digunakan untuk mengecek berapa data yang bernilai NaN dan .sum()
# menjumlahkannya secara default untuk masing-masing kolom dataframe.
# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)

# Seperti kedua output di atas, artinya ada beberapa kolom yang ada null sebagian
# dan ada yang nilainya null semua untuk kolomnya.

# Dataset : https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/CHAPTER+4+-+missing+value+-+public+data+covid19+.csv
