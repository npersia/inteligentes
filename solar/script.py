import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df.drop('Data', axis=1, inplace=True)
df.drop('Time', axis=1, inplace=True)


df['UNIXTime'] = (pd.to_datetime(df['UNIXTime'],unit='s') + timedelta(hours = -10))

__Date = []
__time = []
__sunrise = []
__sunset = []
for i in range(len(df["UNIXTime"])):
    date = df["UNIXTime"][i]
    __Date.append(str(date.day).rjust(2, '0')+'/'+str(date.month).rjust(2, '0'))
    __time.append(str(date.hour).rjust(2, '0')+':'+str(date.minute).rjust(2, '0'))

    __sunrise.append(str(df["TimeSunRise"][i].split(":")[1]).rjust(2, '0'))
    __sunset.append(str(df["TimeSunSet"][i].split(":")[1]).rjust(2, '0'))
    df["Temperature"][i] = (float(df["Temperature"][i]) - 32) * 5.0 / 9.0

    df["Pressure"][i] = str(df["Pressure"][i].split(".")[1]).ljust(2, '0')


df['Date'] = __Date
df['Hour'] = __time
df['SunRise'] = __sunrise
df['SunSet'] = __sunset



df["Radiation"] = pd.to_numeric(df["Radiation"])
df["Radiation"] = pd.cut(df["Radiation"],
       bins=[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
       labels=["0","100", "200", "300", "400", "500", "600", "700", "800", "900"])

df["Temperature"] = pd.to_numeric(df["Temperature"])
df["Temperature"] = pd.cut(df["Temperature"],
       bins=[0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 50],
       labels=["0", "2.5", "5", "7.5", "10", "12.5", "15", "17.5", "20"])


df["Pressure"] = pd.to_numeric(df["Pressure"])
df["Pressure"] = pd.cut(df["Pressure"],
       bins=[0, 20, 25, 30, 35, 40, 45, 50, 55, 60],
       labels=["0", "20", "25", "30", "35", "40", "45", "50", "55"])


df["Humidity"] = pd.to_numeric(df["Humidity"])
df["Humidity"] = pd.cut(df["Humidity"],
       bins=[0, 20, 40, 60, 80, 200],
       labels=["0", "20", "40", "60", "80"])

df["Speed"] = pd.to_numeric(df["Speed"])
df["Speed"] = pd.cut(df["Speed"],
       bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 100],
       labels=["0", "5", "10", "15", "20", "25", "30", "35", "40", "45"])
df.to_csv('processed_data.csv', index=False)