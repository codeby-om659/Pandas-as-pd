import pandas as pd
df=pd.read_csv("output.csv")
print(df["age"].mean())
print(df["age"].std())
print(df["age"].max())

