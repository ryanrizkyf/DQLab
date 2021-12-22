# Selanjutnya, untuk mencari rataan dari suatu data
# dari dataframe. Aku dapat menggunakan syntax mean, median, dan mode dari Pandas.
# print([nama_dataframe].loc[:, "nama_kolom"].mean())
# print([nama_dataframe].loc[:, "nama_kolom"].median())
# print([nama_dataframe].loc[:, "nama_kolom"].mode())
# contoh
# print(nilai_skor_df.loc[:, "Age"].mean())
# print(nilai_skor_df.loc[:, "Score"].median())

import pandas as pd
order_df = pd.read_csv('order.csv')
# print(order_df.loc[:, "qty"].mean())
