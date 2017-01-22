from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

	
# loading text
luminosity = np.loadtxt ('abs_mag_data.txt')
X,Y,Z,M = np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)

#sorting in increasing order
luminosity.sort()
M = np.sort(M)
print M[-11:-1]
#M.pop()
M = M[:-1]
# cdf for both luminosity and mass
#np.concatenate([luminosity,luminosity[[-1]]])
#np.concatenate([M,M[[-1]]])

luminosityFunction=np.arange(luminosity.size)/float(luminosity.size)
MFunction=np.arange(M.size)/float(M.size)
plt.plot(M,MFunction)
plt.show()
plt.clf()
# interpolating 
cdf=np.linspace(0,1,1000)
Luminosity_match=np.interp(cdf, luminosityFunction, luminosity)
Mass_match=np.interp(cdf,MFunction, M)

#Mass_match
plt.plot(Mass_match,Luminosity_match,'.r')
plt.xscale('log')
plt.show()
















print("--- %s seconds ---" % (time.time() - start_time))
