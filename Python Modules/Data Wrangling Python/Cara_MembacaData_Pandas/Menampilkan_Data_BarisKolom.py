# Tidak hanya dengan menentukan dari kolom dan baris,
# dengan menggunakan pandas kita juga bisa memanggil suatu data dari suatu baris
# dan kolom tertentu dalam satu waktu.

import pandas as pd
csv_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(csv_data['Age'].iloc[1])
print("Cuplikan Dataset:")
print(csv_data.head())
