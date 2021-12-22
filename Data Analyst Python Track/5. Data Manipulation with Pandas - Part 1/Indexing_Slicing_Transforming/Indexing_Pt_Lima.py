# Jika file yang akan dibaca melalui penggunaan library pandas dapat dipreview
# terlebih dahulu struktur datanya maka melalui fungsi yang ditujukan untuk membaca
# file dapat diset mana kolom yang akan dijadikan index.

# Fitur ini telah dimiliki oleh setiap fungsi yang digunakan dalam membaca data dengan pandas,
# yaitu penggunaan argumen index_col pada fungsi yang dimaksud.

# Dari dataset sample_csv.csv, sample_tsv.tsv, atau sample_excel.xlsx sudah tahu bahwa kolom dataset
# adalah 'order_id'; 'order_date'; 'customer_id'; 'city'; 'province'; 'product_id'; 'brand'; 'quantity'; and 'item_price'.
# Sehingga kode di atas digunakan langsung kolom 'order_date' pada saat membaca filenya.

import pandas as pd
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("sample_tsv.tsv",
                 sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))

# Terlihat bahwa kolom order_date sudah jadi index, dan tentunya jumlah kolom dataframe berkurang satu, yaitu menjadi delapan kolom.

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv
