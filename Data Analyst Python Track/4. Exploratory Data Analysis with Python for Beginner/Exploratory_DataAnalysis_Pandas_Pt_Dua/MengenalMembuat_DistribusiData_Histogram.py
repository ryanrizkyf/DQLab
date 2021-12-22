# Histogram merupakan salah satu cara untuk mengidentifikasi sebaran distribusi dari data.
# Histogram adalah grafik yang berisi ringkasan dari sebaran (dispersi atau variasi) suatu data.
# Pada histogram, tidak ada jarak antar batang/bar dari grafik.
# Hal ini dikarenakan bahwa titik data kelas bisa muncul dimana saja di daerah cakupan grafik.
# Sedangkan ketinggian bar sesuai dengan frekuensi atau frekuensi relatif jumlah data di kelas.
# Semakin tinggi bar, semakin tinggi frekuensi data. Semakin rendah bar, semakin rendah frekuensi data.
# Syntax umum
# nama_dataframe[["nama_kolom"]].plot.hist(bins=jumlah_bins)

# Beberapa atribut penting dalam histogram pandas:
# bins = jumlah_bins dalam histogram yang akan digunakan. Jika tidak didefinisikan jumlah_bins, maka function akan secara default menentukan jumlah_bins sebanyak 10.
# by = Kolom di DataFrame untuk di group by. (valuenya berupa nama column di dataframe tersebut).
# alpha = Menentukan opacity dari plot di histogram. (value berupa range 0.0 - 1.0, dimana semakin kecil akan semakin kecil opacity nya)
# figsize = digunakan untuk menentukan ukuran dari plot histogram. Contoh: figsize=(10,12)

import pandas as pd
order_df = pd.read_csv(
    "order.csv")
# plot histogram kolom: price
# order_df[[price]].plot.hist(figsize=(4, 5), bins=10,
#                            xlabelsize = 8, ylabelsize = 8)
