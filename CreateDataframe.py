import pandas as pd 
data={
    "name":["om","ram","ansh",'aman'],
    "age":[10,20,30,40],
    "city":["delhi","goa","bihar","up"]
    }

df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
df.to_json("input.json",index=False)
