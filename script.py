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
df['race'] = \
       np.where(df['race_other'] == '1', 'race_other',
       np.where(df['race_nativeau'] == '1', 'race_nativeau',
       np.where(df['race_nativeam'] == '1', 'race_nativeam',
       np.where(df['race_hispanic'] == '1', 'race_hispanic',
       np.where(df['race_white'] == '1', 'race_white',
       np.where(df['race_black'] == '1', 'race_black',
       np.where(df['race_asian'] == '1', 'race_asian',
       np.where(df['race_arab'] == '1', 'race_arab', '0')
                     )
                     )
                     )
                     )
                     )
                     )
                     )


# TODO: Drop race columns
df.drop('race_other', axis=1, inplace=True)
df.drop('race_nativeau', axis=1, inplace=True)
df.drop('race_nativeam', axis=1, inplace=True)
df.drop('race_hispanic', axis=1, inplace=True)
df.drop('race_white', axis=1, inplace=True)
df.drop('race_black', axis=1, inplace=True)
df.drop('race_asian', axis=1, inplace=True)
df.drop('race_arab', axis=1, inplace=True)


# TODO: Delete major or boolean (hasMajorData)

# TODO: Sanitize (<= 100), discretize age
df["age"] = pd.to_numeric(df["age"])
df["age"][df["age"] > 99] = None
df["age"] = df["age"].fillna(df["age"].mean())

df["age"] = pd.cut(df["age"],
       bins=[0, 12, 18, 35, 60, np.Inf],
       labels=["Young", "Teenager", "Adult", "Seniors", "Elderly"])

# TODO: Discretize screenw, screenh. Phone, PC, monitor. 

# Height: 640 (mobile), 760 (tablet), 800 (pc), > monitor
# Width: 360 (mobile), 1020 (tablet), 1280 (pc), > monitor

df["screenw"] = pd.to_numeric(df["screenw"])

df["device"] = pd.cut(df["screenw"],
       bins=[0, 360, 760, 1280, np.Inf],
       labels=["Mobile", "Tablet", "PC", "Monitor"])

# TODO: Discretize class nerdiness (LOW, NORMAL, NERD, FREAK)


# TODO: Remove ASD
df.drop('ASD', axis=1, inplace=True)





ax = df["introelapse"].hist()
fig = ax.get_figure()
fig.savefig('figure.pdf')

df.to_csv('processed_data.csv', index=False)