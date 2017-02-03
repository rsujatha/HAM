import numpy as np
import pair_counting_function as pcf
import time
import glob


#~ dr 	= 0.1
bin_num	= float(raw_input("Enter the value of number of logarithmic bins:\t"))

### using logarithmic binning in dr 
bins = np.exp(np.linspace(np.log(0.2),np.log(75),bin_num))
pi = np.pi
#~ bins = int((75-0.2)/dr)
hist=np.zeros(bins.size-1)

chatter = True 			# Put Chatter True if want more output (like timing info of each segment) on terminal
skip	= 1000			# Number of iteration to skip before printing timing info


list_of_mass_sorted_catalogs = glob.glob('mockgalaxySubset*')

for item in list_of_mass_sorted_catalogs:
	
	start_time = time.time()
	init_time = time.time()
	if chatter: print "\n\nWorking with {}".format(item),'\n\n'
	M,L,X,Y,Z = np.loadtxt (item,unpack=True, skiprows=1)
	if chatter: print 'Data loaded\nTime taken\t:',time.time()-start_time
	start_time = time.time()

	for n in range (X.size):			#Put X.size later
		hist_temp,edge = pcf.counter(X,Y,Z,n,chatter,bins) 			 
		hist+= hist_temp
		if n%skip==0 and chatter:
			print "Running loops {} iterations done,\nTime for prev {} run is\t:".format(n,skip),time.time()-start_time
			start_time = time.time()

	if chatter: print "Completed\nTime for entire operation is\t:",time.time()-init_time
	file_name = item.split('.')[0]
	hist_file_name = 'hist_'+file_name+'.txt'
	np.savetxt (hist_file_name, np.transpose([hist,edge[:-1]]), fmt=['%.6f','%.6f'])


	DD = hist
	DD/=(X.size*(X.size-1))/2
	#~ d_lnr = (bins[1:]/bins[:-1])
	d_lnr = np.log(bins[1:]/bins[:-1])
	RR = 4*pi*(bins[:-1])**3*d_lnr/(300)**3 				

	Xi = DD/RR-1
	xi_file_name = 'Xi_'+file_name+'.txt'
	np.savetxt(xi_file_name,np.transpose(Xi),fmt='%.6f')
if chatter: print "All files created\nRun python final.py to get the plot"
