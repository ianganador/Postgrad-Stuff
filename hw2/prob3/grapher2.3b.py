import numpy as np
import matplotlib.pyplot as plt

#read in file values
Mx, Mc= np.loadtxt("test.dat", unpack=True)

meanMx=np.mean(Mx)
sigmaMx=np.var(Mx)**.5
meanMc=np.mean(Mc)
sigmaMc=np.var(Mc)**.5

Mxs=sorted(Mx)
Mcs=sorted(Mc)

lowMx=Mxs[int(.16*len(Mxs))]
highMx=Mxs[int(.84*len(Mxs))]
lowMc=Mcs[int(.16*len(Mcs))]
highMc=Mcs[int(.84*len(Mcs))]

plt.scatter(Mx,Mc, s=.1, color='k')

plt.axvline(x=meanMx+sigmaMx, color='r', label=r'$\mu \pm 1\sigma$')
plt.axvline(x=meanMx-sigmaMx, color='r')
plt.axhline(y=meanMc+sigmaMc, color='r')
plt.axhline(y=meanMc-sigmaMc, color='r')

plt.axvline(x=lowMx, label=r'$1-\sigma$ Conf. Int.')
plt.axvline(x=highMx)
plt.axhline(y=lowMc)
plt.axhline(y=highMc)

plt.xlabel('Mx')
plt.ylabel('Mc')
plt.legend(fontsize='x-small')


plt.savefig('confidencecompare.png')



