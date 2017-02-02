import numpy as np
import time
import matplotlib.pyplot as plt
import pair_counting_function as pcf
from joblib import Parallel, delayed
import multiprocessing
start_time=time.time()
begin=time.time()
#~ M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)
#~ pi=np.pi
#~ dr=0.1
#~ print "start:",time.time()-begin
#~ hist,edge= pcf.counter_version3(X,Y,Z,dr)	
#~ print time.time()-begin
#~ np.savetxt('hist_0_1_Feb1.txt',np.transpose([hist,edge[:-1]]),fmt=['%.6f','%.6f'], header='Histogram\tedge') 
#~ 
#~ DD=hist
#~ DD/=(X.size*(X.size-1)/2)
#~ r=edge[:-1]
#~ RR = (4*pi*r**2*dr)/300**3 				# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
#~ Xi=DD/RR-1
#~ np.savetxt('Xi.txt',np.transpose([Xi]),fmt=['%.6f'])

########################################################################
####   Mock Galaxy Subsets      ########################################

M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-20.txt',unpack=True, skiprows=1)
pi=np.pi
dr=0.1
print "start:",time.time()-begin
hist,edge= pcf.counter_version3(X,Y,Z,dr)	
print time.time()-begin
np.savetxt('hist_mockgalaxySubset_M_less_than_-20.txt',np.transpose([hist,edge[:-1]]),fmt=['%.6f','%.6f'], header='Histogram\tedge') 
DD=hist
DD/=(X.size*(X.size-1)/2)
r=edge[:-1]
RR = (4*pi*r**2*dr)/300**3 				# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
Xi=DD/RR-1
np.savetxt('Xi_mockgalaxySubset_M_less_than_-20.txt',np.transpose([Xi]),fmt=['%.6f'])

print "ONE"




M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-21.txt',unpack=True, skiprows=1)
pi=np.pi
dr=0.1
print "start:",time.time()-begin
hist,edge= pcf.counter_version3(X,Y,Z,dr)	
print time.time()-begin
np.savetxt('hist_mockgalaxySubset_M_less_than_-21.txt',np.transpose([hist,edge[:-1]]),fmt=['%.6f','%.6f'], header='Histogram\tedge') 
DD=hist
DD/=(X.size*(X.size-1)/2)
r=edge[:-1]
RR = (4*pi*r**2*dr)/300**3 				# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
Xi=DD/RR-1
np.savetxt('Xi_mockgalaxySubset_M_less_than_-21.txt',np.transpose([Xi]),fmt=['%.6f'])

print "TWO"


M,L,X,Y,Z = np.loadtxt ('mockgalaxySubset_M_less_than_-22.txt',unpack=True, skiprows=1)
pi=np.pi
dr=0.1
print "start:",time.time()-begin
hist,edge= pcf.counter_version3(X,Y,Z,dr)	
print time.time()-begin
np.savetxt('hist_mockgalaxySubset_M_less_than_-22.txt',np.transpose([hist,edge[:-1]]),fmt=['%.6f','%.6f'], header='Histogram\tedge') 
DD=hist
DD/=(X.size*(X.size-1)/2)
r=edge[:-1]
RR = (4*pi*r**2*dr)/300**3 				# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
Xi=DD/RR-1
np.savetxt('Xi_mockgalaxySubset_M_less_than_-22.txt',np.transpose([Xi]),fmt=['%.6f'])

print "THREE"
