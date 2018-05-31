import numpy as np
import matplotlib.pyplot as plt
import glob
import os

import sys


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
  

dire   = get_dir("enter directory: ")
#dire= 'templates'
files = files_in_dir(dire, "*.dat")
files.sort(reverse=True)
content = [np.loadtxt(x, unpack=True) for x in files]
for i in range(len(files)):
	label=files[i][43:-4]
	plt.plot(content[i][0], (content[i][1]/np.trapz(content[i][1], content[i][0])+float(i)/3000), linewidth=.5)
	plt.text(content[i][0][-1], (content[i][1][-10]/np.trapz(content[i][1], content[i][0])+float(i)/3000),label)
plt.xlabel(r'Wavelength($\AA$)')
plt.ylabel('Normalized Intensity + Const')
plt.title('Stellar Spectral Templates')
plt.savefig('step1.2.png')


