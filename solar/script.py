import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


data = pd.read_csv("data.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode') 

df = pd.DataFrame(data)

df.drop('Data', axis=1, inplace=True)
df.drop('Time', axis=1, inplace=True)


df['UNIXTime'] = (pd.to_datetime(df['UNIXTime'],unit='s') + timedelta(hours = -10))

#__Date = []
__time = []
__sunrise = []
__sunset = []
for i in range(len(df["UNIXTime"])):
    date = df["UNIXTime"][i]
    #__Date.append(str(date.day).rjust(2, '0')+'/'+str(date.month).rjust(2, '0'))
    __time.append(str(date.hour).rjust(2, '0'))

    __sunrise.append(str(df["TimeSunRise"][i].split(":")[1]).rjust(2, '0'))
    __sunset.append(str(df["TimeSunSet"][i].split(":")[1]).rjust(2, '0'))
    df["Temperature"][i] = (float(df["Temperature"][i]) - 32) * 5.0 / 9.0

    # df["Pressure"][i] = str(df["Pressure"][i].split(".")[1]).ljust(2, '0')

#df['Date'] = __Date
df['Hour'] = __time
df['SunRise'] = __sunrise
df['SunSet'] = __sunset


df["MomentOfDay"] = pd.to_numeric(df["Hour"])
df["MomentOfDay"] = pd.cut(df["MomentOfDay"],
       bins=[-np.inf,6,11,16,20,24],
       labels=["Night","Morning","Midday","Afternoon","Night"],
                    ordered=False)


df["SunRise"] = pd.to_numeric(df["SunRise"])
df["SunRise"] = pd.cut(df["SunRise"],
       bins=[0,20,40,60],
       labels=["6:00-6:20","6:20-6:40","6:40-7:00"])

df["SunSet"] = pd.to_numeric(df["SunSet"])

for i in range(len(df["SunSet"])):
       if df["SunSet"][i] >= 40:
              df["SunSet"][i] -= 60

df["SunSet"] = pd.cut(df["SunSet"],
       bins=[-20,0,20,40],
       labels=["17:40-18:00","18:20-18:40","18:40-19:00"])


df["UNIXTime"] = pd.to_numeric(df["UNIXTime"])

df["month"] = pd.cut(df["UNIXTime"],
       bins=[1472698800000000000 , 1475290800000000000 , 1477969200000000000 , 1480561200000000000, 1483239600000000000],
       labels=["Sep", "Oct", "Nov", "Dec"])

df["WindDirection(Degrees)"] = pd.to_numeric(df["WindDirection(Degrees)"])
df["WindDirection(Degrees)"] = pd.cut(df["WindDirection(Degrees)"],
       bins=[0,45,135,225,315,360],
       labels=["N","E","S","W","N"],
       ordered=False)

df["Radiation"] = pd.to_numeric(df["Radiation"])
df["Radiation"] = pd.cut(df["Radiation"],
       bins=[-np.inf, 3, 300, np.inf],
       labels=["Low","Med","High"])


df["Temperature"] = pd.to_numeric(df["Temperature"])
df["Temperature"] = pd.cut(df["Temperature"],
       bins=[-np.inf, 9, 12, np.inf],
       labels=["Cold","Normal","Heat"])


df["Pressure"] = pd.to_numeric(df["Pressure"])
df["Pressure"] = pd.cut(df["Pressure"],
       bins=[-np.inf, 30.415, 30.445, np.inf],
       labels=["Low", "Normal", "High"])


df["Humidity"] = pd.to_numeric(df["Humidity"])
df["Humidity"] = pd.cut(df["Humidity"],
       bins=[-np.inf, 60, 90, np.inf],
       labels=["Low", "Normal", "High"])

df["Speed"] = pd.to_numeric(df["Speed"])
df["Speed"] = pd.cut(df["Speed"],
       bins=[-np.inf, 5, 8, np.inf],
       labels=["Slow", "Normal", "Fast"])


df['Rad'] = df['Radiation']
#df = df.drop(df[df.Rad == "0-100"].index)
df.drop('UNIXTime', axis=1, inplace=True)
df.drop('TimeSunRise', axis=1, inplace=True)
df.drop('TimeSunSet', axis=1, inplace=True)
df.drop('Radiation', axis=1, inplace=True)

df.to_csv('processed_data.csv', index=False)