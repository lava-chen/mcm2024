import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import math

# 9070972166
# 399.122775304

fig, ax = plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
width = 2.2
length = 0.3
width0 = 3.41

# 设置参数
pi = math.pi
a = 0  # 初始半径
b = 1.7  # 螺距长度
t0 = 16 * math.sqrt(b * (2048 * math.pi ** 3 + 2 * math.pi))
step = 6.759659698263022
# maxFrame=1000000000 高精度
# minFrame = 907097200

maxFrame = 1000  # 低精度
minFrame = 1
beta = b / 2 / pi
Time = 440
nPoint = 0
rects = []

# 生成参数t的值，从0到10，足够多的点来绘制平滑的曲线
t = np.linspace(0, 2 * pi * 16, 10000)
x = (a + beta * t) * np.cos(t)
y = (a + beta * t) * np.sin(t)
line, = ax.plot(x, y,linewidth=0.5,zorder=3)
ax.set_title('问题二 防碰撞动态仿真模型',fontsize=20)
ax.grid(True)
ax.axis('equal')
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

# 点动画
points = [[(a + beta * t0) * np.cos(t0), (a + beta * t0) * np.sin(t0), t0, 0]]
point, = ax.plot([], [], 'bo', ms=2)
text = ax.text(0, 1.03, '', transform=ax.transAxes)
text.set_fontsize(10)

def is_collision(n):
    midpoint1 = ((points[0][0] + points[1][0]) / 2,
                 (points[0][1] + points[1][1]) / 2)
    midpoint2 = ((points[n][0] + points[n + 1][0]) / 2,
                 (points[n][1] + points[n + 1][1]) / 2)
    dx = points[1][0] - points[0][0]
    dy = points[1][1] - points[0][1]
    angle1 = math.atan2(dy, dx) * 180 / np.pi
    dx = points[n][0] - points[n + 1][0]
    dy = points[n][1] - points[n + 1][1]
    angle2 = math.atan2(dy, dx) * 180 / np.pi
    rect1_cv2 = (midpoint1, (width0, length), angle1 % 360)
    rect2_cv2 = (midpoint2, (width, length), angle2 % 360)
    intersection = cv2.rotatedRectangleIntersection(rect1_cv2, rect2_cv2)
    if intersection[1] is not None:
        return True
    return False


def init():
    point.set_data([], [])
    return point, rects, text,


def update(frame):
    global nPoint, text
    for i in range(2, len(rects)):
        if is_collision(i):
            print(frame)
            return
    text.set_text("时间: 第" +str(int((frame / maxFrame) * Time))+"s")
    text.set_position((0, 1.03))
    while Time * (frame - 1) / maxFrame > 2.86 + 1.65 * nPoint and len(points) <= 224:
        points.append([(a + beta * t0) * np.cos(t0), (a + beta * t0) * np.sin(t0),
                       16 * math.sqrt(b * (2048 * math.pi ** 3 + 2 * math.pi)) + step *
                       (2.86 + 1.65 * nPoint), nPoint])
        midpoint = ((points[len(points) - 1][0] + points[len(points) - 2][0]) / 2,
                    (points[len(points) - 1][1] + points[len(points) - 2][1]) / 2)
        if nPoint == 0:
            rects.append(patches.Rectangle(midpoint, width0, length, edgecolor='#d02200', facecolor='#ff8b18',zorder=4))
        else:
            rects.append(patches.Rectangle(midpoint, width, length, edgecolor='blue', facecolor='lightblue',zorder=2))
        ax.add_patch(rects[len(rects) - 1])
        nPoint += 1
    for p in points:
        t = p[2] - step * ((Time) * (frame - 1) / maxFrame)
        theta = np.sqrt((np.sqrt(1 + 4 * t * t / beta) - 1) / 2)
        p[0] = (a + beta * theta) * np.cos(theta)
        p[1] = (a + beta * theta) * np.sin(theta)
        if t <= 0:
            print(t)
            points.remove(p)
    point.set_data([p[0] for p in points], [p[1] for p in points])
    for r in range(len(rects)):
        dx = points[r + 1][0] - points[r][0]
        dy = points[r + 1][1] - points[r][1]
        angle = math.atan2(dy, dx)
        midpoint = ((points[r + 1][0] + points[r][0] + length * np.sin(angle) - width * np.cos(angle)) / 2,
                    (points[r + 1][1] + points[r][1] - np.cos(angle) * (length + width * np.tan(angle))) / 2)
        if r == 0:
            midpoint = ((points[r + 1][0] + points[r][0] + length * np.sin(angle) - width0 * np.cos(angle)) / 2,
                        (points[r + 1][1] + points[r][1] - np.cos(angle) * (length + width0 * np.tan(angle))) / 2)
        angle = angle * 180 / np.pi
        rects[r].set_xy(midpoint)
        rects[r].set_angle(angle)
    return point, rects, text,


ani = FuncAnimation(fig, update, frames=np.linspace(minFrame, maxFrame, maxFrame - minFrame + 1),
                    init_func=init, interval=1)
plt.show()
