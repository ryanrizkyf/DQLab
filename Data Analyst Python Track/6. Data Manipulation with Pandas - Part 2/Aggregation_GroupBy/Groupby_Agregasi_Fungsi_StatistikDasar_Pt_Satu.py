# Pada subbab ini akan menerapkan groupby dan fungsi aggregasi mean dan std
# untuk menentukan nilai rata-rata dan standar deviasi dari masing-masing kelompok data dari
# dataset https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
# dan diassign sebagai variabel df_gaq.

import pandas as pd
# Load data global_air_quality.csv
gaq = pd.read_csv(
    'global_air_quality_4000rows.csv')
# Create variabel pollutantÂ 
pollutant = gaq[['country', 'city', 'pollutant', 'value']].pivot_table(
    index=['country', 'city'], columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())

# Group berdasarkan country dan terapkan aggregasi mean, method .mean()
# setelah penerapan method .groupby() digunakan untuk mencari rata-rata dari tiap kelompok
# [1] Group berdasarkan country dan terapkan aggregasi mean
pollutant_mean = pollutant.groupby('country').mean()
print('Rata-rata pollutant (5 teratas):\n', pollutant_mean.head())

# Group berdasarkan country dan terapkan aggregasi std, method .std()
# setelah penerapan method .groupby() digunakan untuk mencari
# standard deviasi (penyimpangan) dari tiap kelompok
# [2] Group berdasarkan country dan terapkan aggregasi std
pollutant_std = pollutant.groupby('country').std().fillna(0)
print('Standar deviasi pollutant (5 teratas):\n', pollutant_std.head())
