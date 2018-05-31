#Calculate Maximum Likelihood Estimators
import numpy as np
import matplotlib.pyplot as plt

#data arrays
F=np.array([110.,160.,90.])
Lamb=np.array([80.,105.,120.])
sig=np.array([10.,20.,10.])
var=sig**2
invvar=1/var

#gaussian as defined in the homework
def Gfunc(lamb):
	G=1/(np.sqrt(2*np.pi)*5)
	F=np.exp(-.5*((lamb-100)/5)**2)
	G=F*G
	return G
#calculate G(lambda) for given data (G is a function of lambda)
Glamb=np.array([])
for i in range(len(Lamb)):
	Glamb=np.append(Glamb,Gfunc(Lamb[i]))
#calculate det(Hessian) and max-likelihood A,C values
det=np.sum(invvar)*np.sum(Glamb**2*invvar)-np.sum(Glamb*invvar)**2

C=(np.sum(Glamb**2*invvar)*np.sum(F*invvar)-np.sum(Glamb*invvar)*np.sum(F*Glamb*invvar))/det
A=(np.sum(invvar)*np.sum(Glamb*F*invvar)-np.sum(Glamb*invvar)*np.sum(F*invvar))/det

sigC=1/np.sum(invvar)**.5
sigA=1/(np.sum(Glamb**2/var)**.5)
cov=-np.sum(Glamb*invvar)/(np.sum(invvar)*np.sum(Glamb**2*invvar)-np.sum((Glamb/sig)**2))

print cov/sigA/sigC

'''
x=np.linspace(50,150,100)
y1=np.array([])
y2=np.array([])
y3=np.array([])
y4=np.array([])
y5=np.array([])
#plot range of gaussians with maximum uncertainties on A,C
for i in range(len(x)):
	y1=np.append(y1, (C+A*Gfunc(x[i])))
	y2=np.append(y2, (C+sigC)+A*Gfunc(x[i]))	
	y3=np.append(y3, (C-sigC)+A*Gfunc(x[i]))	
	y4=np.append(y4, C+(A+sigA)*Gfunc(x[i]))
	y5=np.append(y5, C+(A-sigA)*Gfunc(x[i]))

plt.scatter(Lamb,F)
plt.plot(x,y1, label=r'$F(\lambda)$')
plt.plot(x,y2, label=r'$C+\sigma$')
plt.plot(x,y3, label=r'$C-\sigma$')
plt.plot(x,y4, label=r'$A+\sigma$')
plt.plot(x,y5, label=r'$A-\sigma$')
plt.errorbar(Lamb,F,sig, fmt='o', c='k')
plt.xlim(70,130)
plt.ylabel(r'$F(\lambda)$')
plt.xlabel(r'$\lambda$')
plt.legend()

plt.savefig('sigmacomparisons.png')'''

