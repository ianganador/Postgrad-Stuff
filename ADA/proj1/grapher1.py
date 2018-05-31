import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read in data
spec, MJD,Time,DwellT,Background,CountRate,ErrorBar= np.loadtxt("qpo.dat", unpack=True)

#set gaussian threshold
tau=12
length=len(Time)

#define gaussian memory function for each time
def gauss(tk,ti,sigma):
	return np.exp(-.5*((tk-ti)/tau)**2.)/sigma**2.

#weight array for each data point's weight at different time values
w=np.zeros((length,length))
for i in range(length):
	for k in range(length):
		w[i][k]=gauss(Time[k],Time[i], ErrorBar[k])
		
#optimal averaging
Xopt=np.zeros(length)
Xopt=[np.sum(CountRate*w[i])/np.sum(w[i]) for i in range(len(Xopt))]
Smooth=CountRate-Xopt

plt.plot(Time,CountRate, label='L(t)=Raw Data')
plt.plot(Time, Xopt, label='G(t)=Gauss. Smoothed Lightcurve')
plt.plot(Time,Smooth, label='L(t)-G(t)')
plt.legend(fontsize='xx-small')
plt.xlabel('Relative Time (s)')
plt.ylabel('Count Rate (Counts/s)')

plt.savefig('problem1+2.png')
