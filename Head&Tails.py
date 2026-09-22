import pandas as pd
df=pd.read_csv("output.csv")
print(df.head(2))#it provide first  n row but default n value is 5
print(df.tail(2))# it provide last n row,default n value is 5
