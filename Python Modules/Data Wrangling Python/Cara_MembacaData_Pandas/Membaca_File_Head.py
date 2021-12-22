# Pada suatu kasus, data yang kita baca cukup banyak atau loading yang lama.
#  Untuk memastikan data kita terbaca dengan baik dan bisa menampilkan data sebagian
# untuk ditampilkan secara benar, kita bisa memakai fungsi head().

import pandas as pd
csv_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(csv_data.head())
