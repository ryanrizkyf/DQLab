# Pertama-tama, kita perlu mengimpor package plotnine terlebih dahulu.
# Kita masih membutuhkan package pandas untuk membaca data serta melakukan manipulasi data sederhana,
# sebelum kita membuat visualisasi data yang kita perlukan.
# Oleh karena itu kita perlu mengimpor package pandas juga:

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
