# Di sub bab sebelumnya telah dibahas terkait single index, tentunya pada sub bab ini akan bahas multi index
# atau disebut juga dengan hierarchical indexing.

# Untuk membuat multi index (hierarchical indexing) dengan pandas diperlukan kolom-kolom mana saja
# yang perlu disusun agar index dari data frame menjadi sebuah hirarki yang kemudian dapat dikenali.

# Selanjutnya akan membuat multi index dengan menggunakan kolom 'order_id', 'city', 'customer_id',
# dengan menggunakan method .set_index().

import pandas as pd

# Baca file TSV sample_tsv.tsv
df = pd.read_csv(
    "sample_tsv.tsv", sep="\t")

# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])

# Untuk melihat multi index yang telah diset dapat dilakukan dengan
# Index dari df_x
print("Index df_x:", df_x.index)

# Perlu diketahui bahwa kumpulan index dari multi index adalah list dari banyak tuples,
# tuples nya merupakan kombinasi yang ada dari gabungan index-index tersebut.
# Dari multi index tersebut juga terdapat atribut levels yang menunjukkan urutan index,
# dalam case ini 'order_date' > 'city' > 'customer_id'.
# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name, ':', level)

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv
