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
	p = P[:,n]				## Coordinates of the point in consideration. The (small) cube is made around this point
	c = P[:,n+1:]			## Shortened array
	#~ print np.shape(considered_array)
	#~ print p
	x,y,z = 0,1,2
	if (p[x]<=r+dr or p[y]<=r+dr or p[z]<=r+dr) or (p[x]>=300-r-dr or p[y]>=300-r-dr or p[z]>=300-r-dr):
		## Edge effects take place 
		if p[x]<=r+dr:
			ind = np.where(c[x]>300-(r+dr))[0]
			c[x,ind]-=300
		elif p[x]>=300-r-dr:
			ind = np.where(c[x]<(r+dr))[0]
			c[x,ind]+=300
		if p[y]<=r+dr:
			ind = np.where(c[y]>300-(r+dr))[0]
			c[y,ind]-=300
		elif p[y]>=300-r-dr:
			ind = np.where(c[y]<(r+dr))[0]
			c[y,ind]+=300
		if p[z]<=r+dr:
			ind = np.where(c[z]>300-(r+dr))[0]
			c[z,ind]-=300
		elif p[z]>=300-r-dr: 
			ind = np.where(c[z]<(r+dr))[0]
			c[z,ind]+=300
		index = np.where((np.abs(c[x]-p[x])<r+dr) & 
						 (np.abs(c[y]-p[y])<r+dr) &
						 (np.abs(c[z]-p[z])<r+dr))[0]
		sel_arr = c[:,index]
		dist_array = np.linalg.norm(sel_arr-p[:,None],axis=0)
	else: 
		## The point is well inside the cube and thus will give correct results directly
		index = np.where((np.abs(c[x]-p[x])<r+dr) & 
						 (np.abs(c[y]-p[y])<r+dr) &
						 (np.abs(c[z]-p[z])<r+dr))[0]
		sel_arr = c[:,index]
		dist_array = np.linalg.norm(sel_arr-p[:,None],axis=0)
	DD = (np.where((dist_array<r+dr) & (dist_array>=r))[0]).size
	return DD

def counter_version3 (X,Y,Z,dr):
	
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
	T = time.time()	
	P = np.array([X,Y,Z])	# Creating a coordinate map of points
	num = X.size 			# Number of points
	bins = int((75-0.2)/dr)
	hist=np.zeros(bins)
	
	for x in range(1,230000):
		#~ P_prime = np.roll(P,-x,axis=1)
		#~ d = (P-P_prime)
		temp_1 = P[:,:-x]
		temp_2 = P[:,x:]
		d = (temp_1-temp_2)**2
		sum_d=np.sqrt(np.sum(d,axis=0))
		#sum_d = np.linalg.norm(d,axis=0)
		hist1,edge = np.histogram(sum_d,bins,range=(0.2,75))
		hist+=hist1
		#if x%1000==0:
		#	print "Iter No:",x,time.time()-T,"sec passed"
		#	T=time.time()
	return hist,edge

def counter_version4 (dr,X,Y,Z,n):
	
	'''
	
	This function takes the Original arrays from the text file and returns the histogram 
	of number of pairs for the element given by 'n'
	
	Input:
	---------------------
	dr					: Thickness of the shell in consideration 
	X					: X coordinates of all the points
	Y					: Y coordinates of all the points
	Z					: Z coordinates of all the points
	n					: Index number of the point to be computed for
	
	Output:
	---------------------
	hist				: Histogram of the distances between 'n' and other galaxies
	edge				: Edges of the Histogram 
	
	
	'''
	P = np.array([X,Y,Z])
	p = P[:,n]				## Coordinates of the point in consideration. The (small) cube is made around this point
	c = P[:,n+1:]			## Shortened array
	#~ print np.shape(considered_array)
	#~ print p
	x,y,z = 0,1,2
	start_time = time.time()
	del_x = np.abs(c[x]-p[x])
	del_y = np.abs(c[y]-p[y])
	del_z = np.abs(c[z]-p[z])
	del_x[np.where(del_x>225)[0]] -= 300
	del_y[np.where(del_y>225)[0]] -= 300
	del_z[np.where(del_z>225)[0]] -= 300
	
	index = np.where(((del_x<75)) & 
					((del_y<75)) & 
					((del_z<75)) ) [0]
	if n%1000==0: print 'time for finding the small cube for 1000 iter', (time.time()-start_time )*1000
	#sel_arr = c[:,index]
	start_time = time.time()
	#~ dist_array = np.linalg.norm(sel_arr-p[:,None],axis=0)
	dist_array = np.sqrt( del_x[index]**2+del_y[index]**2+del_z[index]**2)
	#dist_array = np.sqrt( del_x**2+del_y**2+del_z**2)
	if n%1000==0: print 'time for computing distance for 1000 iter', (time.time()-start_time )*1000
	bins = int((75-0.2)/dr)
	start_time = time.time()
	hist, edge =  np.histogram(dist_array,bins,range = (0.2,75))
	if n%1000==0: print 'time for making histogram for 1000 iter', (time.time()-start_time )*1000

	return hist,edge




#~ X = np.array([1,2,3,4,5])
#~ Y = np.array([6,7,8,9,0]) 
#~ Z = np.array([1,3,5,7,9])

#~ hist,edge = counter(X,Y,Z,0.1)
#~ 
#~ plt.plot(edge[:-1],hist)
#~ plt.show()

#~ print counter_version2(1,1,X,Y,Z,0)

