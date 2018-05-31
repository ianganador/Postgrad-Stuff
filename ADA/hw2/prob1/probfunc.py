#Graphing the Poisson Distribution
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y= x*np.exp(-x)

plt.plot(x,y)
plt.xlabel('R')
plt.ylabel('P(R)')
plt.legend()

plt.savefig('probfunc.png')
