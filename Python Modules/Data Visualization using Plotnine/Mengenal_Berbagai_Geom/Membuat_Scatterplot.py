# Pertama-tama, kita perlu mengimpor package plotnine terlebih dahulu.
# Kita masih membutuhkan package pandas untuk membaca data serta melakukan manipulasi data sederhana,
# sebelum kita membuat visualisasi data yang kita perlukan.
# Oleh karena itu kita perlu mengimpor package pandas juga:

import plotnine
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

# Mendefinisikan Objek Geometris

# Kita sudah memiliki plot dengan NAMA KABUPATEN/KOTA sebagai x-axis dan JUMLAH sebagai y-axis.
# Namun kita belum mendefinisikan objek geometris apa yang ingin kita gunakan,
# jadi di plot tersebut belum ada data yang ditampilkan.

# Ketika menggabungkan dua atau lebih komponen, perlu diperhatikan bahwa:
# 1. Kita menggunakan operator +
# 2. Kita perlu menggunakan tanda kurung di keseluruhan fungsi kita,
# karena kalau tidak, Python akan menganggap itu sebagai error.

# Jadi, alih-alih menuliskan:
# ggplot(data=df_penduduk)
# + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')

# Kita harus menuliskan tanda kurung di sekitar fungsinya:
# (ggplot(data=df_penduduk)
# + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH'))

# Sebagai contoh, kita menggunakan bars untuk membuat visualisasi jumlah penduduk per kabupaten/kota.
# Kita akan menggunakan geom geom_col().
# Tinggi dari bars yang dihasilkan oleh geom_col(),
# merepresentasikan data yang telah kita definisikan di y-axis.
# Tambahkan geom untuk membuat bar chart di kode di bawah ini,
# agar kita dapat memunculkan data jumlah penduduk.

(ggplot(data=df_penduduk)
 + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
 + geom_col()
 ).draw()
plt.show()

# Notes : Lebih lanjut tentang geom_col() dapat dibaca di
# (https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_col.html)

# Membuat Horizontal Bar Chart

# Pada plot sebelumnya kita sudah mengenal komponen-komponen dasar yang digunakan di plotnine,
# yaitu data, aestetik, dan geoms.
# Selanjutnya kita akan mempelajari hal-hal yang kita dapat lakukan untuk membuat
# visualisasi data yang tampak lebih rapi dan menarik.

# Satu hal yang mungkin kita perhatikan adalah label di x-axis yang berdempetan.
# Hal ini karena label-label di x-axis kita mempunyai nama yang cukup panjang.
# Salah satu solusi yang dapat dilakukan adalah membuat horizontal bar chart.
# Di plotnine, kita dapat menggunakan
# coord_flip() agar x-axis di grafik berubah posisi dari horizontal menjadi vertikal,
# dan y-axis berubah posisi dari vertikal ke horizontal.

# Tambahkan fungsi yang diperlukan,
# agar kita bisa mendapatkan horizontal bar chart dari plot yang telah kita buat sebelumnya.

(ggplot(data=df_penduduk)
 + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
 + geom_col()
 + coord_flip()
 ).draw()
plt.tight_layout()
plt.show()

# Note : Lebih lanjut tentang fungsi tersebut dapat dilihat di
# (https://plotnine.readthedocs.io/en/stable/generated/plotnine.coords.coord_flip.html?highlight=coord_flip)

# Menambah Judul dan Mengubah Label

# Kita dapat menambahkan judul dan mengubah label pada axis di grafik dengan fungsi labs().

# Berikut beberapa argumen yang dapat kita gunakan:
# title : menambahkan judul plot
# x : mendefinisikan label pada x-axis
# y : mendefinisikan label pada y-axis

# Gunakan fungsi labs untuk:
# Menambahkan judul grafik yaitu "Jumlah penduduk per kabupaten/kota di DKI Jakarta (2013)"
# Mengubah label "JUMLAH" menjadi "Jumlah Penduduk"
# Mengubah label "NAMA KABUPATEN/KOTA" menjadi "Kabupaten/Kota"

plotnine.options.figure_size = (12, 4.8)
(ggplot(data=df_penduduk)
 + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
 + geom_col()
 + coord_flip()
 + labs(title='Jumlah penduduk per kabupaten/kota di DKI Jakarta (2013)',
        x='Kabupaten/Kota',
        y='Jumlah Penduduk')
 ).draw()
plt.show()

# Menampilkan Warna Berbeda

# Bagaimana jika kita ingin menampilkan bar chart yang memiliki warna berbeda untuk perempuan dan laki-laki?
# Kita dapat membuatnya dengan mendefinisikan argumen fill di fungsi aes.
# Pada argumen fill di fungsi aes, berikan nilai berupa nama kolom jenis kelamin di data kependudukan kita.

plotnine.options.figure_size = (10, 3.6)
(ggplot(data=df_penduduk)
 + aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH', fill='JENIS KELAMIN')
 + geom_col()
 + coord_flip()
 + labs(title='Jumlah penduduk per kabupaten/kota di DKI Jakarta (2013)',
        x='Kabupaten/Kota',
        y='Jumlah Penduduk')
 ).draw()
plt.show()

# Membuat Grafik dengan Variabel Berbeda

# Sekarang kita akan berlatih untuk membuat grafik serupa namun dengan variabel yang berbeda.

# Buatlah grafik horizontal bar chart dengan ketentuan sebagai berikut:
# Bar chart menggambarkan jumlah penduduk per kelurahan di kecamatan Cengkareng.
# Judul grafik yaitu "Jumlah penduduk per kelurahan di Kecamatan Cengkareng (2013)"
# Pada axis yang berisi nama kelurahan, berikan label "Kelurahan"
# Pada axis yang berisi jumlah penduduk, berikan label "Jumlah Penduduk"
# Berikan warna yang berbeda untuk jenis kelamin laki-laki dan perempuan.

plotnine.options.figure_size = (10, 3.6)
(ggplot(data=df_penduduk[df_penduduk['NAMA KECAMATAN'] == 'CENGKARENG'])
 + aes(x='NAMA KELURAHAN', y='JUMLAH', fill='JENIS KELAMIN')
 + geom_col()
 + coord_flip()
 + labs(title='Jumlah penduduk per kelurahan di DKI Jakarta (2013)',
        x='Kelurahan',
        y='Jumlah Penduduk')
 ).draw()
plt.show()

# Memisahkan Grafik

# Contoh plot yang telah kita buat adalah bar chart yang berbentuk stacked,
# dalam artian untuk data jenis kelamin laki-laki dan perempuan, keduanya bertumpuk di satu bar.
# Bagaimana kalau kita ingin memisahkannya dan meletakannya di samping satu sama lain?

# Kita dapat menggunakan argumen position di fungsi geom_col().
# Untuk memisahkan grafik tersebut kita dapat mendefinisikan position = position_dodge.

plotnine.options.figure_size = (10, 3.6)
(ggplot(data=df_penduduk[df_penduduk['NAMA KECAMATAN'] == 'CENGKARENG'])
 + aes(x='NAMA KELURAHAN', y='JUMLAH', fill='JENIS KELAMIN')
 + geom_col(position='position_dodge')
 + coord_flip()
 + labs(title='Jumlah penduduk per kelurahan di DKI Jakarta (2013)',
        x='Kelurahan',
        y='Jumlah Penduduk')
 ).draw()
plt.show()

# Membuat Scatterplot

# Scatterplot biasanya digunakan untuk melihat hubungan antara dua variabel.
# Kita dapat menggunakan scatterplot untuk melihat hubungan antara jumlah penduduk di suatu kelurahan,
# dengan luas kelurahan tersebut.

# Untuk mempermudah, kita akan mendefinisikan data frame baru, df_penduduk_luas_jumlah,
# sebagai rangkuman dari kolom nama kelurahan, luas wilayah, dan jumlah penduduk.
# df_penduduk_luas_jumlah = df_penduduk.groupby(['NAMA KELURAHAN', 'LUAS WILAYAH (KM2)'])[['JUMLAH']].agg('sum').reset_index()

# Untuk membuat scatterplot, kita dapat menggunakan geom geom_point().
# Buatlah sebuah scatterplot dengan menggunakan data di data frame df_penduduk_luas_jumlah.
# Gunakan ggplot() untuk mendefinisikan data,
# aes() untuk menentukan aestetik, dan geom_point() sebagai geom -nya.
# Variabel di x-axis adalah jumlah penduduk, sementara di y-axis adalah luas wilayah (km persegi).


df_penduduk_luas_jumlah = df_penduduk.groupby(
    ['NAMA KELURAHAN', 'LUAS WILAYAH (KM2)'])[['JUMLAH']].agg('sum').reset_index()

(ggplot(data=df_penduduk_luas_jumlah)
 + aes(y='LUAS WILAYAH (KM2)', x='JUMLAH')
 + geom_point()
 ).draw()
plt.show()
