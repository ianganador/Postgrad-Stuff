import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import re
import sys
#from natsort import natsorted, ns


input_direct = raw_input

def get_dir(prompt):
    while True:
	direct_name = input_direct(prompt)
	direct_name = os.path.join(os.getcwd(), direct_name)
	if os.path.isdir(direct_name):
	    return direct_name
	else:
	    print("does not exist")


def files_in_dir(dir_name, file_spec="*.dat"):
    return glob.glob(os.path.join(dir_name, file_spec))

def file_iter(files):
    for fname in files:
	with open(fname) as inf:
	    yield fname, inf.read()
  


#dire   = get_dir("Please enter email directory: ")
#files = files_in_dir(dire, "*.dat")
files = files_in_dir('xoptimal', "*.dat")
files2= files_in_dir('templates', "*.dat")
files3= files_in_dir('spectra', "*.dat")
files.sort()
files3.sort(reverse=True)
files2.sort()
print files
print np.shape(files2)
print files3
content = [np.loadtxt(x, unpack=True) for x in files]
content2 = [np.loadtxt(x, unpack=True) for x in files2]
content3 = [np.loadtxt(x, unpack=True) for x in files3]


waves=content3[0][0]
smoothmean=np.mean(content, axis=0)
meanspec=np.mean(content3, axis=0)[1]
#this plots all normalized spectra with their smoothed counterparts
for k in range(len(content)):
	#plt.plot(waves, content3[k][1]/np.trapz(content3[k][1], waves)+k/2000.)
	plt.plot(waves, content[k]/np.trapz(content[k], waves)+k/2000.)
	plt.text(waves[-1], content[k][-1]/np.trapz(content[-1], waves)+k/2000., files3[k][-6:-4])
#this plots average spectrum/average smooth
#plt.plot(waves, (meanspec/np.trapz(meanspec,waves))/(smoothmean/np.trapz(smoothmean, waves)))
#plots best spectral type/average smooth

#plt.plot(waves, (content2[8][1]/np.trapz(content2[8][1],waves))/(smoothmean/np.trapz(smoothmean, waves)), linewidth=.5)

plt.title('Smoothed GS2000 Spectra')
plt.xlabel(r'Wavelength ($\AA$)')
plt.savefig('step4.smoothedGS.png')










