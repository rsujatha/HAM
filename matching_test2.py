from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

	
# loading text
luminosity = np.loadtxt ('abs_mag_data.txt')
luminosity=abs(luminosity)
print luminosity
X,Y,Z,M = np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)

#sorting in increasing order
luminosity.sort()
M = np.sort(M)
print luminosity

# cdf for both luminosity and mass
np.concatenate([luminosity,luminosity[[-1]]])
np.concatenate([M,M[[-1]]])

luminosityFunction=np.arange(luminosity.size)/float(luminosity.size)
MFunction=np.arange(M.size)/float(M.size)
plt.plot(M,MFunction)
plt.title('Halo Mass Function cdf')
plt.xlabel('Halo Mass')
plt.show()
plt.clf()
plt.plot(luminosity,luminosityFunction)
plt.xlabel('Absolute of Absolute Magnitude')
plt.title('Luminosity Function cdf')
plt.show()
plt.clf()
# interpolating 
Luminosity_match=np.linspace(luminosity[0],luminosity[-1],100)
cdf_match=np.interp(Luminosity_match,luminosity,luminosityFunction)
Mass_match=np.interp(cdf_match,MFunction, M)

#Mass_match
plt.plot(Mass_match,Luminosity_match,'.r')
plt.xscale('log')
plt.ylabel('Absolute of Absolute Magnitue')
plt.xlabel('Halo Mass')
plt.show()
















print("--- %s seconds ---" % (time.time() - start_time))
