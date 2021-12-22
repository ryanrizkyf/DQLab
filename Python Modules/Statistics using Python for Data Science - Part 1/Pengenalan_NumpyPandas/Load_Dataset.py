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
