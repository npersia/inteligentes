import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df["Radiation"] = pd.to_numeric(df["Radiation"])
df["Radiation"] = pd.cut(df["Radiation"],
       bins=[0,300,700,  5000],
       labels=["Low","Med","High"])

df['Rad'] = df['Radiation']

df.to_csv('initial_data.csv', index=False)