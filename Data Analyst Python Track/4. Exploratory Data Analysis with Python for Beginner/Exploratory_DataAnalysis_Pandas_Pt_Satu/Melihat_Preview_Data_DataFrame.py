# Selanjutnya, untuk mendapatkan gambaran dari konten dataframe tersebut.
# Kita dapat menggunakan function head dan tail, dengan syntax:

# Menampilkan konten teratas dari [nama_dataframe]
# untuk sejumlah bilangan bulat [jumlah_data]
# print([nama_dataframe].head([jumlah_data]))

# Jika [jumlah_data] pada function head dan tail dikosongkan maka
# secara default akan di ditampilkan sebanyak 5 (lima) baris saja.
# Sehingga bisa ditulis sebagai berikut:
# DEFAULT: Menampilkan 5 (baris) konten teratas dari [nama_dataframe]
# print([nama_dataframe].head())

# DEFAULT: Menampilkan 5 (baris) konten terbawah dari [nama_dataframe]
# print([nama_dataframe].tail())

import pandas as pd
order_df = pd.read_csv(
    "order.csv")
print(order_df.head(15))

# read_csv = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/order.csv #
