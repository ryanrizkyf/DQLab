# Method .read_json() digunakan untuk membaca URL API yang formatnya JSON
# dan merubahnya menjadi dataframe pandas.

# Notes
# Dataset JSON: https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/covid2019-api-herokuapp-v2.json

import pandas as pd
# File JSON
url = "https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10))  # Menampilkan 10 data teratas
