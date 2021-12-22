import pandas as pd
order_df = pd.read_csv(
    "order.csv")
# Standar variasi kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].std())
# Varians kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].var())

# read_csv = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/order.csv #
