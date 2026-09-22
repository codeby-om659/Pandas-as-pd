import pandas as pd
df=pd.read_csv("output.csv")
df.drop(columns=["age"],inplace=True)
print(df)
