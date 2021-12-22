# Seperti yang telah dipelajari sebelumnya bahwa ada method .head
# yang diterapkan pada suatu variabel bertipe pandas dataframe/series.

# Method .head ditujukan untuk membatasi tampilan jumlah baris teratas dari dataset.
# Sementara itu, method .tail ditujukan untuk membatasi jumlah baris terbawah dari dataset.

# Secara umum kedua method ini memiliki bentuk
# [nama_dataframe].head()
# dan
# [nama_dataframe].tail()

# dengan n merupakan jumlah baris yang akan ditampilkan,
# jika tidak disebutkan n = 5 (sebagai nilai default dari n).

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv(
    "sample_csv.csv")
# Tampilkan 3 data teratas
print("Tiga data teratas:\n", df.head(3))
# Tampilkan 3 data terbawah
print("Tiga data terbawah:\n", df.tail(3))

# dataset read_csv = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv #
