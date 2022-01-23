import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df["Radiation"] = pd.to_numeric(df["Radiation"])
df["Radiation"] = pd.cut(df["Radiation"],
       bins=[-np.inf, 3, 300, np.inf],
       labels=["Low","Med","High"])

df['Rad'] = df['Radiation']

df["Temperature"] = pd.to_numeric(df["Temperature"])
# df["Temperature"] = (df["Temperature"] - 32) * 5.0 / 9.0

df.to_csv('initial_data.csv', index=False)

# df.plot(x="Rad", y=["Temperature"], kind="bar")

# plot.show()