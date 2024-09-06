import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# 创建极坐标图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
pi = np.pi
n=32
# 定义角度和半径
t = np.concatenate((np.linspace(0,50, 10000),np.linspace(50,8*np.sqrt(11/5*(2048*pi**3+2*pi)),10000)))
#math.sqrt(((2*n*n*pi*pi+1)**2-1)*11/160/pi)
beta = 11 / 40 / pi
theta = 32*pi-np.sqrt((np.sqrt(1 + 4 * t * t / beta) - 1) / 2)
r = beta * theta  # 半径随角度线性增加

# 绘制极坐标图
ax.plot(theta, r, 'b-')

# 设置极坐标图的属性
ax.set_title("Spiral in Polar Coordinates")
ax.set_ylim(0, 10)  # 设置半径的显示范围

plt.show()
