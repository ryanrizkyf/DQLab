# Seperti artinya slicing adalah cara untuk melakukan filter ke dataframe/series
# berdasarkan kriteria tertentu dari nilai kolomnya ataupun kriteria index-nya.

# Terdapat 2 cara paling terkenal untuk slicing dataframe,
# yaitu dengan menggunakan method .loc dan .iloc pada variabel bertipe pandas DataFrame/Series.
# Method .iloc ditujukan untuk proses slicing berdasarkan index berupa nilai integer tertentu.
# Akan tetapi akan lebih sering menggunakan dengan method .loc karena lebih fleksibel.

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv(
    "sample_csv.csv")

# Dataset belum dilakukan indexing, jadi slicing berdasarkan nilai kolomnya.
# Untuk itu "sample_csv.csv" dibaca kembali dan dipraktikkan metode .loc[]
# dan slice/filter-lah dataset
# jika customer_id adalah 18055 dan product_id-nya yaitu P0029, P0040, P0041, P0116, dan P0117.
df_slice = df.loc[(df["customer_id"] == "18055") &
                  (df["product_id"].isin(
                      ["P0029", "P0040", "P0041", "P0116", "P0117"]))
                  ]
print("Slice langsung berdasarkan kolom:\n", df_slice)

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv
