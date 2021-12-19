import pandas as pd 
import numpy as np

data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

# Data preparation

# Remove malformed lines (#13507)

# Convert time lapses to numeric
df["introelapse"] = pd.to_numeric(df["introelapse"])

df["introelapse"] = pd.cut(df["introelapse"],
       bins=[0, 25, 50, 75, 100, 125], 
       labels=["Muy rápido", "Rápido", "Promedio", "Lento", "Muy lento"])



df.to_csv('processed_data.csv', index=False)