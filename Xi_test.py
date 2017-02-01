####ChaNge function file
####Change number N

import numpy as np
import time
import matplotlib.pyplot as plt
import pair_counting_function as pcf
from random import randint

from matplotlib import rc
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )

start_time=time.time()
begin=time.time()
N=30000
X=np.random.randint(300,size=N)
Y=np.random.randint(300,size=N)
Z=np.random.randint(300,size=N)

pi = np.pi

print X.size
print "start",time.time()-begin
dr=0.1
#~ hist,edge=pcf.counter_version3(X,Y,Z,dr)
bins = int((75-0.2)/dr)
hist=np.zeros(bins)


for n in range (X.size):
	hist_temp,edge = pcf.counter_version4(dr,X,Y,Z,n)
	hist+= hist_temp
DD=hist/(X.size*(X.size-1)/2)
RR = (4*pi*(edge[:-1])**2*dr)/300**3
#~ print DD/RR-1
print "time taken", time.time()-begin
plt.plot(DD/RR-1)
plt.show()

