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


def counter_version2 (r,dr,X,Y,Z,n):
	
	'''
	
	This function takes the Original arrays from the text file and the 
	radius element we need to compute the pairs for, and returns the number of pairs within 
	r and r+dr
	
	Input:
	---------------------
	r					: Minimum radius of the shell in consideration
	dr					: Thickness of the shell in consideration 
	X					: X coordinates of all the points
	Y					: Y coordinates of all the points
	Z					: Z coordinates of all the points
	n					: Index number of the point to be computed for
	
	Output:
	---------------------
	DD					: Number of points within r and r+dr of point 'n'
	
	'''
	
	P = np.array([X,Y,Z])
	p = P[:,n]
	c = P[:,n+1:]			## Shortened array
	#~ print np.shape(considered_array)
	#~ print p
	x,y,z = 0,1,2
	if (p[0]<=r or p[1]<=r or p[2]<=r) or (p[0]>=300-r or p[1]>=300-r or p[2]>=300-r):
		## Edge effects take place 
	else:
		## The point is well inside the cube and thus will give correct results directly
		index = np.where((np.abs(c[x]-p[x])<r) & 
						 (np.abs(c[y]-p[y])<r) &
						 (np.abs(c[z]-p[z])<r))[0]
		sel_arr = c[:,index]
		dist_array = np.linalg.norm(sel_arr-p,axis=)
	DD=1
	
	return DD
X = np.array([1,2,3,4,5])
Y = np.array([6,7,8,9,0]) 
Z = np.array([1,3,5,7,9])

#~ counter_version2(1,0.1,X,Y,Z,2)