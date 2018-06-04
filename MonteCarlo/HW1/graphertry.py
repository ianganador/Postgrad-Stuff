import numpy as np
import matplotlib.pyplot as plt

#read in file values
x,y, weights= np.loadtxt("prob2_tau=50.dat", unpack=True)

#convert pixels to physical distances
x=[x[i]*.00714-(.714) for i in range(len(x))]

#constant for intensity calculation (.1*Lsun/(140pc^2)/(pi*theta^2)
#small angle, we can approximate solid angle as pi*theta^2,
#theta in rads is 100AU[m]/140pc[m]
#const=.1*3.83E26/(4.32E18)**2/(np.pi*.714**2)

#divide weights by number of photon packets
#weights=[(weights[i])*const/len(weights) for i in range(len(weights))]
plt.scatter(x,y, c=weights, s=.1)
#plot bins of intensity over x
#plt.hist(x, weights=weights)
plt.xlabel("Angular Position with Nebula Center at 0 (Arcseconds)") 
plt.show()
#plt.savefig("image.png")
