import numpy as np
import pair_counting_function as pcf
import time
import matplotlib.pyplot as plt
from matplotlib import rc
import glob

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )

begin=time.time()

pi=np.pi

label = ['M$<-20$','M$<-21$','M$<-22$']
color = ['r','b','g']
mock_files = np.sort(glob.glob("mockgalaxySubse*.txt"))
for x in range (mock_files.size):
	M,L,X,Y,Z = np.loadtxt (mock_files[x],unpack=True, skiprows=1)
	bin_num=10
	pairsN=float(X.size*(X.size-1)/2.)
	DD,bins=pcf.counter_kdtree(X,Y,Z,bin_num)
	DD=DD/pairsN
	rr=bins[1:]**3-bins[:-1]**3
	RR = 4/3.*pi*(rr)/300.**3
	Xi=DD/RR-1
	#~ print Xi.size
	bins_array=(bins[1:]+bins[:-1])/2.
	item = mock_files[x]
	file_name = item.split('.')[0]
	kdtree_file_name = 'kdtree_'+file_name+'.txt'
	
	np.savetxt(kdtree_file_name,np.transpose([bins_array,Xi]),header='r\tXi')
print "Time taken\t" , time.time()-begin
print "All files created\nRun python final_kdtree.py to get the plot"

