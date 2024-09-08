import pandas as pd
import numpy as np

# 读取Excel文件
file_path = 'result4.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 添加噪声的函数
def add_noise(value, noise_level=0.001):
    # 生成一个范围为[-noise_level, noise_level]的小数点后三位的随机噪声
    noise = np.random.uniform(-noise_level, noise_level)
    return value + round(noise, 3)

# 对所有数据添加噪声（仅对数值型数据进行操作）
df_noisy = df.applymap(lambda x: add_noise(x) if isinstance(x, (int, float)) else x)

# 将添加了噪声的数据保存到新的Excel文件中
df_noisy.to_excel('new_result4.xlsx', index=False)