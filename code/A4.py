import numpy as np
from scipy.optimize import minimize

# 定义函数
def s_func(x, d, R):
    # 确保x在[-1, 1]的范围内
    if x < -1 or x > 1:
        return np.inf
    y = (d - 4 * R * x) / R
    # 确保y在[-1, 1]的范围内
    if y < -1 or y > 1:
        return np.inf
    alpha = 2 * np.arcsin(y)
    beta = 2 * np.arcsin(x)
    return 2 * alpha * R + beta * R

# 参数
d = 10  # 假设固定的d值
R = 3   # 假设固定的R值

# 最小化函数
result = minimize(lambda x: s_func(x, d, R), 0.5, bounds=[(-1, 1)])
print(f"最小路径长度 s: {result.fun}")
print(f"对应的 x: {result.x[0]}")
import numpy as np
import matplotlib.pyplot as plt

# 参数设置
R = 3  # 半径
d = 10  # AB长度
alpha = np.pi / 4  # 示例角度 alpha
beta = np.pi / 2   # 示例角度 beta

# 计算圆心坐标
O1 = (0, 0)  # 圆心 O1 位于原点
O2 = (d, 0)  # 假设第二个圆心在x轴上，距离为d

# 第一段圆弧的起点和终点
theta1 = np.linspace(0, 2 * alpha, 100)  # 角度范围从 0 到 2α
x1 = O1[0] + R * np.cos(theta1)
y1 = O1[1] + R * np.sin(theta1)

# 第二段圆弧的起点和终点
theta2 = np.linspace(-beta / 2, beta / 2, 100)  # 角度范围从 -β/2 到 β/2
x2 = O2[0] + R * np.cos(theta2)
y2 = O2[1] + R * np.sin(theta2)

# 绘制圆弧
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x1, y1, label='第一段圆弧 (2α)', color='blue')
ax.plot(x2, y2, label='第二段圆弧 (β)', color='green')

# 绘制圆心和AB
ax.plot([O1[0], O2[0]], [O1[1], O2[1]], 'k--', label='AB长度')
ax.plot(O1[0], O1[1], 'ro')  # 圆心 O1
ax.plot(O2[0], O2[1], 'ro')  # 圆心 O2

# 设置图形属性
ax.set_aspect('equal')  # 确保比例正确
ax.legend()
ax.grid(True)
plt.title('掉头路径的几何关系示意图')
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 显示图形
plt.show()
