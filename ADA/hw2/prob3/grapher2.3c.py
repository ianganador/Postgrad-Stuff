#analyzing mass data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

#read in values
Mx, Mc= np.loadtxt("test.dat", unpack=True)

meanMx=np.mean(Mx)
varMx=np.var(Mx)
meanMc=np.mean(Mc)
varMc=np.var(Mc)
#distance from each point to mean in data space
Mxdist=[(x-meanMx)**2/varMx for x in Mx]
Mcdist=[(y-meanMc)**2/varMc for y in Mc]

dist=[(Mxdist[i]**2+Mcdist[i]**2)**.5 for i in range(len(Mxdist))]
sortd=sorted(dist)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='auto')

e1 = patches.Ellipse([meanMx, meanMc], width=2*varMx**.5, height=2*varMc**.5, angle=2, linewidth=1, fill=False)
e2 =patches.Ellipse([meanMx, meanMc], width=4*varMx**.5, height=4*varMc**.5, angle=2, linewidth=1, fill=False)

ax.add_patch(e1)
ax.add_patch(e2)
ax.autoscale()
plt.scatter(Mx,Mc, s=.01)

Mxs=sorted(Mx)
Mcs=sorted(Mc)

#find 1-sig confidence interval from sorted Mx, Mc data (34% on either 
#side of median, not robust
lowMx=Mxs[int(.16*len(Mxs))]
highMx=Mxs[int(.84*len(Mxs))]
lowMc=Mcs[int(.16*len(Mcs))]
highMc=Mcs[int(.84*len(Mcs))]

plt.axvline(x=lowMx, c='r', label=r'$1-\sigma$ Conf. Int.')
plt.axvline(x=highMx, c='r')
plt.axhline(y=lowMc, c='r')
plt.axhline(y=highMc, c='r')
plt.xlabel('Mx')
plt.ylabel('Mc')
plt.legend()

covmatrix=np.cov(Mx,Mc)
print covmatrix[0][1]/(varMx**.5*varMc**.5)
print varMx**.5, varMc**.5

plt.savefig('chicontoursblackhole.png')

