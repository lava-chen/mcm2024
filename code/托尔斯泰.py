from math import *
import numpy as np
theta_1 = 9*pi/1.7
print(442.5902564*1.7/0.55-(1.7/(4*pi))*(theta_1*sqrt(1+theta_1**2)+log(theta_1+sqrt(1+theta_1**2))))
print("一次经过的度数",1/9.802766194309257*186.88155610019717)
print("一次经过的度数2",0.5/9.802766194309257*186.88155610019717)

print("t:",round(sqrt(1.7/4*((2*theta_1**2-1)-1)),6))
print("t2:",round(sqrt(1.7/4*((2*(theta_1+pi)**2-1)-1)),6))