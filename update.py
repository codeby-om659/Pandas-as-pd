import pandas as pd
df=pd.read_csv("output.csv")
#
print(df["sallary"])
df["sallary"]=df["sallary"]*1.5
print(df)
