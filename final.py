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
	plt.plot(edge,Xi,'.',color=color[x],label=label[x])
plt.xlabel('Distance(r)')
plt.legend()
plt.ylabel(r'$\xi$(r)')
plt.xscale('log')
plt.yscale('log')
plt.show()
