import numpy as np
import math
import pandas as pd

# indexs = []
# for index in range(0, 223):
#     if index == 0:
#         indexs.append("龙头x (m)")
#         indexs.append("龙头y (m)")
#     elif index == 222:
#         indexs.append("龙尾x (m)")
#         indexs.append("龙尾y (m)")
#         indexs.append("龙尾（后）x (m)")
#         indexs.append("龙尾（后）y (m)")
#     else:
#         indexs.append("第" + str(index) + "节龙身x (m)")
#         indexs.append("第" + str(index) + "节龙身y (m)")
# data = pd.DataFrame({}, index=indexs)
data=pd.read_excel("./附件/result1.xlsx",index_col=0)
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
6.7625410784633
for t in np.arange(t0, t0 - (step) * 301, -step):
    theta = np.sqrt((np.sqrt(1 + 4 * t * t / beta) - 1) / 2)
    r = beta * (theta)  # 半径随角度线性增加
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    xys[0].append(((x.round(6) + 1e-8).round(6), (y.round(6) + 1e-8).round(6)))
    # print("第" + str(((t0 - t) / step).round(0)) + "秒:", ((x.round(6) + 1e-8).round(6), (y.round(6) + 1e-8).round(6)))
for i in range(1, 224):
    ti = 2.86 + (i - 1) * 1.65
    for j in range(301):
        if j < ti:
            xys[i].append((8.8, round((ti - j), 6)))
        else:
            t0 = 8 * math.sqrt((11 / 5) * (2048 * math.pi ** 3 + 2 * math.pi)) + (ti - j) * step
            for t in np.arange(t0, t0 - (step) * (301 - j), -step):
                theta = np.sqrt((np.sqrt(1 + 4 * t * t / beta) - 1) / 2)
                r = beta * (theta)  # 半径随角度线性增加
                x = r * np.cos(theta)
                y = r * np.sin(theta)
                xys[i].append(((x.round(6) + 1e-8).round(6), (y.round(6) + 1e-8).round(6)))
            break

print(data.shape)
for i in range(448):
    for j in range(301):
        data.iloc[i,j]=xys[int(i/2)][j][int((i/2-int(i/2))*2)]
data.to_excel("result1.xlsx")
