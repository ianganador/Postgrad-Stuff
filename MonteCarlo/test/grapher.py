import numpy as np
import matplotlib.pyplot as plt

#read in sampled values
x=np.loadtxt('test.dat', unpack=True)

x1=np.arange(0,20,.1) # xrange for analytic form
y = (15*x1**3)/(((3.14157)**4)*(np.exp(x1) - 1)) #generate analytic blackbody function

weights=np.ones_like(x)/float(len(x)) #weights to normalize sampled function
plt.plot(x1,y, label='Analytic')
plt.hist(x, weights=weights, bins=20, label='MC Sampled')
plt.legend()
plt.xlabel(r'X ($h \nu/kT)$')
plt.ylabel('Normalized Intensity')
plt.title('Test Problem 2 (Comparing Sampled and Analytic Planck')
plt.savefig('blackbody.png')



