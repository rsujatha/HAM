import numpy as np
import pair_counting_function as pcf
from scipy import spatial
import time
import sys
import matplotlib.pyplot as plt
from matplotlib import rc
begin=time.time()

pi=np.pi
M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-20.txt',unpack=True, skiprows=1)
bin_num=20
pairsN=float(X.size*(X.size-1)/2.)
DD,bins=pcf.counter_kdtree(X,Y,Z,bin_num)
DD=DD/pairsN
rr=bins[1:]**3-bins[:-1]**3
RR = 4/3.*pi*(rr)/300.**3
Xi=DD/RR-1
print Xi.size
bins_array=(bins[1:]+bins[:-1])/2.
plt.plot(bins_array,Xi,'-o',label='M<-20')
plt.xscale('log')
plt.yscale('log')


M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-21.txt',unpack=True, skiprows=1)
bin_num=20
pairsN=float(X.size*(X.size-1)/2.)
DD,bins=pcf.counter_kdtree(X,Y,Z,bin_num)
DD=DD/pairsN
rr=bins[1:]**3-bins[:-1]**3
RR = 4/3.*pi*(rr)/300.**3
Xi=DD/RR-1
print Xi.size
bins_array=(bins[1:]+bins[:-1])/2.
plt.plot(bins_array,Xi,'-o',label='M<-21')
plt.xscale('log')
plt.yscale('log')


M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-22.txt',unpack=True, skiprows=1)
bin_num=20
pairsN=float(X.size*(X.size-1)/2.)
DD,bins=pcf.counter_kdtree(X,Y,Z,bin_num)
DD=DD/pairsN
rr=bins[1:]**3-bins[:-1]**3
RR = 4/3.*pi*(rr)/300.**3
Xi=DD/RR-1
print Xi.size
bins_array=(bins[1:]+bins[:-1])/2.
plt.plot(bins_array,Xi,'-o',label='M<-22')
plt.xscale('log')
plt.yscale('log')
plt.title('2_point Correlation')
plt.xlabel('Distance r')
plt.ylabel(r'$\xi$(r)')
plt.legend()
plt.savefig('kdtreeXi.pdf')
plt.show()




