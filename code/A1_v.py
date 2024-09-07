import pandas as pd
from math import *
from sympy import *

p = 0.55#螺距
aa = p/(2*pi)

df = pd.read_excel("result1.xlsx")
df_theta = pd.read_excel("theta_data.xlsx")
data_v = {}

for i in range(1,301): #创建速度输出数据架构
    data_v[f'{i} s']=[None]*224

print("1")#检验执行进度
#----------------------------definition----------------------->
def k(theta):#斜率计算函数
    return (aa*sin(theta)+aa*theta*cos(theta))/(aa*cos(theta)-aa*theta*sin(theta))

def n_basic(x,y):#计算单位向量的函数
    xe = x/sqrt(x**2+y**2)
    ye = y/sqrt(x**2+y**2)
    return [xe,ye]

def kToVector(k):
    xe = 1/sqrt(1+k**2)
    ye = k/sqrt(1+k**2)
    return [xe,ye]


#------------------------------running------------------------->
for t in range(1,301):
    data_v[f'{t} s'][0] = 1#都是1

print("2")

#写入速度程序
v_1 = 1#初始速度
for t in range(3,300):
    print("-------------",t)
    for i in range(2,362,2):
        #角度读取
        theta_i = df_theta[f'{t} s'][int(i/2)]
        theta_ii = df_theta[f'{t} s'][int(i/2)+1]
        k_i = k(theta_i)
        k_i_vec = kToVector(k_i)
        k_ii = k(theta_ii)
        k_ii_vec = kToVector(k_ii)
        if df[f'{t} s'][i] != None:
            x1=df[f'{t} s'][i]
            x2=df[f'{t} s'][i-2]
            y1=df[f'{t} s'][i+1]
            y2=df[f'{t} s'][i-1]
            print("xyxy:",x1,x2,y1,y2)
            n_s = n_basic(x1-x2,y1-y2)
            n_t = [n_s[1],-n_s[0]]
            print("n_s:",n_s,"n_t:",n_t,"k_i_vec:",k_i_vec)
            if n_s[0] == nan:
                break
            a = Symbol('a')
            b = Symbol('b')
            result = solve([a*n_s[0]+b*n_t[0]-v_1*k_i_vec[0],a*n_s[1]+b*n_t[1]-v_1*k_i_vec[1]],[a,b])
            print(result)
            a_r = result[a]
            v_2 = Symbol('v_2')
            c = Symbol('c')
            result_2 = solve([a_r*n_s[0]+c*n_t[0]-v_2*k_ii_vec[0],a_r*n_s[1]+c*n_t[1]-v_2*k_ii_vec[1]],[c,v_2])
            print(result_2)
            v_22 = result_2[v_2]
            data_v[f'{t} s'][int(i/2)] = v_22
            v_1 = v_22
            print(i)#检验进度
    v_1 =1
df = pd.DataFrame(data_v)
df.to_excel('A1_speed.xlsx')

