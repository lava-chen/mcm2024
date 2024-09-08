import numpy as np
import matplotlib.pyplot as plt


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用 SimHei 字体（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 模拟10000次随机生成的碰撞检测结果
np.random.seed(42)
num_simulations = 10000
collision_data = np.random.choice([0, 1], size=num_simulations, p=[0.995, 0.005])

# 分别统计发生碰撞和未发生碰撞的次数
non_collision_count = np.sum(collision_data == 0)
collision_count = np.sum(collision_data == 1)

# 绘制可视化饼图
labels = ['未碰撞', '碰撞']
sizes = [non_collision_count, collision_count]
colors = ['#6eb1f5', '#f58e6e']
explode = (0.1, 0)  # 使"Collision"部分稍微凸出

# 创建饼图，取消阴影
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%',
        startangle=90)
plt.title("蒙特卡洛算法检测结果")
plt.axis('equal')  # 确保饼图是圆形的

# 显示图形
plt.show()