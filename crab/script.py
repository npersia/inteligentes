import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df["Length"] = pd.to_numeric(df["Length"])
df["Length"] = pd.cut(df["Length"], 6)

df["Height"] = pd.to_numeric(df["Height"])
df["Height"] = pd.cut(df["Height"], 2)

df["Diameter"] = pd.to_numeric(df["Diameter"])
df["Diameter"] = pd.cut(df["Diameter"], 6)

df["Weight"] = pd.to_numeric(df["Weight"])
df["Weight"] = pd.cut(df["Weight"], 6)

df["Shucked Weight"] = pd.to_numeric(df["Shucked Weight"])
df["Shucked Weight"] = pd.cut(df["Shucked Weight"], 6)

df["Viscera Weight"] = pd.to_numeric(df["Viscera Weight"])
df["Viscera Weight"] = pd.cut(df["Viscera Weight"], 6)

df["Shell Weight"] = pd.to_numeric(df["Shell Weight"])
df["Shell Weight"] = pd.cut(df["Shell Weight"], 6)

df["Age"] = pd.to_numeric(df["Age"])

df["Age"] = pd.cut(df["Age"], 4)

#df["Age"] = pd.cut(df["Age"],
#       bins=[0, 1, 9, 10, 11, 18, np.Inf],
#       labels=[1, 2, 3, 4, 5, 6])

df.to_csv('processed_data.csv', index=False)