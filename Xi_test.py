####ChaNge function file
####Change number N

import numpy as np
import time
import matplotlib.pyplot as plt
import pair_counting_function as pcf
from random import randint
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
hist,edge=pcf.counter_version3(X,Y,Z,dr)
DD=hist/(X.size*(X.size-1)/2)
RR = (4*pi*edge[:-1]**2*dr)/300**3
print DD/RR-1
plt.plot(DD/RR-1)
plt.show()

