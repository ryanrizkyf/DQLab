# CSV dan TSV pada hakikatnya adalah tipe data text dengan perbedaan terletak
# pada pemisah antar data dalam satu baris.
# Pada file CSV, antar data dalam satu baris dipisahkan oleh comma, ",".
# Namun, pada file TSV antar data dalam satu baris dipisahkan oleh "Tab".

# Fungsi .read_csv() digunakan untuk membaca file yang value nya dipisahkan oleh comma (default),
# terkadang pemisah value nya bisa di set â\tâ untuk file tsv (tab separated values).

# Notes
# Dataset csv : https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv
# Dataset tsv : https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv

import pandas as pd
# File CSV
df_csv = pd.read_csv(
    "sample_csv.csv")
print(df_csv.head(3))  # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv(
    "sample_tsv.tsv", sep='\t')
print(df_tsv.head(3))  # Menampilkan 3 data teratas
