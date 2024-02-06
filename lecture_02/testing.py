import pandas as pd

df = pd.read_csv('train.csv')

num_rows_with_empty = df.isnull().any(axis=1).sum()

print("There are " +  str(num_rows_with_empty) + " rows with at least one empty value")