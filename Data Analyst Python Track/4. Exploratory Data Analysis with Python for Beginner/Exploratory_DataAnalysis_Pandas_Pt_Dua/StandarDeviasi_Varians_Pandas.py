# Varians dan standar deviasi juga merupakan suatu ukuran dispersi atau variasi.
# Standar deviasi merupakan ukuran dispersi yang paling banyak dipakai.
# Hal ini mungkin karena standar deviasi mempunyai satuan ukuran yang sama dengan satuan ukuran data asalnya.
# Sedangkan varians memiliki satuan kuadrat dari data asalnya (misalnya cm^2).
# Syntax dari standar deviasi dan varians pada Pandas
# print([nama_dataframe].loc[:, "nama_kolom"].std())
# print([nama_dataframe].loc[:, "nama_kolom"].var())
# Contoh
# print(nilai_skor_df.loc[:, "Age"].std())
# print(nilai_skor_df.loc[:, "Score"].var())

import pandas as pd
order_df = pd.read_csv("order.csv")
print(order_df.loc[:, "product_weight_gram"].std())
