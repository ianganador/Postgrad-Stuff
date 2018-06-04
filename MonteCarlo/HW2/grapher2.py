import numpy as np
import matplotlib.pyplot as plt


#gen, neut=np.loadtxt('cri1.dat', unpack=True)
gen1,neut1, keff1=np.loadtxt('cri49d.dat', unpack=True)
gen2,neut2, keff2=np.loadtxt('cri49c.dat', unpack=True)
#gen3,neut3, keff3=np.loadtxt('cri51c.dat', unpack=True)
gen4,neut4, keff4=np.loadtxt('cri51.3c.dat', unpack=True)
gen5,neut5, keff5=np.loadtxt('cri51.3d.dat', unpack=True)
#gen6,neut6, keff6=np.loadtxt('cri51.4c.dat', unpack=True)
gen7,neut7, keff7=np.loadtxt('cri53c.dat', unpack=True)
gen8,neut8, keff8=np.loadtxt('cri53d.dat', unpack=True)

print np.mean(keff1), np.mean(keff5), np.mean(keff8)
plt.plot(gen1, keff1)
plt.xlabel('Generation Number')
plt.ylabel(r'$K_{eff}$')

plt.plot(gen2, keff2)
#plt.plot(gen3, keff3)
plt.plot(gen4, keff4)
plt.plot(gen5, keff5)
#plt.plot(gen6, keff6)
plt.plot(gen7, keff7)
plt.plot(gen8, keff8)
plt.title(r'$K_{eff}$ v. Neutron Generation (Comparison)')
plt.text(gen8[1]+1,keff8[1], 'Central Emission')
plt.text(gen2[1], keff2[1]-.02, 'Uniform Distribution')
plt.text(gen8[-1],keff8[-1]+.002, '53kg', fontsize='x-small')
plt.text(gen5[-1],keff5[-1], '51.3kg', fontsize='x-small')
plt.text(gen1[-1],keff1[-1]-.002, '49kg', fontsize='x-small')
plt.xlim(0,107)
plt.savefig('prob2.png')
