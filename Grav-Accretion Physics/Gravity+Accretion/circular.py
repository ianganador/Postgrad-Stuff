import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

t1, x1,y1,z1, vx1,vy1,vz1=np.loadtxt("keplereuler.dat", unpack=True)
t, x,y,z,vx,vy,vz=np.loadtxt("keplerrk2.dat", unpack=True)
t1=t1/6.34
t=t/6.34


r=np.sqrt(x**2+y**2+z**2)
U=-1/r
v=np.sqrt(vx*vx+vy*vy+vz*vz)
K=.5*v
Q=U+K
Q=Q/Q[0]-1

r1=np.sqrt(x1**2+y1**2+z1**2)
U1=1/r1
v1=np.sqrt(vx1*vx1+vy1*vy1+vz1*vz1)
K1=.5*v1
Q1=U1+K1
Q1=Q1/Q1[0]-1
plt.title(r"% Error with Timestep = $2^{-6}$ (Code Units)")
plt.plot(t,Q, label='Euler')
plt.plot(t1,Q1, label='RK2')
plt.ylabel('% Error from Energy Conservation')
plt.xlabel(r'Time (in $t_{orbit}$)') 
plt.legend()
#plt.ylim(.99,1.0001)

#ax.plot(x2,y2,z2)
plt.show()
