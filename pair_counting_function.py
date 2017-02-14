import numpy as np
from scipy import spatial
import time

def counter (X,Y,Z,n,chatter,bins=None):
	
	'''
	
	This function takes the Original arrays from the text file and returns the histogram 
	of number of pairs for the element given by 'n'
	
	Input:
	---------------------
	X					: X coordinates of all the points
	Y					: Y coordinates of all the points
	Z					: Z coordinates of all the points
	n					: Index number of the point to be computed for
	chatter				: Boolean variable to determine whether running info is to be printed 
	bins				: Sequence of bins edges to be used, or none if uniform binning is to be used
	
	Output:
	---------------------
	hist				: Histogram of the distances between 'n' and other galaxies
	edge				: Edges of the Histogram 
	
	
	'''
	if bins==None: bins= int((75-0.2)/dr)
	P = np.array([X,Y,Z])
	p = P[:,n]				## Coordinates of the point in consideration. The (small) cube is made around this point
	c = P[:,n+1:]			## Shortened array
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
	#~ if n%skip==0 and chatter: print 'time for finding the small cube for {} iter'.format(skip), (time.time()-start_time )*skip
	start_time = time.time()
	dist_array = np.sqrt( del_x[index]**2+del_y[index]**2+del_z[index]**2)
	#~ if n%skip==0 and chatter: print 'time for computing distance for {} iter'.format(skip), (time.time()-start_time )*skip
	#~ bins = int((75-0.2)/dr)
	start_time = time.time()
	hist, edge =  np.histogram(dist_array,bins,range = (0.2,75))
	#~ if n%skip==0 and chatter: print 'time for making histogram for {} iter'.format(skip), (time.time()-start_time )*skip

	return hist,edge


def counter_kdtree (X,Y,Z,bin_num):
	L=300
	Rmax=75

	## Box 1 - Right Face 			R
	sel_ind = np.where(X<=Rmax)[0]  
	X1=X[sel_ind]+300
	Y1=Y[sel_ind]
	Z1=Z[sel_ind]


	## Box 2 - Left Face 			L
	sel_ind = np.where(X>=L-Rmax)[0]  
	X2=X[sel_ind]-300
	Y2=Y[sel_ind]
	Z2=Z[sel_ind]

	## Box 3 - Top Face 			T
	sel_ind = np.where(Y<=Rmax)[0]  
	X3=X[sel_ind]
	Y3=Y[sel_ind]+300
	Z3=Z[sel_ind]

	## Box 4 - Bottom Face		 	B
	sel_ind = np.where(Y>=L-Rmax)[0]  
	X4=X[sel_ind]
	Y4=Y[sel_ind]-300
	Z4=Z[sel_ind]

	## Box 5 - Back Face 			K
	sel_ind = np.where(Z>=L-Rmax)[0]  
	X5=X[sel_ind]
	Y5=Y[sel_ind]
	Z5=Z[sel_ind]-300

	## Box 6 - Front Face 			F
	sel_ind = np.where(Z<=Rmax)[0]  
	X6=X[sel_ind]
	Y6=Y[sel_ind]
	Z6=Z[sel_ind]+300

	## Box 7 - Edge RT
	sel_ind = np.where((X<=Rmax) & (Y<=Rmax))[0]  
	X7=X[sel_ind]+300
	Y7=Y[sel_ind]+300
	Z7=Z[sel_ind]

	## Box 8 - Edge LT
	sel_ind = np.where((X>=L-Rmax)&(Y<=Rmax))[0]  
	X8=X[sel_ind]-300
	Y8=Y[sel_ind]+300
	Z8=Z[sel_ind]

	## Box 9 - Edge KT
	sel_ind = np.where((Z>=L-Rmax)&(Y<=Rmax))[0]  
	X9=X[sel_ind]
	Y9=Y[sel_ind]+300
	Z9=Z[sel_ind]-300

	## Box 10 -Edge FT
	sel_ind = np.where((Z<=Rmax)&(Y<=Rmax))[0]  
	X10=X[sel_ind]
	Y10=Y[sel_ind]+300
	Z10=Z[sel_ind]+300

	## Box 11 - Edge RB
	sel_ind = np.where((X<=Rmax) & (Y>=L-Rmax))[0]  
	X11=X[sel_ind]+300
	Y11=Y[sel_ind]-300
	Z11=Z[sel_ind]

	## Box 12 - Edge LB
	sel_ind = np.where((X>=L-Rmax)&(Y>=L-Rmax))[0]  
	X12=X[sel_ind]-300
	Y12=Y[sel_ind]-300
	Z12=Z[sel_ind]

	## Box 13 - Edge KB
	sel_ind = np.where((Z>=L-Rmax)&(Y>=L-Rmax))[0]  
	X13=X[sel_ind]
	Y13=Y[sel_ind]-300
	Z13=Z[sel_ind]-300

	## Box 14 - Edge FB
	sel_ind = np.where((Z<=Rmax)&(Y>=L-Rmax))[0]  
	X14=X[sel_ind]
	Y14=Y[sel_ind]-300
	Z14=Z[sel_ind]+300

	## Box 15 - Edge RF  
	sel_ind = np.where((X<=Rmax)&(Z<=Rmax))[0]  
	X15=X[sel_ind]+300
	Y15=Y[sel_ind]
	Z15=Z[sel_ind]+300

	## Box 16 - Edge LF
	sel_ind = np.where((X>=L-Rmax)&(Z<=Rmax))[0]  
	X16=X[sel_ind]-300
	Y16=Y[sel_ind]
	Z16=Z[sel_ind]+300

	## Box 17 - Edge RK
	sel_ind = np.where((X<=Rmax)&(Z>=L-Rmax))[0]  
	X17=X[sel_ind]+300
	Y17=Y[sel_ind]
	Z17=Z[sel_ind]-300

	## Box 18 - Edge LK
	sel_ind = np.where((X>=L-Rmax)&(Z>=L-Rmax))[0]  
	X18=X[sel_ind]-300
	Y18=Y[sel_ind]
	Z18=Z[sel_ind]-300

	## Box 19 - Corner RTK
	sel_ind = np.where((X<=Rmax)&(Y<=Rmax)&(Z>=L-Rmax))[0]  
	X19=X[sel_ind]+300
	Y19=Y[sel_ind]+300
	Z19=Z[sel_ind]-300 

	## Box 20 - Corner RBK
	sel_ind = np.where((X<=Rmax)&(Y>=L-Rmax)&(Z>=L-Rmax))[0]  
	X20=X[sel_ind]+300
	Y20=Y[sel_ind]-300
	Z20=Z[sel_ind]-300

	## Box 21 - Corner RTF
	sel_ind = np.where((X<=Rmax)&(Y<=Rmax)&(Z<=Rmax))[0]  
	X21=X[sel_ind]+300
	Y21=Y[sel_ind]+300
	Z21=Z[sel_ind]+300

	## Box 22 - Corner RBF
	sel_ind = np.where((X<=Rmax)&(Y>=L-Rmax)&(Z<=Rmax))[0]  
	X22=X[sel_ind]+300
	Y22=Y[sel_ind]-300
	Z22=Z[sel_ind]+300

	## Box 23 - Corner LTK
	sel_ind = np.where((X>=L-Rmax)&(Y<=Rmax)&(Z>=L-Rmax))[0]  
	X23=X[sel_ind]-300
	Y23=Y[sel_ind]+300
	Z23=Z[sel_ind]-300 

	## Box 24 - Corner LBK
	sel_ind = np.where((X>=L-Rmax)&(Y>=L-Rmax)&(Z>=L-Rmax))[0]  
	X24=X[sel_ind]-300
	Y24=Y[sel_ind]-300
	Z24=Z[sel_ind]-300

	## Box 25 - Corner LTF
	sel_ind = np.where((X>=L-Rmax)&(Y<=Rmax)&(Z<=Rmax))[0]  
	X25=X[sel_ind]-300
	Y25=Y[sel_ind]+300
	Z25=Z[sel_ind]+300

	## Box 26 - Corner LBF
	sel_ind = np.where((X>=L-Rmax)&(Y>=L-Rmax)&(Z<=Rmax))[0]  
	X26=X[sel_ind]-300
	Y26=Y[sel_ind]-300
	Z26=Z[sel_ind]+300


	X_shell = np.concatenate((X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26))
	Y_shell = np.concatenate((Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21,Y22,Y23,Y24,Y25,Y26))
	Z_shell = np.concatenate((Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13,Z14,Z15,Z16,Z17,Z18,Z19,Z20,Z21,Z22,Z23,Z24,Z25,Z26))
#~ print X_shell.size, Y_shell.size,Z_shell.size


	X_all = np.concatenate((X,X_shell))
	Y_all = np.concatenate((Y,Y_shell))
	Z_all = np.concatenate((Z,Z_shell))

	#~ bin_num=20
	bins = 10**(np.linspace(np.log10(0.2),np.log10(75.),bin_num))
	pts_all=np.transpose(np.array([X_all,Y_all,Z_all]))
	pts=np.transpose(np.array([X,Y,Z]))
	T = spatial.cKDTree(pts)
	T_all=spatial.cKDTree(pts_all)
	n=T.count_neighbors(T_all,bins)
	return ( n[1:]-n[:-1])/2 , bins

def counter_bruteforce(X,Y,Z,dr):
	
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
	hist=0
	a=np.log10(0.2)
	b=np.log10(75.)
	bins_array=np.linspace(a,b,20)
	bins_array=10.**bins_array
	for x in range(0,len(X)):
		X_diff = np.abs(X[x]-X[x+1:])
		Y_diff = np.abs(Y[x]-Y[x+1:])
		Z_diff = np.abs(Z[x]-Z[x+1:])
		X_diff = np.minimum(X_diff,300-X_diff)
		Y_diff = np.minimum(Y_diff,300-Y_diff)
		Z_diff = np.minimum(Z_diff,300-Z_diff) 
		sum_d = np.sqrt(X_diff**2 + Y_diff**2 + Z_diff**2)
		hist1,edge = np.histogram(sum_d,bins=bins_array)
		hist+=hist1
		
	return hist


def counter_spherical_select(X,Y,Z,dr):
	
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
	hist=0
	a=np.log10(0.2)
	b=np.log10(75.)
	bins_array=np.linspace(a,b,20)
	bins_array=10.**bins_array
	#a=0.2
	#b=75
	for x in range(0,len(X)):
		X_diff = np.abs(X[x]-X[x+1:])
		Y_diff = np.abs(Y[x]-Y[x+1:])
		Z_diff = np.abs(Z[x]-Z[x+1:])
		X_diff = np.minimum(X_diff,300-X_diff)
		Y_diff = np.minimum(Y_diff,300-Y_diff)
		Z_diff = np.minimum(Z_diff,300-Z_diff) 
		sum_d = np.sqrt(X_diff**2 + Y_diff**2 + Z_diff**2)
		index=np.where(sum_d<=80)[0]
		hist1,edge = np.histogram(sum_d[index],bins=bins_array)
		hist+=hist1
		
	return hist,edge
