import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import sys
import scipy.stats as stat


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
files = files_in_dir('spectra', "*.dat")
#files.sort(reverse=True)
content = [np.loadtxt(x, unpack=True) for x in files]
files2=files_in_dir('templates', "*.dat")
files2.sort(reverse=True)
content2=[np.loadtxt(x, unpack=True) for x in files2]
print len(content2[0][0]), len(content[0][0])
for k in range(len(content2)):

	chi=stat.chisquare(content2[k][1]/np.sum(content2[k][1]),np.mean(content, axis=0)[1]/np.sum(np.mean(content, axis=0)[1]))
	print chi, files2[k]





plt.plot(content[0][0], np.mean(content, axis=0)[1]/np.trapz(np.mean(content, axis=0)[1], content[0][0]), linewidth=.5)
plt.title('Average GS2000 Spectrum')
plt.xlabel(r'Wavelength($\AA$)')
plt.ylabel('Normalized Intensity')



plt.savefig('step3.png')



