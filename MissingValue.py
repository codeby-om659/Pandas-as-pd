import pandas as pd
df=pd.read_csv("output.csv")
print(df.isnull())# none ki jagah true pritn hoga
print(df.isnull().sum())#each column mai kitni missing value hai 
#print(df.fillna(5))#none value  5 se replace ho jayegi

#print(df.dropna())#none wali row drop ho jayegi

print(df["age"].fillna(df["age"].mean(),inplace=True))
