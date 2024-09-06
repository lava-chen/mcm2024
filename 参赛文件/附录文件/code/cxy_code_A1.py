import matplotlib.pyplot as plt
from scipy import optimize
from math import *
import pandas as pd

a = 0.04376761
b = 442.5902564
l_x = []
l_y = []
l_wtf = []
l_theta =[]
for i in range(0,301):
    def func_1(x):
        return b-a*(x*sqrt(1+x**2)+log(x+sqrt(1+x**2)))-i
    lbeta = optimize.fsolve(func_1,1)
    theta = lbeta[0]
    wtf = func_1(theta)
    x = 2*a*theta*cos(theta)
    y = 2*a*theta*sin(theta)
    print(i,':',x,y,wtf)
    l_theta.append(theta)
    l_x.append(x)
    l_y.append(y)
    l_wtf.append(wtf)

def func_2(d,theta):
    def p_x(_):
        return 2*a*_*cos(_)
    def p_y(_):
        return 2*a*_*sin(_)
    def f(ct):
        return sqrt((p_x(theta)-p_x(ct))**2+(p_y(theta)-p_y(ct))**2)-d
    solution = optimize.fsolve(f,theta)
    theta_2 = solution[0]
    ls_f2 = []
    ls_f2.append(p_x(theta_2))
    ls_f2.append(p_y(theta_2))
    ls_f2.append("a")
    ls_f2.append(theta_2)
    if theta_2>32*pi:
        ls_f2[2]=0
    return ls_f2
data = {}
for i in range(1,301):
    print(i)
    data[f'{i} s']=[None]*448
for t in range(1,301):
    print(t)
    data[f'{t} s'][0] = l_x[t]
    data[f'{t} s'][1] = l_y[t]
    if func_2(2.86,l_theta[t])[2] != 0:
        data[f'{t} s'][2] = func_2(2.86,l_theta[t])[0]
        data[f'{t} s'][3] = func_2(2.86,l_theta[t])[1]
    cc = func_2(2.86,l_theta[t])[3]
    for j in range(4,448,2):
        if func_2(1.65,cc)[2] != 0:
            data[f'{t} s'][j] = func_2(2.86,l_theta[t])[0]
            data[f'{t} s'][j+1] = func_2(2.86,l_theta[t])[1]
        cc = func_2(1.65,cc)[3]
df = pd.DataFrame(data)
df.to_excel('export.xlsx')



