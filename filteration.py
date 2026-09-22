import pandas as pd 
df=pd.read_csv("output.csv")
print(df["name"])
print(df[["name","age"]])

#Condition
filter=df[(df["age"]>30) & (df["sallary"]>15000)]
print(filter) 
