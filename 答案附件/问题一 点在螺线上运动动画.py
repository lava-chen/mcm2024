import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# 等距螺线
# 设置参数
pi = math.pi
a = 0  # 初始半径
b = 0.55 / 2 / pi  # 螺距参数
interval = 2
t0 = 2 * pi * 16
tn = 0

# 生成参数t的值，从0到10，足够多的点来绘制平滑的曲线
t = np.linspace(0, 2 * pi * 16, 10000)

# 计算阿基米德螺线的x和y坐标
x = (a + b * t) * np.cos(t)
y = (a + b * t) * np.sin(t)

# 绘制螺线
line, = ax.plot(x, y)
ax.set_title('Archimedean Spiral')
line.set_label("X label")
ax.grid(True)
ax.axis('equal')  # 确保x和y轴的刻度相同，以保持圆形

# 点动画
# 创建一个点的实例
points = []  # 存储点的坐标
point, = ax.plot([], [], 'bo', ms=10)  # 'bo' 表示蓝色圆圈


def init():
    point.set_data([], [])
    return point,


# 更新函数，用于动画的每一帧
def update(frame):
    global tn
    if frame - tn * interval >= 0:
        tn += 1
        points.append([(a + b * t0) * np.cos(t0), (a + b * t0) * np.sin(t0), tn])  # 将新点添加到列表中
    for p in points:
        t = t0 - frame + (p[2] - 1) * interval
        p[0] = (a + b * t) * np.cos(t)  # 假设点沿着x轴移动
        p[1] = (a + b * t) * np.sin(t)  # 点的y坐标是x坐标的2倍
        if t >t0:
            points.remove(p)
    point.set_data([p[0] for p in points], [p[1] for p in points])
    return point,


# 创建动画
ani = FuncAnimation(fig, update, frames=np.linspace(0, t0, 5000),
                    init_func=init, blit=True, interval=100)

# 保存动画
#ani.save('animation.gif', writer='ffmpeg', fps=120)
plt.show()
