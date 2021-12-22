# Jika ingin mendapatkan summary statistik dari kolom yang tidak
# bernilai angka, maka aku dapat menambahkan command include=["object"] pada syntax describe().
# print(nama_dataframe.describe(include=["object"]))

# Function describe() dengan include="all" akan memberikan summary statistic dari semua kolom.
# print(nama_dataframe.describe(include=["all"]))

import pandas as pd
order_df = pd.read_csv('order.csv')
print(order_df.describe(include=["object"]))
