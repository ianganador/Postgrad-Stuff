import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot
import matplotlib.figure 

x1=np.loadtxt("scattau..1.dat")
x2=np.loadtxt("scattau.1.dat")
x3=np.loadtxt("scattau.5.dat")
x4=np.loadtxt("scattau.10.dat")
x5=np.loadtxt("scattau.20.dat")
x6=np.loadtxt("scattau.50.dat")
x7=np.loadtxt("scattau.100.dat")

plt.xscale("log")
plt.yscale("log")
weights1 = np.ones_like(x1)/float(len(x1))
weights2 = np.ones_like(x2)/float(len(x2))
weights3 = np.ones_like(x3)/float(len(x3))
weights4 = np.ones_like(x4)/float(len(x4))
weights5 = np.ones_like(x5)/float(len(x5))
weights6 = np.ones_like(x6)/float(len(x6))
weights7 = np.ones_like(x7)/float(len(x7))
binboounds3=np.linspace(0,200,30)
binboounds=np.linspace(0,150,50)
binboounds2=np.linspace(0,120,40)
binboounds1=np.linspace(0,30,10)

y1,binEdges1=np.histogram(x1, bins=binboounds1, weights=weights1)
y2,binEdges2=np.histogram(x2, bins=binboounds1, weights=weights2)
y3,binEdges3=np.histogram(x3, bins=binboounds1, weights=weights3)
y4,binEdges4=np.histogram(x4, bins=binboounds, weights=weights4)
y5,binEdges5=np.histogram(x5, bins=binboounds3, weights=weights5)
y6,binEdges6=np.histogram(x6, bins=binboounds3, weights=weights6)
y7,binEdges7=np.histogram(x7, bins=binboounds3, weights=weights7)


bincenters1=0.5*(binEdges1[1:]+binEdges1[:-1])
bincenters2=0.5*(binEdges2[1:]+binEdges2[:-1])
bincenters3=0.5*(binEdges3[1:]+binEdges3[:-1])
bincenters4=0.5*(binEdges4[1:]+binEdges4[:-1])
bincenters5=0.5*(binEdges5[1:]+binEdges5[:-1])
bincenters6=0.5*(binEdges6[1:]+binEdges6[:-1])
bincenters7=0.5*(binEdges7[1:]+binEdges7[:-1])

plt.plot(bincenters1,y1,'-', label=r'$\tau=.1$')
plt.plot(bincenters2,y2,'-', label=r'$\tau=1$')
plt.plot(bincenters3,y3,'-', label=r'$\tau=5$')
plt.plot(bincenters4,y4,'-', label=r'$\tau=10$')
plt.plot(bincenters5,y5,'-', label=r'$\tau=20$')
plt.plot(bincenters6,y6,'-', label=r'$\tau=50$')
plt.plot(bincenters7,y7,'-', label=r'$\tau=100$')



plt.xlabel(r"Time to Escape (days)")
plt.ylabel(r"Percentage of Photons")
plt.legend()
plt.xlim(1,150)
plt.ylim(.01,1)

plt.savefig('problem1.png')
#plt.savefig("test.5.png")
