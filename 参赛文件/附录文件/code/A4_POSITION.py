from math import *

theta_1 = 9*pi/1.7
a=1.7/(2*pi)
k = (a*sin(theta_1)+a*theta_1*cos(theta_1))/(a*cos(theta_1)-a*theta_1*sin(theta_1))
k_2 = -1/k
sin_theta_2 = k_2/sqrt(1+k_2**2)
cos_theta_2 = 1/sqrt(1+k_2**2)
r = 81/(54*cos_theta_2)
print("r:",r)
x_o_1 = a*theta_1*cos(theta_1)+2*r*cos_theta_2
y_o_1 = a*theta_1*sin(theta_1)+2*r*sin_theta_2
print("o_1:",x_o_1,y_o_1)
x_o_1 = a*theta_1*cos(theta_1+pi)-r*cos_theta_2
y_o_1 = a*theta_1*sin(theta_1+pi)-r*sin_theta_2
print("o_2:",x_o_1,y_o_1)
alpha  = pi - acos((9*cos_theta_2-3*r)/3*r)
print("alpha:",alpha)