import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib import rc
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )


label = ['M$<-20$','M$<-21$','M$<-22$']
color = ['r','b','g']
xi_files = np.sort(glob.glob("Xi_mockgalaxySubset*"))
hist_files = np.sort(glob.glob("hist_mockgalaxySubset*"))

for x in range (xi_files.size):
	Xi = np.loadtxt(xi_files[x],unpack=True)
	hist,edge = np.loadtxt(hist_files[x],unpack=True)
	ind_zero = np.where (Xi>1e-6)[0]
	plt.plot(edge[ind_zero],Xi[ind_zero],'-o',color=color[x],label=label[x])
	#~ plt.plot(edge,Xi,'-o',color=color[x],label=label[x])
plt.xlabel('Distance(r)')
plt.legend()
plt.ylabel(r'$\xi$(r)')
plt.xscale('log')
plt.yscale('log')
plt.savefig('Clustering_at_different_scales_for_diff_luminosity_50.pdf')
plt.show()
