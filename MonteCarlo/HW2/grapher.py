import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
gen11,neut11=np.loadtxt('cri49b.dat', unpack=True)
gen,neut=np.loadtxt('cri50b.dat', unpack=True)
gen5,neut5=np.loadtxt('cri51b.dat', unpack=True)
gen2,neut2=np.loadtxt('cri51.2b.dat', unpack=True)
gen3,neut3=np.loadtxt('cri51.3b.dat', unpack=True)
gen4,neut4=np.loadtxt('cri51.4b.dat', unpack=True)
gen55,neut55=np.loadtxt('cri52b.dat', unpack=True)
gen6,neut6=np.loadtxt('cri53b.dat', unpack=True)


neut11=neut11/9200
neut=neut/9200
neut2=neut2/9200
neut3=neut3/9200
neut4=neut4/9200
neut5=neut5/9200
neut55=neut55/9200
neut6=neut6/9200

color=iter(cm.rainbow(np.linspace(0,1,5)))
plt.plot(gen11,neut11,  c=next(color))
plt.plot(gen,neut,  c=next(color))
plt.plot(gen2,neut2,c='k')
plt.plot(gen3,neut3,c=next(color))
plt.plot(gen4,neut4,c='k')
plt.plot(gen5,neut5,c='k')
plt.plot(gen55,neut55,c=next(color))
plt.plot(gen6,neut6,c=next(color))

plt.text(gen11[-1],neut11[-1], '49kg', fontsize='xx-small')
plt.text(gen[-1],neut[-1], '50kg', fontsize='xx-small')
plt.text(gen5[-1],neut5[-1]-.03, '51.3kg', fontsize='xx-small')
plt.text(gen2[-1],neut2[-1]-.0, '51.2kg', fontsize='xx-small')
plt.text(gen3[-1],neut3[-1], '51kg', fontsize='xx-small')
plt.text(gen4[-1],neut4[-1], '51.4kg', fontsize='xx-small')
plt.text(gen55[-1],neut55[-1], '52kg', fontsize='xx-small')
plt.text(gen6[-1],neut6[-1], '53kg', fontsize='xx-small')
plt.xlim(0,107)

plt.xlabel('Generation Number')
plt.ylabel('Neutron Pop. Relative to Starting Pop.')
plt.title('Neutron Population v. Generation (Uniform Distribution)')
plt.savefig('prob1b.png')
