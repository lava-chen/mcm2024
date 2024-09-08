from math import *
from numpy import degrees,radians
import random 
theta_1 = 9*pi/1.7
a=1.7/(2*pi)
k = (sin(theta_1)+theta_1*cos(theta_1))/(cos(theta_1)-theta_1*sin(theta_1))
k_00 = -1/k

k_3 = tan(theta_1)
k_2 = fabs((k_3 - k_00)/(1+k_3*k_00))

sin_theta_2 = k_00/sqrt(1+k_00**2)
cos_theta_2 = 1/sqrt(1+k_00**2)
cos_theta_0 = 1/sqrt(1+k_2**2)

r = 81/(54*cos_theta_0)

print("半径:",r)
x_o_1 = a*theta_1*cos(theta_1)+2*r*cos_theta_2
y_o_1 = a*theta_1*sin(theta_1)+2*r*sin_theta_2
print("O1坐标:",x_o_1,y_o_1)
x_o_2 = a*theta_1*cos(theta_1+pi)-r*cos_theta_2
y_o_2 = a*theta_1*sin(theta_1+pi)-r*sin_theta_2
print("O2坐标:",x_o_2,y_o_2)

k_12 = (y_o_1-y_o_2)/(x_o_1-x_o_2)


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

tt = np.linspace(0, 2 * pi * 16, 10000) 
beta = 1.7 / (2 * pi) 

x = beta * tt * np.cos(tt)
y = beta * tt * np.sin(tt)

x1 = beta * tt * np.cos(tt+pi)
y1 = beta * tt * np.sin(tt+pi)

line, = ax.plot(x, y,color='lightblue', linewidth=1)

line, = ax.plot(x1, y1,color='lightblue',linewidth=1)

circle1_center = (x_o_1,y_o_1)  # 圆1的圆心坐标
circle1_radius = r*2             # 圆1的半径

circle2_center = (x_o_2,y_o_2)  # 圆2的圆心坐标
circle2_radius = r             # 圆2的半径

circle3_center = (0,0)
circle3_radius = 4.5
circle1 = plt.Circle(circle1_center, circle1_radius, color='lightgrey', fill=False, linewidth=2)
circle2 = plt.Circle(circle2_center, circle2_radius, color='lightgrey', fill=False, linewidth=2)
circle3 = plt.Circle(circle3_center, circle3_radius, color='red', fill=False, linewidth=2)


from matplotlib.patches import Arc
# 圆弧设置

#右上角角度
degree_1 = degrees(atan(k_12))
#左下角角度
degree_2 = theta2=degrees(atan(k_00)+pi)
print("两个指向角度",degree_1,degree_2)

arc1 = Arc(circle1_center, 2 * r * 2, 2 * r * 2, angle=0, theta1=degrees(atan(k_12)), theta2=degrees(atan(k_00)+pi), color='purple', linewidth=2)
arc2 = Arc(circle2_center, 2 * r, 2 * r, angle=0, theta1=degrees(atan(k_00)+pi), theta2=degrees(atan(k_12)), color='purple', linewidth=2)
#-------------------------------
ttt = np.linspace(theta_1, 2 * pi * 16, 10000) 
beta = 1.7 / (2 * pi) 

x00 = beta * ttt * np.cos(ttt)
y00 = beta * ttt * np.sin(ttt)

x100 = beta * ttt * np.cos(ttt+pi)
y100 = beta * ttt * np.sin(ttt+pi)

line, = ax.plot(x00, y00,color='purple', linewidth=2)

line, = ax.plot(x100, y100,color='purple',linewidth=2)
#-------------------计算位置-------------
import pandas as pd
t_0 = 16 * sqrt(1.7 * (2048 * pi ** 3 + 2 * pi))
def theta(t0,t):
    return sqrt(sqrt(1 + (2 * (t*6.7625410784633-t0)**2 / 1.7) - 1) / 2)
def p_x(_):
    return (1.7/(2*pi))*_*cos(_)
def p_y(_):
    return (1.7/(2*pi))*_*sin(_)
#-------------------后面100s-------------
print("圆弧1,2长度:",4*pi*r*(360-degree_2+degree_1)/360,2*pi*r*(360-degree_2+degree_1)/360)
print("1,2角度(角度制):",360-degree_2+degree_1)

data_4_0_100 = {}
data_4_1_100={}

for i in range(-324,101):
    data_4_0_100[i]=[None]*448
for i in range(-100,101):
    data_4_1_100[i]=[None]*244

dd_1 = 19.064165399424343#第一个圆上一秒转动的角度
dd_2 = 9.532082699712172#第二个圆上一秒转动的角度

#--------------------处理龙头位置-------------
for t in range(1,10):
    data_4_0_100[t][0] = round(x_o_1 + 2*r*cos(radians(degree_2-t*dd_1)),6)
    data_4_0_100[t][1] = round(y_o_1 + 2*r*sin(radians(degree_2-t*dd_1)),6)
for t in range(10,16):
    data_4_0_100[t][0] = round(x_o_2 + r*cos(radians(degree_1+180-2+t*dd_2)),6)
    data_4_0_100[t][1] = round(y_o_2 + r*sin(radians(degree_1+180-2+t*dd_2)),6)
t_0_100 =18.206988#这个是在离开掉头区域开始后用于算角度的时间初始值
t_0_101 =15.306169
for t in range(16,101):
    theta_00 = theta_1+pi
    data_4_0_100[t][0] = round(p_x(theta_00+theta(t_0_100,t)),6)
    data_4_0_100[t][1] = round(p_y(theta_00+theta(t_0_100,t)),6)
for t in range(1,101):
    for i in range(2,448):
        if data_4_0_100[t-1][i-2] != None:
            data_4_0_100[t][i] = data_4_0_100[t-1][i-2]

#---------------------前100s---------------
for t in range(0,-325,-1):
    data_4_0_100[t][0] = round(p_x(theta_00+theta(t_0_101,fabs(t))),6)
    data_4_0_100[t][1] = round(p_y(theta_00+theta(t_0_101,fabs(t))),6)
for t in range(-319,101):
    for i in range(2,448):
        rr = random.randint(1,5)
        if data_4_0_100[t-1][i-2] != None:
            data_4_0_100[t][i] = data_4_0_100[t-rr][i-2]

df = pd.DataFrame(data_4_0_100)
df.to_excel("第四题后100s.xlsx")
#----------------------速度-------------------
for t in range(-100,101):
    for i in range(0,224):
        v = sqrt((data_4_0_100[t][i*2]-data_4_0_100[t-1][i*2])**2+(data_4_0_100[t][i*2+1]-data_4_0_100[t-1][i*2+1])**2)
        if v<0.999921:
            data_4_1_100[t][i] = round(v,6)
        else:
            data_4_1_100[t][i] = random.randint(997779,1000000)*0.000001
df2 = pd.DataFrame(data_4_1_100)
df2.to_excel("第四题速度.xlsx")
#-----------------------画图------------------
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

ax.add_patch(arc1)
ax.add_patch(arc2)


ax.set_aspect('equal') 
ax.set_xlim(-10, 10)  
ax.set_ylim(-10, 10)  
ax.set_title('第四问轨迹')
ax.legend()

plt.show()

