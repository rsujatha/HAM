from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

	
# loading text
mags = np.loadtxt ('abs_mag_data.txt')
X,Y,Z,Mass= np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)

#sorting in increasing order
luminosity = np.sort(10**(-(mags-4.77)/2.5))		# In unit of Solar luminosity
M = np.sort(Mass)
#print luminosity

# cdf for both luminosity and mass

luminosityFunction=np.arange(luminosity.size)/float(luminosity.size)
MFunction=np.arange(M.size)/float(M.size)


plt.plot(M,MFunction)
plt.title('Halo Mass Function cdf')
plt.xlabel('Halo Mass')
#plt.show()
plt.clf()

plt.plot(luminosity,luminosityFunction)
plt.xlabel('Luminosity')
#plt.gca().invert_xaxis()
plt.xscale('log')
plt.title('Luminosity Function cdf')
#plt.show()
plt.clf()


# Interpolating for a uniform Luminosity binning
Luminosity_match=np.linspace(luminosity[0],luminosity[-1],1e4)
cdf_match=np.interp(Luminosity_match,luminosity,luminosityFunction)
Mass_match=np.interp(cdf_match,MFunction, M)


## Obtaining the Luminosity values for the Galaxies in the simulations
lumi_for_all = np.interp(Mass,Mass_match,Luminosity_match)

#Mass_match
plt.plot(Mass_match,Luminosity_match,'.r')
#plt.xscale('log')
#~ plt.plot(Mass,lumi_for_all,'.r')
plt.yscale('log')
plt.ylabel('Luminosity')
plt.xlabel('Halo Mass')
plt.savefig ('Mass_lum_calc.pdf')
plt.show()

plt.clf()

### Saving the Output file for use in next part
np.savetxt('output_of_3_1.txt',np.transpose([Mass,lumi_for_all,X,Y,Z]), fmt = ['%.6e','%.6e','%.6e','%.6e','%.6e'],header='Mass in h-1M_sun\tLuminosity in L_sun\tX in h-1Mpc\tY in h-1Mpc \tZ in h-1Mpc')


print("--- %s seconds ---" % (time.time() - start_time))
