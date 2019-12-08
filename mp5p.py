import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi
n=np.linspace(0,199,200)
x=eval(input())
m=np.size(x)
y=np.linspace(0,199,200)
for i in range (200):
    if y[i]==0:
        y[i]=-1.5*x[i]+2*x[i+1]-0.5*x[i+2]
    elif y[i]<=198 and y[i]>0:
        y[i]=0.5*x[i+1]-0.5*x[i+-1]
    elif y[i]==199:
        y[i]=1.5*x[i]-2*x[i-1]+0.5*x[i-2]
plt.plot(x,'r',label='x(n)')
plt.plot(y,'k',label='x(n)')
plt.title('Graphs of x(n) and y(n)')
plt.legend()