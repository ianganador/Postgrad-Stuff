import numpy as np
import matplotlib.pyplot as plt

Mx=np.loadtxt('MC_Mx.dat', unpack=True)
weights = np.ones_like(Mx)/float(len(Mx))
print np.mean(Mx), np.median(Mx)
print np.sqrt(np.var(Mx))
plt.hist(Mx, weights=weights, bins=50, cumulative=True)
plt.axvline(np.mean(Mx), c='k', label='Mean')
plt.axvline(np.median(Mx), c='r', label='Median')
plt.axvline(np.median(Mx)+np.sqrt(np.var(Mx)),ls='--' ,c='r', label=r'1-$\sigma$ interval')
plt.axvline(np.median(Mx)-np.sqrt(np.var(Mx)),ls='--' ,c='r')
plt.legend()
plt.ylabel('Relative Frequency')
plt.xlabel(r'$M_x$ ($M_{\odot}$)')
plt.savefig('step10.2.png')
