# Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim.
# Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau
# beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya.

# Pada umumnya, outliers dapat ditentukan dengan metric IQR (interquartile range).
# Rumus dasar dari IQR: Q3 - Q1, daan data suatu observasi dapat dikatakan outliers jika memenuhi kedua syarat dibawah ini:
# data < Q1 - 1.5 * IQR
# data > Q3 + 1.5 * IQR

# Syntax di Python
# Q1 = nama_dataframe.quantile(0.25)
# Q3 = nama_dataframe.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
# Contoh
# Q1 = nilai_skor_df[["Score"]].quantile(0.25)
# Q3 = nilai_skor_df[["Score"]].quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)

# Karena saat ini memiliki skor IQR, saatnya untuk menentukan Outliers.
# Kode di bawah ini akan memberikan output dengan beberapa nilai True atau False.
# Titik data di mana terdapat False yang berarti nilai-nilai ini valid sedangkan True menunjukkan adanya Outliers.
# print((nilai_skor_df < (Q1 - 1.5*IQR))) | (nilai_skor_df > (Q3 + 1.5*IQR))

import pandas as pd
order_df = pd.read_csv("order.csv")
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print((order_df < (Q1 - 1.5*IQR))) | (order_df > (Q3 + 1.5*IQR))
