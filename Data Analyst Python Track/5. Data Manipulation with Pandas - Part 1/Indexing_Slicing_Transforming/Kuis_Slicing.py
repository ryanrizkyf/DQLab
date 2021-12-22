import pandas as pd
sample_csv = pd.read_csv('sample_csv.csv')
sample_csv = sample_csv.set_index(['province', 'product_id'])
idx = pd.IndexSlice
print(sample_csv.sort_index().loc[idx['Sulawesi Selatan', 'P3082':'P3357'], :])
