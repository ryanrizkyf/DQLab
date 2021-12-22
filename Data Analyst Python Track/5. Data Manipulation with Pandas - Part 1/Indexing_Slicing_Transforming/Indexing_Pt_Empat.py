# Terdapat beberapa cara untuk membuat index, salah satunya adalah seperti yang telah dilakukan
# pada sub bab sebelumnya dengan menggunakan method .set_index().

# Di sub bab ini akan menggunakan assignment untuk menset index dari suatu data frame.
# Untuk itu file "sample_excel.xlsx" yang digunakan. Perhatikan code berikut.

# import pandas as pd
# Buat data frame
# df_week = pd.DataFrame({
#    "day_number": [1, 2, 3, 4, 5, 6, 7],
#    "week_type": ["weekday" for i in range(5)] + ["weekend" for i in range(2)]
# })
# Deifinisikan indexnya dan assign
# df_week.index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print(df_week)

# Notes
# Cara yang ditunjukkan oleh baris 14 (ke 14) pada code editor di atas hanya berlaku
# jika index yang diassign tersebut memiliki panjang yang sama dengan jumlah baris dari dataframe.

# Jika ingin kembalikan dataframe ke index defaultnya yaitu dari 0 s/d jumlah baris data - 1,
# maka dapat menggunakan method .reset_index(drop=True), argument drop=True bertujuan untuk menghapus index lama.

import pandas as pd
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv(
    "sample_tsv.tsv", sep="\t", nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv
