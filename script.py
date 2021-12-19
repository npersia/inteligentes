import pandas as pd 

data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

# Data preparation

df["introelapse"] = pd.to_numeric(df["introelapse"])

df["introelapse"] = pd.cut(df["introelapse"],
       bins=[0, 25, 50, 75, 100, 125], 
       labels=["Muy rápido", "Rápido", "Promedio", "Lento", "Muy lento"])

print(df["introelapse"])

print(data.head())