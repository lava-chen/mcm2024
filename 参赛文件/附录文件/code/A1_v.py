import pandas as pd
from math import *

df = pd.read_excel("export.xlsx")
data_v = {}
for i in range(1,301):
    data_v[f'{i} s']=[None]*224


print("1")
for t in range(1,301):
    data_v[f'{t} s'][0] = 1


print("2")
for t in range(3,300):
    for i in range(2,362,2):


        print(i)
        if df[f'{t} s'][i] != None:
            x1=df[f'{t} s'][i]
            x2=df[f'{t+1} s'][i]
            y1=df[f'{t} s'][i+1]
            y2=df[f'{t+1} s'][i+1]
            data_v[f'{t} s'][int(i/2)] = sqrt((x1-x2)**2+(y1-y2)**2)
df = pd.DataFrame(data_v)
df.to_excel('export2.xlsx')