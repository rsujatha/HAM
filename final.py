import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )

#~ M20,L20,X20,Y20,Z20 = np.loadtxt ('mockgalaxySubset_M<_-20.txt',unpack=True, skiprows=1)
#~ M21,L21,X21,Y21,Z21 = np.loadtxt ('mockgalaxySubset_M<_-21.txt',unpack=True, skiprows=1)
#~ M22,L22,X22,Y22,Z22 = np.loadtxt ('mockgalaxySubset_M<_-22.txt',unpack=True, skiprows=1)

Xi20=np.loadtxt('Xi_mockgalaxySubset_M_less_than_-20.txt',unpack=True)
Xi21=np.loadtxt('Xi_mockgalaxySubset_M_less_than_-21.txt',unpack=True)
Xi22=np.loadtxt('Xi_mockgalaxySubset_M_less_than_-22.txt',unpack=True)
hist20,edge20=np.loadtxt('hist_mockgalaxySubset_M_less_than_-20.txt',unpack=True)
hist21,edge21=np.loadtxt('hist_mockgalaxySubset_M_less_than_-21.txt',unpack=True)
hist22,edge22=np.loadtxt('hist_mockgalaxySubset_M_less_than_-22.txt',unpack=True)
plt.plot(edge20,Xi20,'.r',label='M$<-20$')
plt.plot(edge21,Xi21,'.b',label='M$<-21$')
plt.plot(edge22,Xi22,'.g',label='M$<-22$')
plt.xlabel('Distance(r)')
plt.legend()
plt.ylabel('Xi(r)')
plt.xscale('log')
plt.yscale('log')
plt.show()
