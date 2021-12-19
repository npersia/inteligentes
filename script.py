import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

# Remove malformed lines (#13507)
data = data.drop(13505)

df = pd.DataFrame(data)

# Data preparation

# Process introelapse column (convert to numeric, replace missing with mean, discretize)
df["introelapse"] = pd.to_numeric(df["introelapse"])

df["introelapse"] = df["introelapse"].fillna(df["introelapse"].mean())

df["introelapse"] = pd.cut(df["introelapse"],
       bins=[0, 25, 50, 75, 100, np.Inf],
       labels=["Very Fast", "Fast", "Average", "Slow", "Very Slow"])

# Process testelapse column (convert to numeric, replace missing with mean, discretize)

df["testelapse"] = pd.to_numeric(df["testelapse"])

df["testelapse"] = df["testelapse"].fillna(df["testelapse"].mean())

df["testelapse"] = pd.cut(df["testelapse"],
       bins=[0, 50, 100, 150, 200, np.Inf],
       labels=["Very Fast", "Fast", "Average", "Slow", "Very Slow"])

# Process surveyelapse column (convert to numeric, replace missing with mean, discretize)
df["surveyelapse"] = pd.to_numeric(df["surveyelapse"])

df["surveyelapse"] = df["surveyelapse"].fillna(df["surveyelapse"].mean())

df["surveyelapse"] = pd.cut(df["surveyelapse"],
       bins=[0, 50, 100, 150, 200, np.Inf],
       labels=["Very Fast", "Fast", "Average", "Slow", "Very Slow"])


# TODO: Race booleans to categoric

# TODO: Delete major or boolean (hasMajorData)

# TODO: Sanitize (<= 100), discretize age

# TODO: Discretize screenw, screenh. Phone, PC, monitor. 

# TODO: Discretize class nerdiness (LOW, NORMAL, NERD, FREAK)

# TODO: Remove ASD

ax = df["introelapse"].hist()
fig = ax.get_figure()
fig.savefig('figure.pdf')

df.to_csv('processed_data.csv', index=False)