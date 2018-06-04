import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x,y= np.loadtxt("scattau.dat", unpack=True)

t=np.linspace(0,25,100)
z=t+t**2/2

plt.plot(t,z, label=r'$y=x + x^2/2$')
plt.plot(x,y, label='Monte Carlo Model')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$<N_{ave}>$')
plt.legend()
plt.show()
#plt.savefig('scattau.png')

