from sympy import *
a = Symbol('a')
b = Symbol('b')
res = solve([a+b-1,a-b+5],[a,b])
print(res[a])