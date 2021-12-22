# Mengganti nama kolom pada Pandas dapat dilakukan dengan 2 cara:
# 1. Menggunakan nama kolom.
# 2. Menggunakan indeks kolom.

# 1. Rename menggunakan nama kolom
# Syntax
# nama_dataframe.rename(columns={"column_name_before":"column_name_after"}, inplace=True)
# contoh
nilai_skor_df.rename(columns={"Age": "Umur"}, inplace=True)

# 2. Rename menggunakan indeks kolom
# Syntax
# nama_dataframe.columns.values[no_of_column] = "column_name_after"
# contoh
nilai_skor_df.columns.values[0] = "Umur"
