import numpy as np
import matplotlib.pyplot as plt

#read in file values
Mx, Mc= np.loadtxt("test.dat", unpack=True)

meanMx=np.mean(Mx)
sigmaMx=np.var(Mx)**.5
meanMc=np.mean(Mc)
sigmaMc=np.var(Mc)**.5
print meanMx,sigmaMx,meanMc,sigmaMc


plt.hist(Mx, label=r'$M_x$')
plt.hist(Mc, label=r'$M_c$')
plt.xlabel(r'Mass ($M_\odot$)')
plt.ylabel(r'Counts (out of $10^6$ trials)')
plt.legend()


plt.savefig('masshistogram.png')



