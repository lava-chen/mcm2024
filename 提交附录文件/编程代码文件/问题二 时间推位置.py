import numpy as np
import math
import pandas as pd


data=pd.read_excel("./附件/result2.xlsx",index_col=0)
xys = []
for i in range(224):
    xys.append([])
# 设置参数
pi = math.pi
a = 0  # 初始半径
b = 0.55 / 2 / pi  # 螺距参数
beta = 11 / 40 / pi
n = 32

xs = []
ys = []
last = 0
t0 = 8 * math.sqrt((11 / 5) * (2048 * math.pi ** 3 + 2 * math.pi))
step = 6.759659698263022

for i in range(0, 224):
    ti =2.86 + (i - 1) * 1.65
    if not i :ti=0
    j=399.122775304
    t0 = 8 * math.sqrt((11 / 5) * (2048 * math.pi ** 3 + 2 * math.pi)) + (ti - j) * step
    theta = np.sqrt((np.sqrt(1 + 4 * t0 * t0 / beta) - 1) / 2)
    r = beta * (theta)  # 半径随角度线性增加
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    xys[i].append(((x.round(6) + 1e-8).round(6), (y.round(6) + 1e-8).round(6)))

for i in range(0,224):
    data.iloc[i,0]=xys[i][0][0]
    data.iloc[i, 1] = xys[i][0][1]
data.to_excel("result2.xlsx")
