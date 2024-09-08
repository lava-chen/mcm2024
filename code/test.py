import pandas as pd
from math import *

df = pd.read_excel("result1.xlsx")
data_v = {}
for i in range(0,301):
    data_v[i]=[None]*224
for t in range(0,301):
    data_v[t][0] = 1
for t in range(1,301):
    for i in range(2,448,2):
        if df[f'{t} s'][i]!= None:
            x1 = df[f'{t} s'][i]
            x2 = df[f'{t-1} s'][i]
            y1 = df[f'{t} s'][i+1]
            y2 = df[f'{t-1} s'][i+1]
            data_v[t][int(i/2)] = sqrt((x1-x2)**2+(y1-y2)**2)
df =pd.DataFrame(data_v)
df.to_excel("A1_speed.xlsx")