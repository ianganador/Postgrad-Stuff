#plotting contours and calculating coefficients/chi fit
import numpy as np
import matplotlib.pyplot as plt

#initial data arrays
F=np.array([110.,160.,90.])
Lamb=np.array([80.,105.,120.])
sig=np.array([10.,20.,10.])
var=sig**2
invvar=1/var

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
A_mean=(np.sum(invvar)*np.sum(Glamb*F*invvar)-np.sum(Glamb*invvar)*np.sum(F*invvar))/det
sigC=1/np.sum(invvar)**.5
sigA=1/(np.sum(Glamb**2/var)**.5)

Chisq1=2.3
Chisq2=6.17
Chisq3=11.8
C11=np.array([])
C21=np.array([])
C12=np.array([])
C22=np.array([])
C13=np.array([])
C23=np.array([])
C14=np.array([])
C24=np.array([])
A=np.arange(-1000,4000,1)
#itrate over different chisq values (corresponding to 1-3 sigma, and
#a range of A values to find roots of C

for i in range(len(A)):
	a1=np.sum(invvar)
	b=np.sum(invvar*(-2*F+2*A[i]*Glamb))
	c1=np.sum(invvar*(F**2-2*F*Glamb*A[i]+A[i]**2*Glamb**2))-Chisq1
	C11=np.append(C11, (-b+(b**2-4*a1*c1)**.5)/2/a1)
	C21=np.append(C21, (-b-(b**2-4*a1*c1)**.5)/2/a1)
	
	c2=np.sum(invvar*(F**2-2*F*Glamb*A[i]+A[i]**2*Glamb**2))-Chisq2
	C12=np.append(C12, (-b+(b**2-4*a1*c2)**.5)/2/a1)
	C22=np.append(C22, (-b-(b**2-4*a1*c2)**.5)/2/a1)
	
	c3=np.sum(invvar*(F**2-2*F*Glamb*A[i]+A[i]**2*Glamb**2))-Chisq3
	C13=np.append(C13, (-b+(b**2-4*a1*c3)**.5)/2/a1)
	C23=np.append(C23, (-b-(b**2-4*a1*c3)**.5)/2/a1)	
	
	c4=np.sum(invvar*(F**2-2*F*Glamb*A[i]+A[i]**2*Glamb**2))-1.0
	C14=np.append(C14, (-b+(b**2-4*a1*c4)**.5)/2/a1)
	C24=np.append(C24, (-b-(b**2-4*a1*c4)**.5)/2/a1)

	


plt.plot(A, C11, c='r', label=r'2 param $1\sigma$ $\chi^2$')
plt.plot(A, C21, c='r')
plt.plot(A, C12, c='b', label=r'2 param $2\sigma$ $\chi^2$')
plt.plot(A, C22, c='b')
plt.plot(A, C13, c='g', label=r'2 param $3\sigma$ $\chi^2$')
plt.plot(A, C23, c='g')
plt.axvline(A_mean-sigA, c='k', label=r'1 param 1$\sigma$ ')
plt.axvline(A_mean+sigA, c='k')
plt.axhline(C-sigC, c='k')
plt.axhline(C+sigC, c='k')
plt.xlabel('A')
plt.ylabel('C')
plt.legend(fontsize='xx-small')

plt.scatter(A, C14)
plt.scatter(A, C24)
plt.savefig('chicontour.png')


