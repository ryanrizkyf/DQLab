# Sekarang, akan melakukan treatment ketiga untuk menghandle missing value pada dataframe.
# Treatment ini dilakukan dengan cara mengisi missing value dengan nilai lain, yang dapat berupa :
# 1. Nilai statistik seperti mean atau median
# 2. Interpolasi data
# 3. Text tertentu

# Akan mulai pada kolom yang missing yang tipe datanya adalah berupa object.
# Kolom tersebut adalah province_state, karena tidak tahu secara persis province_state mana yang dimaksud,
# bisa menempatkan string "unknown" sebagai substitusi missing value.
# Meskipun keduanya berarti sama-sama tidak tahu tetapi berbeda dalam representasi datanya.

# Untuk melakukan hal demikian dapat menggunakan method .fillna() pada kolom dataframe yang dimaksud.

import pandas as pd
# Baca file "public data covid19 jhu csse eu.csv"
df = pd.read_csv(
    "CHAPTER+4+-+missing+value+-+public+data+covid19+.csv")
# Cetak unique value pada kolom province_state
print("Unique value awal:\n", df["province_state"].unique())
# Ganti missing value dengan string "unknown_province_state"
df["province_state"] = df["province_state"].fillna("unknown_province_state")
# Cetak kembali unique value pada kolom province_state
print("Unique value setelah fillna:\n", df["province_state"].unique())

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/CHAPTER+4+-+missing+value+-+public+data+covid19+.csv
