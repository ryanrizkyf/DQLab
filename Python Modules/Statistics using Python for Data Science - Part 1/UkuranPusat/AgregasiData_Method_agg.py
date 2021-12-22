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


# Terkadang kita hanya ingin melakukan analisa sebagian kecil dari data atau hanya beberapa kolom saja,
# untuk itu kita dapat melakukan slice-and-dice pada data yang kita punya.

# Untuk memilih kolom untuk dianalisa,
# kita dapat memanggil objek dataframe yang sudah dibuat
# dan menggunakan tanda ['nama_kolom'] untuk memilih satu kolom
# atau [['nama_kolom_1', 'nama_kolom_2', ..., 'nama_kolom_n']] untuk memilih lebih dari 1 kolom.

# Memilih kolom 'Pendapatan' saja
print(raw_data['Pendapatan'])

# Memilih kolom 'Jenis Kelamin' dan 'Pendapatan'
print(raw_data[['Jenis Kelamin', 'Pendapatan']])


# Untuk memilih baris, kita dapat menggunakan [m:n] untuk mengambil baris data ke-m sampai ke-(n-1)
# atau bisa juga menggunakan method loc untuk pemilihan baris yang lebih spesifik.

# mengambil data dari baris ke-0 sampai baris ke-(10-1) atau baris ke-9
print(raw_data[:10])

# mengambil data dari baris ke-3 sampai baris ke-(5-1) atau baris ke-4
print(raw_data[3:5])

# mengambil data pada baris ke-1, ke-3 dan ke-10
print(raw_data.loc[[1, 3, 10]])

# Kita juga dapat melakukan pemilihan kolom dan baris secara bersamaan
# Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dan ambil baris ke-1 sampai ke-9
print(raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])

# Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dan ambil baris ke-1, ke-10 dan ke-15
print(raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1, 10, 15]])


# Rata-rata atau mean adalah salah satu ukuran pusat yang nilainya diperoleh dengan cara
# menjumlahkan semua nilai titik data yang ada lalu dibagi oleh jumlah data.

# Secara matematis hal ini dapat dirumuskan sebagai berikut:
# Lihat gambar pada file RataRata_Mean.png
# Dimana:
# x¯ adalah rerata
# x1,x2,...,xn adalah titik data
# n adalah jumlah data

# Kita dapat menghitung nilai rata-rata menggunakan method .mean() pada numpy atau pandas
# mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']

# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print(produk_A['Pendapatan'].mean())

# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print(np.mean(produk_A['Pendapatan']))


# Median adalah salah satu ukuran pusat yang nilainya terletak di tengah titik data.
# Sebagai gambaran, jika kita memiliki titik data bernilai 1, 2, 3, 4, 4, 5, 6
# maka median dari sekumpulan titik data tersebut adalah 4.

# Namun jika kita memiliki titik data bernilai 1, 2, 3, 3
# maka media dari sekumpulan titik data tersebut adalah:
# Lihat gambar pada file Median.png

# Kita dapat menemukan nilai median dengan menggunakan method .median() pada numpy maupun pandas
print(raw_data)
# Hitung median dari pendapatan menggunakan pandas
print(produk_A['Pendapatan'].median())

# Hitung median dari pendapatan menggunakan numpy
print(np.median(produk_A['Pendapatan']))


# Modus didefinisikan sebagai data yang memiliki frekuensi kemunculan terbanyak/terbesar.
# Sebagai contoh, jika terdapat titik data seperti berikut: 1, 1, 1, 1, 2, 3, 3, 4
# maka modus dari data tersebut adalah 1 karena 1 muncul sebanyak 4 kali,
# lebih banyak dibanding titik data lainnya.

# Kita dapat menggunakan method .count_values() pada pandas
# Melihat jumlah dari masing-masing produk
print(raw_data['Produk'].value_counts())


# Kuantil adalah nilai-nilai data yang membagi data,
# yang telah diurutkan sebelumnya menjadi beberapa bagian yang sama besar ukurannya.

# Beberapa ukuran fraktil ini diantaranya adalah:
# Kuartil: Adalah kuantil yang membagi data menjadi empat bagian sama besar.
# Kuartil ke-2 dari adalah median dari data tersebut.
# Desil: Adalah kuantil yang membagi data menjadi 10 bagian sama besar.
# Persentil: Adalah kuantil yang membagi data menjadi 100 bagian sama besar.

# Untuk mencari fraktil dari data, kita dapat menggunakan method .quantile dari pandas atau numpy
# mencari median atau 50% dari data menggunakan pandas
print(raw_data['Pendapatan'].quantile(q=0.5))

# mencari median atau 50% dari data menggunakan pandas
print(np.quantile(raw_data['Pendapatan'], q=0.5))


# Ada kalanya kita ingin menghitung sekaligus beberapa ukuran,
# misalnya menghitung nilai mean sekaligus menghitung nilai median.
# Kita dapat melakukan kedua hal tersebut dengan menggunakan method .agg() pada objek pandas.

# menghitung rerata dan median usia (age) dan insulin (insu)
print(raw_data[['Pendapatan', 'Harga']].agg([np.mean, np.median]))

# menghitung rerata dan median Pendapatan dan Harga dari tiap produk
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby(
    'Produk').agg([np.mean, np.median]))
