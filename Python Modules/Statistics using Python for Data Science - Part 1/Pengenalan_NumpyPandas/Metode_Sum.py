# Biasanya pada awal mula sebelum melakukan pengolahan data,
# kita memanggil library yang diinginkan untuk digunakan dalam analisa data,
# dalam hal ini kita akan memuat numpy dan pandas.

# memuat numpy sebagai np
import numpy as np

# memuat pandas sebagai pd
import pandas as pd

# Pada tahap pertama ketika ingin menganalisa data,
# kita biasanya memuat data yang disimpan di salah satu folder
# untuk dimuat ke IDE atau interactive notebook seperti Jupyter.
# Untuk memuat data dalam format csv kita dapat menggunakan method .read_csv() dari pandas

# memuat data bernama 'dataset_statistics.csv' dan memasukkan hasilnya ke dalam 'raw_data'
raw_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')


# Untuk melihat keseluruhan data cukup memanggil nama variabelnya dengan fungsi :
print(raw_data)
# melihat 10 data pada baris pertama
print(raw_data.head(10))
# melihat 5 data pada baris terakhir
print(raw_data.tail())


# Berapa banyak baris data dan fitur yang dataset punya?
# Untuk melihat dimensi dari data kita dapat menggunakan method shape :
# melihat dimensi dari raw_data
print(raw_data.shape)
# Sehingga untuk mengambil jumlah data, kita bisa mengambil nilai shape pada indeks ke 0
# mengambil jumlah data
print(raw_data.shape[0])


# Kolom apa saja yang terdapat dalam dataset?
# Untuk melihat kolom apa saja yang terdapat pada dataset cukup menggunakan method columns:
print(raw_data)
print(raw_data.columns)


# Ada berapa banyak data yang hilang dari dataset?
# Untuk melihat data dari dataset bisa menggunakan method isna:
print(raw_data.isna())

# Nilai kolom akan bernilai False jika tidak terdapat nilai na dan akan bernilai True jika sebaliknya.

# Untuk menghitung jumlah data yang hilang dari dataset, bisa menggabungkan method isna dengan method sum:
print(raw_data.isna().sum())


# Untuk bisa melihat ringkasan dari data misalnya rerata, jumlah, nilai maksimum-minimum dan ukuran lainnya.
# Kita dapat menggunakan method .describe():
print(raw_data.describe())

# Selain itu terdapat beberapa fungsi yang umumnya dipakai dalam analisa data, diantaranya adalah:
# Mencari nilai maksimum dengan method .max() dan nilai minimum dengan method .min()

# Mencari nilai maksimum dari tiap kolom
raw_data.max()

# Mencari nilai maksimum dari kolom 'Harga'
raw_data['Harga'].max()

# Mencari nilai minimum dari kolom 'Harga'
raw_data['Harga'].min()


# Jumlah dari semua nilai pada kolom dengan method .sum() agar menghasilkan :
# menghitung jumlah dari semua kolom
print(raw_data.sum())

# menghitung jumlah dari semua kolom bertipe data numerik saja
raw_data.sum(numeric_only=True)

# menghitung jumlah dari kolom 'Harga' dan 'Pendapatan'
raw_data[['Harga', 'Pendapatan']].sum()
