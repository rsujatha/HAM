import numpy as np
import time

def counter (dr,X,Y,Z,n,chatter):
	
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
	chatter				: Boolean variable to determine whether running info is to be printed 
	
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
	skip=1000
	index = np.where(((del_x<75)) & 
					((del_y<75)) & 
					((del_z<75)) ) [0]
	if n%skip==0 and chatter: print 'time for finding the small cube for {} iter'.format(skip), (time.time()-start_time )*skip
	#sel_arr = c[:,index]
	start_time = time.time()
	#~ dist_array = np.linalg.norm(sel_arr-p[:,None],axis=0)
	dist_array = np.sqrt( del_x[index]**2+del_y[index]**2+del_z[index]**2)
	#dist_array = np.sqrt( del_x**2+del_y**2+del_z**2)
	if n%skip==0 and chatter: print 'time for computing distance for {} iter'.format(skip), (time.time()-start_time )*skip
	bins = int((75-0.2)/dr)
	start_time = time.time()
	hist, edge =  np.histogram(dist_array,bins,range = (0.2,75))
	if n%skip==0 and chatter: print 'time for making histogram for {} iter'.format(skip), (time.time()-start_time )*skip

	return hist,edge

