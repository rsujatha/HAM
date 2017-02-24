import pair_counting_function_keep as pcfk
import pair_counting_function as pcf
import numpy as np
import time
import matplotlib.pyplot as plt
begin=time.time()
X,Y,Z,M = np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)

T1=[]
T2=[]
T3=[]
T4=[]


NofPoints=np.linspace(int(np.log10(1)),int(np.log10(100000)),10000)
#~ NofPoints=range(1,100000,10000)

for i in NofPoints:
	#~ print i
	i = int(10**i)
	##semi bruteforce
	t=time.time()
	bins = np.exp(np.linspace(np.log(0.2),np.log(75),20))
	hist=np.zeros(bins.size-1)
	for n in range (X[:i].size):			#Put X.size later
		hist_temp,edge = pcf.counter(X[:i],Y[:i],Z[:i],n,False,bins) 			 
		hist+= hist_temp
	t=time.time()-t
	T3.append(t)
	
	##brute force
	t=time.time()
	hist=pcfk.counter_bruteforce(X[:i],Y[:i],Z[:i],0.1)
	t=time.time()-t
	T1.append(t)
	
	#~ ##kdtree
	t=time.time()
	hist,edge=pcf.counter_kdtree(X[:i],Y[:i],Z[:i],0.2,75,20)
	t=time.time()-t
	T2.append(t)
	
	
	
	##semibruteforce sphere
	t=time.time()
	hist,edge=pcfk.counter_spherical_select(X[:i],Y[:i],Z[:i],0.1)
	t=time.time()-t
	T4.append(t)
	
	
	
np.savetxt('Time4.txt',np.transpose([NofPoints,T1,T2,T3,T4]), header = 'No of Points \t bruteforce \t kdtree \t cubical \t spherical')	
#~ plt.plot(np.array(NofPoints,T1),label='bruteforce')
#~ plt.plot(np.array(NofPoints,T2),label='kdtree')
#~ plt.plot(np.array(NofPoints,T3),label='bruteforce_cubicbox')
#~ plt.plot(np.array(NofPoints,T4),label='bruteforce_spherical')
#~ plt.legend()
#~ plt.title('Time Complexity Analysis')
#~ plt.xlabel('No of Points')
#~ plt.ylabel('Time in secs')
#~ plt.savefig('TimeAnalysis.pdf')
#~ plt.show()

	
	
	
	
