# Pertama-tama, kita perlu mengimpor package plotnine terlebih dahulu.
# Kita masih membutuhkan package pandas untuk membaca data serta melakukan manipulasi data sederhana,
# sebelum kita membuat visualisasi data yang kita perlukan.
# Oleh karena itu kita perlu mengimpor package pandas juga:

from plotnine import *
import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd

# Membaca Data
# Selanjutnya kita akan membaca data-data yang kita perlukan.
# Terdapat dua dataset yang akan kita gunakan di modul ini:
# 1. Data kependudukan DKI Jakarta, yang akan disimpan dalam variabel bernama df_penduduk
# 2. Data inflasi Indonesia dan Singapura, yang akan disimpan dalam variabel bernama df_inflasi

# Kedua data tersebut akan disimpan dalam bentuk Pandas data frame.

# Link dataset :
# Kependudukan DKI Jakarta : https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv
# Inflasi : https://storage.googleapis.com/dqlab-dataset/inflasi.csv

import pandas as pd
df_penduduk = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
df_inflasi = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/inflasi.csv')

# Menampilkan Data

# Ide dasar dari grammar of graphics adalah,
# sebuah grafik statistik merupakan pemetaan dari data ke atribut-atribut aestetik
# (seperti warna, ukuran, dan bentuk) dari objek-objek geometris (seperti titik dan garis).

# Pada package plotnine , sebuah grafik terdiri dari komponen-komponen sebagai berikut:
# 1. data: sebuah data frame yang berisi data yang ingin kita visualisasikan
# 2. geoms (geometric objects): objek geometris seperti lingkaran, titik,
# dan teks yang ingin kita lihat di grafik
# 3. aesthetics: pemetaan dari data ke geometric objects seperti posisi, ukuran, warna, bentuk, dll.

# Di plotnine, ketiga komponen tersebut dihubungkan dengan operator + .

# Di bagian ini, kita akan membuat plot pertama kita dengan menggunakan data yang ada di variabel df_penduduk.
# Kita akan mencoba untuk membuat visualisasi jumlah penduduk di DKI Jakarta untuk masing-masing kabupaten/kota.

# Kode di bawah ini akan memperlihatkan 5 baris pertama dari dataset kependudukan yang kita miliki.
print(df_penduduk.head())

# Menjalankan Fungsi ggplot

# Pertama-tama, kita akan membuat plot terlebih dahulu.
# Untuk membuat plot, kita akan menggunakan fungsi ggplot.
# Untuk membuat sebuah plot kita perlu ggplot data apa yang ingin kita visualisasikan, dengan argumen data .

# Jalankan fungsi ggplot dan tambahkan argumen data dengan nilai,
# berupa data frame data kependudukan yang telah kita definisikan sebelumnya!

# Note : Karena kita belum mendefinisikan komponen-komponen lain seperti aestetik dan objek geometris,
# maka kita akan mendapatkan sebuah plot kosong.
ggplot(data=df_penduduk).draw()
plt.show()

# Menambahkan Variabel

# Selanjutnya, kita perlu mendefinisikan variabel-variabel apa yang ingin kita visualisasikan di plot,
# dengan mendefinisikan aestetik. Aestetik dapat didefinisikan dengan menggunakan fungsi aes().
# Untuk x-axis, kita akan menggunakan variabel NAMA KABUPATEN/KOTA,
# sementara untuk y-axis kita akan gunakan variabel JUMLAH.

# Dengan fungsi aes,
# tambahkan argumen x dengan variabel berupa kolom yang berisi nama kabupaten/kota di dataset penduduk,
# dan untuk argumen y gunakan variabel berupa kolom berisi jumlah penduduk di dataset penduduk.

# Menghasilkan :
(ggplot(data=df_penduduk)
 + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
 ).draw()
plt.show()
