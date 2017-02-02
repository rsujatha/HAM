import numpy as np
import pair_counting_function as pcf
import time
import glob


dr 		= 0.1
pi = np.pi
bins = int((75-0.2)/dr)
hist=np.zeros(bins)

chatter = False 		# Put Chatter True if want more output (like timing info of each segment) on terminal
skip	= 1000			# Number of iteration to skip before printing timing info


list_of_mass_sorted_catalogs = glob.glob('mockgalaxySubset*')

for item in list_of_mass_sorted_catalogs:
	
	start_time = time.time()
	init_time = time.time()
	M,L,X,Y,Z = np.loadtxt (item,unpack=True, skiprows=1)
	
	if chatter:print 'Data loaded\nTime taken\t:',time.time()-start_time
	start_time = time.time()

	for n in range (X.size):			#Put X.size later
		hist_temp,edge = pcf.counter_version4(dr,X,Y,Z,n,chatter) 			# Version 3 can also be implemented 
		hist+= hist_temp
		if n%skip==0 and chatter:
			print "Number of points accumulated in 100th bin", hist[99]
			print "Running loops {} iterations done,\nTime for prev {} run is\t:".format(n,skip),time.time()-start_time
			start_time = time.time()

	if chatter: print "Completed\nTime for entire operation is\t:",time.time()-init_time
	file_name = item.split('.')
	hist_file_name = 'hist_'+file_name+'.txt'
	np.savetxt (hist_file_name, np.transpose([hist,edge[:-1]]), fmt=['%.6f','%.6f'])


	DD = hist
	DD/=(X.size*(X.size-1))/2

	RR = 4*pi*(edge[:-1])**2*dr/(300)**3 				# originally the formula is RR = 4*pi*(r/L)**3*d(ln (r)), d () being differential operator

	Xi = DD/RR-1
	xi_file_name = 'Xi_'+file_name+'.txt'
	np.savetxt(xi_file_name,np.transpose(Xi),fmt='%.6f')
if chatter: print "All files created\nRun python final.py to get the plot"
