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
files3.sort()
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
#for k in range(len(content)):
#	plt.plot(waves, content3[k][1]/np.trapz(content3[k][1], waves)+k/2000.)
#	plt.plot(waves, content[k]/np.trapz(content[k], waves)+k/2000., c='w')

#normalized everage GS2000 spectrum
GS2000=[content3[i][1]/np.trapz(content3[i][1],content3[i][0]) for i in range(len(content))]

#normalized best spectrum
m0=(content2[9][1]/np.trapz(content2[9][1],waves))

#normalized smoothed GS2000 spectrum
smooth=smoothmean/np.trapz(smoothmean, waves)

subGS=[(GS2000[i]-smooth) for i in range(len(GS2000))]
subTEMPLATE=m0-smooth
chisquares=np.zeros(100)
rv=np.zeros(len(subGS))
'''
for i in range(len(waves)):
	print waves[i], i
plt.plot(waves[100:1000],subGS[0][100:1000], label='GS2000')
plt.plot(waves[100:1000], subTEMPLATE[150:1050]-.00015, label='Shifted Template')
plt.plot(waves[100:1000], subTEMPLATE[100:1000], label='Normal Template')
plt.legend()
plt.show() 
'''
for k in range(len(subGS)):
	for x in range (-50,50):
		chisq=(subGS[k][100:1900]-(subTEMPLATE[100-x:1900-x]))**2/subTEMPLATE[100-x:1900-x]
		chisquares[x]=np.sum(chisq)
	rv[k]=(np.argmin(chisquares)*.577/6000)*3e5
	print rv[k]
phases=[-.1405,-.0583,.0325,.0998,.1740,.2310,.3079,.3699,.4388,.5008,.5698, .6371,.7276]
plt.plot(phases, rv)
#plt.plot(chisquares)
plt.show()



