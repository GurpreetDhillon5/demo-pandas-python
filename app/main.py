import pandas as pd
print ("done")
# read csv
df = pd.read_csv("./input/sol-dataset.csv")
print(df.shape)
print(df.describe())
sum_df = df.describe()
sum_df.to_csv('./output/sum_df.csv')