import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# 创建极坐标图
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# 等距螺线
# 设置参数
pi = math.pi
a = 0  # 初始半径
b = 0.55 / 2 / pi  # 螺距参数
beta = 11 / 40 / pi

# 生成参数t的值，从0到10，足够多的点来绘制平滑的曲线
t = np.linspace(0, 2 * pi * 16, 10000)

# 计算阿基米德螺线的x和y坐标
x = (a + b * t) * np.cos(t)
y = (a + b * t) * np.sin(t)

# 绘制螺线
line, = ax.plot(x, y, linewidth=3)
ax.set_title('Archimedean Spiral')
line.set_label("X label")
ax.grid(True)
ax.axis('equal')  # 确保x和y轴的刻度相同，以保持圆形
pi = np.pi
n = 32

xs = []
ys = []
last = 0
t0 = 8 * math.sqrt((11 / 5) * (2048 * math.pi ** 3 + 2 * math.pi))
step = 6.759659698263022
for t in np.arange(t0, t0 - (step) * 301, -step):
    if t > 0:
        theta = np.sqrt((np.sqrt(1 + 4 * t * t / beta) - 1) / 2)
    if t == 0:
        theta = 0
    r = beta * (theta)  # 半径随角度线性增加
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    xs.append(x)
    ys.append(y)
    print("第"+str(((t0 - t)/step).round(0))+"秒:", ((x.round(6)+1e-8).round(6), (y.round(6)+1e-8).round(6)))
    # print(((r*np.cos(theta)).round(2),(r*np.sin(theta)).round(2)),end="")
    # if not (t+1)%10:
    # print()
# 绘制极坐标图
plt.plot(xs, ys, 'o', linestyle="")

# 设置极坐标图的属性
# plt.suptitle("Spiral in Polar Coordinates")

plt.show()
