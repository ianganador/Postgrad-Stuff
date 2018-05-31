import numpy as np
import matplotlib.pyplot as plt
import matplotlib

data1=np.loadtxt("monteavesample.dat")
data2=np.loadtxt("montemedsample.dat")
stev1=np.zeros(len(data1))
stev2=np.zeros(len(data2))
N=np.zeros(len(data1))
for i in range(len(data1)):
	stev1[i]=data1[i,0]
	stev2[i]=data2[i,0]
	N[i]=data1[i,1]
print np.ave(stev1)
plt.plot(N,stev1, label="stdev mean")
plt.plot(N,stev2, label="stdev median")
plt.legend()
#plt.yscale('log')
#plt.xscale('log')
#plt.show()
