import pandas as pd

df = pd.read_csv("data.csv")
print("Column names:", df.columns.tolist())
