import pandas as pd

filename = "input.csv"

df = pd.read_csv(filename)

print(df.loc[2:3])