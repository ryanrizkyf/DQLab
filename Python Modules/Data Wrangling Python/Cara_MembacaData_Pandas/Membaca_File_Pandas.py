# Sebagai salah satu library untuk melakukan proses awal dari analisis data,
# pandas juga memiliki kemampuan untuk membaca berbagai macam jenis file.
# Format yang bisa dibaca oleh pandas ada berbagai macam, antara lain .txt, .csv, .tsv, dan lainnya.

# Pandas tidak hanya bisa membaca file saja,
# namun juga bisa merubah data dari file menjadi bentuk dataframe yang akhirnya nanti bisa diakses,
# diagregasi dan diolah.

import pandas as pd
csv_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(csv_data)
