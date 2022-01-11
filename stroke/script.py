import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df.drop('id', axis=1, inplace=True)

# heart_disease

df["age"] = pd.to_numeric(df["age"])

df["age"] = pd.cut(df["age"],
       bins=[0,35, np.Inf],
       labels=["Not Risky", "Risky"])

df["avg_glucose_level"] = pd.to_numeric(df["avg_glucose_level"])

df["avg_glucose_level"] = pd.cut(df["avg_glucose_level"],
       bins=[0, 70, 140, np.Inf],
       labels=["Low", "Medium", "High"])

df["bmi"][df["bmi"] == "N/A"] = None

df["bmi"] = pd.to_numeric(df["bmi"])

df["bmi"] = df["bmi"].fillna(df["bmi"].mean())

df["bmi"] = pd.cut(df["bmi"],
       bins=[0, 18.5, 24.9, 25, 30, np.Inf],
       labels=["Very Low", "Low", "Healthy", "OverWeight", "Obesity"])

# stroke

df.to_csv('processed_data.csv', index=False)