# File Excel dengan ekstensi *.xls atau *.xlsx cukup banyak digunakan dalam menyimpan data.
# Pandas juga memiliki fitur untuk membaca file excel.

# Notes :
# Dataset : https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_excel.xlsx

# Fungsi .read_excel() digunakan untuk membaca file excel menjadi dataframe pandas.

import pandas as pd
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel(
    "sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4))  # Menampilkan 4 data teratas
