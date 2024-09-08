from math import *
import pandas as pd

a=0.55/(2*pi)
t_0 = 8*sqrt(11*(2048*pi**3+2*pi)/5)
def thetaa(t):
    return 32*pi-sqrt((sqrt(1+4*(t_0-t)**2/0.55)-1)/2)
t_2 = 412.3319325500
t_3 = 413.3319325500
t_1 = 411.3319325500

def p_x(_):
    return 2*a*_*cos(_)
def p_y(_):
    return 2*a*_*sin(_)

# 计算龙头位置
data_r = {}
data_r['x']=[None]*224
data_r['y']=[None]*224
data_r['v']=[None]*224

data_r['x'][0]=p_x(thetaa(t_2))
data_r['y'][0]=p_y(thetaa(t_2))

def v_r(x1,x2,y1,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)





df = pd.DataFrame(data_r)
df.to_excel("A2_result.xlsx")