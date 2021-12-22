# Dalam sub bab sebelumnya telah mempelajari bagaimana
# menslicing/filtering dataset dengan menggunakan method .loc pada kolom dataset.

# Sekarang, menerapkan berdasarkan index. Tentu syaratnya adalah dataset sudah dilakukan
# indexing terlebih dahulu melalui penerapan method .set_index

# Cara 1 : Gunakan method .loc seperti contoh berikut
# import pandas as pd
# Baca file sample_csv.csv
# df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Set index dari df sesuai instruksi
# df = df.set_index(["order_date","product_id"])
# Cara 1, Gunakan .loc
# df_slice1 = df.loc[("2019-01-01",["P2154","P2556"]),:]
# print("Cara 1:\n", df_slice1)

# Cara 2 : Gunakan pd.IndexSlice sebagai variabel untuk melakukan slicing index
# Cara 2, Gunakan pd.IndexSlice dan terapkan dengan .loc
# idx = pd.IndexSlice
# df_slice2 = df.sort_index().loc[idx["2019-01-01", "P2154":"P2556"], :]
# print("Cara 2:\n", df_slice2)

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv(
    "sample_csv.csv")
# Set index dari df sesuai instruksi
df = df.set_index(["order_date", "order_id", "product_id"])

# Baca kembali file "sample_csv.csv" dan set terlebih dahulu indexnya
# yaitu order_date, order_id, dan product_id. Kemudian slice/filter-lah dataset
# jika order_date adalah 2019-01-01, order_id adalah 1612339 dan product_id-nya yaitu P2154 dan P2159.
# Gunakanlah cara pertama.
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01", 1612339, ["P2154", "P2159"]), :]
print("Slice df:\n", df_slice)

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv
