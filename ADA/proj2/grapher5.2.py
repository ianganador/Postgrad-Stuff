import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
k=500.
gamma=100.
sigmas=np.zeros(13)
sigma=np.random.normal(sigmas, 10.)

phase=np.zeros(13)
phase=[-.1405,-.0583,.0325,.0998,.1740,.2310,.3079,.3699,.4388,.5008,.5698, .6371,.7276]
x=[2.*np.pi*y for y in phase]
velocity=gamma+k*np.sin(x)+sigma
sigma=[10]*13
sigmas=np.random.normal(sigmas,10.)
sigmas=[ 15.99673741, -14.37806515,   2.19733885,  19.9647144,    0.95873288,
  16.51627162,  16.59582365,  10.14396908,   0.039826,    15.31592272,
   0.77429533,   3.96046771,  -5.12545611]
velocity=[-268.24758615,  -79.87050779,  197.20789717 , 395.74821504,  563.24825736,
  598.39146844,  568.58674301,  463.28365205 , 270.86283662,  100.83942189,
 -114.19287216, -285.30208835, -391.54605108]
velocity=[sigmas[i]+velocity[i] for i in xrange(len(velocity))]



#y=np.zeros(length)

def trigfunc(phase,GAM,Ky,Kx):
	term=2*np.pi*phase
	return GAM+Ky*np.cos(term)+Kx*np.sin(term)

popt,pcov=curve_fit(trigfunc, phase, velocity, sigma=sigma)
y=popt[0]+popt[1]*np.cos(x)+popt[2]*np.sin(x)
print popt
print np.sqrt(np.diag(pcov))
print velocity
print sigma
print sigmas


plt.plot(phase,y, linewidth=.5)
plt.scatter(phase, velocity, s=2.)
plt.errorbar(phase, velocity, sigma, fmt='none', c='r')
plt.xlabel('Phase')
plt.ylabel(r'Radial Velocity (km s$^{-1}$)')
plt.title('Radial Velocity v. Phase')
#plt.show()
plt.savefig('step7.png')

