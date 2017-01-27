import numpy as np
import pair_counting_function as pcf
import time


start_time = time.time()
init_time = time.time()
M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)

print 'Data loaded\nTime taken\t:',time.time()-start_time
start_time = time.time()

r_all 	= [0.2,5,6,75]
r 		= r_all[1]
dr 		= 0.1
DD 		= 0
skip	= 1000				# Number of iteration to skip before printing timing info
for n in range (X.size):			#Put X.size later
	DD += pcf.counter_version2(r,dr,X,Y,Z,n)
	if n%skip==0:
		print "Running loops {} iterations done,\nTime for prev {} run is\t:".format(n,skip),time.time()-start_time
		start_time = time.time()

print "Completed\nTime for entire operation is\t:",time.time()-init_time
print DD

