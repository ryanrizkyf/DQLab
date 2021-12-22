import pandas as pd
import numpy as np

arr_df = np.array([[1, 2, 3, 5],
                   [5, 6, 7, 8],
                   ['a', 'b', 9, 10]])
df = pd.DataFrame(arr_df)
# mengubah data yang berupa string menjadi angka misal 'a' menjadi 11 dan 'b' menjadi 12
df.iloc[2, 0:2] = [11:12]
