from math import *
from numpy import degrees
theta_1 = 9*pi/1.7
a=1.7/(2*pi)
k = (sin(theta_1)+theta_1*cos(theta_1))/(cos(theta_1)-theta_1*sin(theta_1))
k_00 = -1/k
print("k,k_00:",k,k_00)

k_3 = tan(theta_1)
k_2 = fabs((k_3 - k_00)/(1+k_3*k_00))
print(k_3,k_2)

sin_theta_2 = k_00/sqrt(1+k_00**2)
cos_theta_2 = 1/sqrt(1+k_00**2)
cos_theta_0 = 1/sqrt(1+k_2**2)

r = 81/(54*cos_theta_0)
print(a*theta_1*cos(theta_1)**2+a*theta_1*sin(theta_1)**2,'    ',6*r)

print("r:",r)
x_o_1 = a*theta_1*cos(theta_1)+2*r*cos_theta_2
y_o_1 = a*theta_1*sin(theta_1)+2*r*sin_theta_2
print("o_1:",x_o_1,y_o_1)
x_o_2 = a*theta_1*cos(theta_1+pi)-r*cos_theta_2
y_o_2 = a*theta_1*sin(theta_1+pi)-r*sin_theta_2
print("o_2:",x_o_2,y_o_2)

k_12 = (y_o_1-y_o_2)/(x_o_1-x_o_2)


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

t = np.linspace(0, 2 * pi * 16, 10000) 
beta = 1.7 / (2 * pi) 

x = beta * t * np.cos(t)
y = beta * t * np.sin(t)

x1 = beta * t * np.cos(t+pi)
y1 = beta * t * np.sin(t+pi)

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
arc1 = Arc(circle1_center, 2 * r * 2, 2 * r * 2, angle=0, theta1=degrees(atan(k_12)), theta2=degrees(atan(k_00)+pi), color='purple', linewidth=2)
arc2 = Arc(circle2_center, 2 * r, 2 * r, angle=0, theta1=degrees(atan(k_00)+pi), theta2=degrees(atan(k_12)), color='purple', linewidth=2)
#-------------------------------
t = np.linspace(theta_1, 2 * pi * 16, 10000) 
beta = 1.7 / (2 * pi) 

x00 = beta * t * np.cos(t)
y00 = beta * t * np.sin(t)

x100 = beta * t * np.cos(t+pi)
y100 = beta * t * np.sin(t+pi)

line, = ax.plot(x00, y00,color='purple', linewidth=2)

line, = ax.plot(x100, y100,color='purple',linewidth=2)
#--------------------------------
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

ax.add_patch(arc1)
ax.add_patch(arc2)


ax.set_aspect('equal') 
ax.set_xlim(-10, 10)  
ax.set_ylim(-10, 10)  
ax.set_title('spiral & 2 circles')
ax.legend()  


plt.show()

