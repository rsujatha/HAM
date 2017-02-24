import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib import rc
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )


label = ['M$<-20$','M$<-21$','M$<-22$']
color = ['r','b','g']
kdtree_files = np.sort(glob.glob("kdtree_mockgalaxySubset*"))

for x in range (kdtree_files.size):
	bins_array,Xi = np.loadtxt(kdtree_files[x],unpack=True,skiprows=1)
	plt.plot(bins_array,Xi,'-o',color=color[x],label=label[x])

plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig('kdtreeXi.pdf')
plt.show()

