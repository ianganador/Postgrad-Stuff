import numpy as np
import matplotlib.pyplot as plt


error,step=np.loadtxt("erroreuler.dat",unpack=True)
e,h=np.loadtxt("errorrk2.dat", unpack=True)


y2=1/step**1
plt.loglog(1/step,error, label="Euler")
plt.loglog(1/h, e, label='RK2')

plt.loglog(1/step, y2, label='t^1')
plt.title('Error v. Integration Step Size (Over One Orbit)')
plt.axhline(y=.1, xmin=.05, xmax=.95,ls='--', c='k', label=r'RMSE=0.10')
plt.ylabel(r'RMS Error')
plt.xlabel(r'H (step size)')

plt.legend()
plt.show()
