import numpy as np
import pair_counting_function as pcf
import time
from joblib import Parallel, delayed
import multiprocessing as mpg


#~ parallelise = True
parallelise = False

pi = np.pi

start_time = time.time()
init_time = time.time()
M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)

print 'Data loaded\nTime taken\t:',time.time()-start_time
start_time = time.time()

r_all 	= [0.2,5,6,75]
r 		= r_all[2]
dr 		= 0.1
DD 		= 0
skip	= 1000				# Number of iteration to skip before printing timing info

bins = int((75-0.2)/dr)
hist=np.zeros(bins)

if not(parallelise):
	print '---------------Not parallelising-------------------'
	for n in range (X.size):			#Put X.size later
		#~ DD += pcf.counter_version2(r,dr,X,Y,Z,n)
		hist_temp,edge = pcf.counter_version4(dr,X,Y,Z,n)
		hist+= hist_temp
		if n%skip==0:
			print "Running loops {} iterations done,\nTime for prev {} run is\t:".format(n,skip),time.time()-start_time
			start_time = time.time()
else:
	print '---------------Parallelising the run-------------------'		
	num_cores = mpg.cpu_count()
	res = Parallel(n_jobs=num_cores)(delayed(pcf.counter_version2)(r,dr,X,Y,Z,n) for n in range (X.size))
	#~ print res 
	DD = np.sum(res)
#~ print DD
DD/=X.size
print "Completed\nTime for entire operation is\t:",time.time()-init_time
print 'DD\t:',DD

RR = 4*pi*r**2*dr 				# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
print 'RR\t:',RR

print r'\xi for r = {}'.format(r),'\t:',DD/RR-1
