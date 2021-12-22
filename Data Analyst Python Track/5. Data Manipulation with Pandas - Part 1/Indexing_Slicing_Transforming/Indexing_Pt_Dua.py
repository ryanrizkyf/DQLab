# Secara default setelah suatu data frame dibaca dari file dengan format tertentu,
# index-nya merupakan single index.

# Pada sub bab ini akan mencetak index dan kolom yang dimiliki oleh file "sample_csv.csv".
# Untuk menentukan index dan kolom yang dimiliki oleh dataset yang telah dinyatakan sebagai
# sebuah dataframe pandas dapat dilakukan dengan menggunakan attribut .index dan .columns.

import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv(
    "sample_tsv.tsv", sep="\t")
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv #
