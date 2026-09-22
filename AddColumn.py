import pandas as pd
df=pd.read_csv("output.csv")
df["bonous"]=df["sallary"]*0.1
print(df)
