# Fungsi .read_sql() atau .read_sql_query() digunakan untuk membaca query dari database
# dan translate menjadi pandas dataframe, contoh case ini database sqlite.

# Contoh penggunaan
# Membuat koneksi ke database Financial di https://relational.fit.cvut.cz/dataset/Financial
import pandas as pd
import mysql.connector
my_conn = mysql.connector.connect(host="relational.fit.cvut.cz",
                                  port=3306,
                                  user="guest",
                                  passwd="relational",
                                  database="financial",
                                  use_pure=True)

# Jika menggunakan .read_sql_query
# Gunakanlah .read_sql_query untuk membaca tabel load tersebut
df_loan = pd.read_sql_query(my_query, my_conn)
# Tampilkan 5 data teratas
df_loan.head()

# Jika menggunakan .read_sql
# Gunakanlah .read_sql untuk membaca tabel load tersebut
df_loan = pd.read_sql(my_query, my_conn)
# Tampilkan 5 data teratas
df_loan.head()
