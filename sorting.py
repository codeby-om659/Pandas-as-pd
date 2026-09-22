import pandas as pd
df=pd.read_csv("output.csv")
print(df.sort_values(by="age",ascending=True,inplace=True))
print(df)
