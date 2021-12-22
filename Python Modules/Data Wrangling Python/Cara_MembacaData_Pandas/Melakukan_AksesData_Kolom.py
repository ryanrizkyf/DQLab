# Dalam suatu analisis data ada kalanya kita hanya butuh melakukan akses beberapa data saja
# dan tidak perlu harus menampilkan semua data. Pada pandas kita bisa melakukan akses dalam berbagai kebutuhan.
# Mulai dari hanya akses kolom tertentu ataupun baris tertentu.
# Pada sesi kali ini kita akan mencoba untuk melakukan akses beberapa kolom tertentu pada suatu dataset.

import pandas as pd
csv_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
# Pertama yang harus dilakukan untuk melakukan akses kolom adalah mengetahui nama-nama kolom yang ada.
# Coba ketikkan kode di bawah ini untuk melihat nama kolom yang ada.
print(csv_data.columns)
# Pada dataset ini ada 5 kolom termasuk class,
# dimana 4 kolom  merupakan data numerik dan 1 kolom merupakan data string.

# Pada praktek selanjutnya kita akan mencoba mengakses data age.
# Untuk melakukannya coba tuliskan kode di bawah ini :
print(csv_data['Age'])
