import numpy as np
#import matplotlib.pyplot as plt
import time


def counter (X,Y,Z,dr):
	
	'''
	
	Takes the coordinates of the galaxies and computes distances between each pair 
	and generates an histogram which is then returned
	
	Input:
	-----------------
	X				: X coordinate of the galaxy
	Y				: Y coordinate of the galaxy
	Z				: Z coordinate of the galaxy
	dr				: Bin width of the histogram
	
	Output:
	-----------------
	hist			: Histogram of the distances between galaxies
	edge			: Edges of the histogram
	
	
	Note:
	1) The code doesn't correct for the edge effects
	2) The length of edges array is one more than histogram
	
	'''
	start_time = time.time()	
	P = np.array([X,Y,Z])	# Creating a coordinate map of points
	num = X.size 			# Number of points
	dist = np.zeros(num*(num-1)/2,dtype=int)
	print time.time()-start_time
	if num%2==0:
		for x in range (1,num/2+1):
			P_prime = np.roll(P,x,axis=1)
			d = (P-P_prime)
			sum_d = np.linalg.norm(d,axis=0)
			if x!=num/2:dist = np.concatenate((dist,sum_d),axis=1)
			else: dist = np.concatenate((dist,sum_d[:-(num/2)]))
			if x%100==0: print x,time.time()-start_time
	else:
		for x in range (1,(num+1)/2):
			P_prime = np.roll(P,x,axis=1)
			d = (P-P_prime)
			sum_d = np.linalg.norm(d,axis=0)
			
			#dist = np.concatenate((dist,sum_d),axis=1)
			if x==1:
				print np.shape(sum_d)
				dist[((x-1)*num):(x*num)] = sum_d
			else: 
				#dist = np.vstack([dist,sum_d])#,axis=1)
				dist[((x-1)*num):(x*num)] = sum_d
			if x%100==0: print x,time.time()-start_time

	#dist = np.sqrt(dist)
	bins = int(np.sqrt(3)*450/dr)
	hist,edge = np.histogram(dist,bins,range=(0,np.sqrt(3)*450))	
	return hist,edge

#~ X = np.array([1,2,3,4,5])
#~ Y = np.array([6,7,8,9,0]) 
#~ Z = np.array([1,3,5,7,9])
#~ hist,edge = counter(X,Y,Z,0.1)
#~ 
#~ plt.plot(edge[:-1],hist)
#~ plt.show()
