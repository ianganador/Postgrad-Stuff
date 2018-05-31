import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read in data
spec, MJD,Time,DwellT,Background,CountRate,ErrorBar= np.loadtxt("qpo.dat", unpack=True)
#set gaussian threshold
tau=12
length=len(Time)
#print 242/np.mean(CountRate[0:216]), 242/np.mean(CountRate[300:419]), 24/np.mean(CountRate[0:216]), 24/np.mean(CountRate[300:419])
ErrorBar=ErrorBar*np.sqrt(3966/(length-3))
#define gaussian memory function for each time
def gauss(tk,ti,sigma):
	return np.exp(-.5*((tk-ti)/tau)**2.)/sigma**2.

length=len(Time)
#weight array for each data point's weight at different time values
w=np.zeros((length,length))
for i in range(length):
	for k in range(length):
		w[i][k]=gauss(Time[k],Time[i], ErrorBar[k])
#optimal averaging
Xopt=np.zeros(length)
Xopt=[np.sum(CountRate*w[i])/np.sum(w[i]) for i in range(len(Xopt))]
Smooth=CountRate-Xopt
maxm=.08955
n=10000
f=0
step=maxm/n
#curve fitting 
popt1=np.zeros(n)
popt2=np.zeros(n)
popt3=np.zeros(n)

value=8
for p in range(0,50):
	k=8*p
	freq=np.zeros(n)
	chi=np.zeros(n)
	y=np.zeros(length)
	for i in range(0,n):
		f=f+step
		def trigfunc(t,B,C,S):
			term=2*np.pi*f*t
			return B+C*np.cos(term)+S*np.sin(term)
	
		popt,pcov=curve_fit(trigfunc, Time[k: k+value], Smooth[k: k+value], sigma=ErrorBar[k: k+value])

	
		#popt1[i]=popt[0]
		#popt2[i]=popt[1]
		#popt3[i]=popt[2]
		#print popt
		y=popt[0]+popt[1]*np.cos(2*np.pi*f*Time)+popt[2]*np.sin(2*np.pi*f*Time)
		#print np.sqrt(np.diag(pcov))
		#print popt
		#print np.sum(((Smooth-y)/ErrorBar)**2), f
		
		chi[i]=np.sum(((Smooth-y)/ErrorBar)**2)
		#print chi[i]
		freq[i]=f
		plt.plot(Time[k: k+value], y[k: k+value])
		plt.scatter(Time[k: k+value], Smooth[k: k+value])
		plt.show()
	print chi[np.argmin(chi)], freq[np.argmin(chi)]/p
#plt.plot(freq, chi)
#plt.plot(Time,y)
#plt.scatter(Time,Smooth, s=.5, c='r')


#plt.xlabel('Frequency(Hz)')
#plt.ylabel(r'$\chi^2$')

#intmin=list(chi).index(min(chi))
#print freq[intmin], intmin

plt.show()
#plt.savefig('zoomedchi.png')
