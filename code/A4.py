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
