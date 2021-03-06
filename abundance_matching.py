from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

from matplotlib import rc
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']} )

#~ show_flag = True
show_flag = False

start_time = time.time()

# loading text
mags = np.loadtxt ('abs_mag_data.txt')
X,Y,Z,Mass= np.loadtxt ('x1_y1_z1_m_sim_selected.txt',unpack=True, skiprows=1)

#sorting in increasing order
luminosity = np.sort(10**(-(mags-4.77)/2.5))		# In unit of Solar luminosity
M = np.sort(Mass)


# cdf for both luminosity and mass

luminosityFunction=np.arange(luminosity.size)/float(luminosity.size)
MFunction=np.arange(M.size)/float(M.size)


















plt.plot(M,MFunction)
plt.title('Halo Mass cdf')
plt.xlabel('Halo Mass M')
plt.ylabel('$n(<M)$')
plt.xscale('log')
#plt.yscale('log')

plt.savefig('halo_mass_cdf.pdf')
if show_flag: plt.show()
plt.clf()

plt.plot(luminosity,luminosityFunction)
plt.xscale('log')
#plt.yscale('log')

plt.title('Luminosity cdf')
plt.xlabel('Luminosity L' )
plt.ylabel('$n(<L)$')
plt.savefig('luminosity_cdf.pdf')
if show_flag: plt.show()
plt.clf()


# Interpolating for a uniform Luminosity binning
Luminosity_match=np.linspace(luminosity[0],luminosity[-1],1e6)
cdf_match=np.interp(Luminosity_match,luminosity,luminosityFunction)
Mass_match=np.interp(cdf_match,MFunction, M)


## Obtaining the Luminosity values for the Galaxies in the simulations
lumi_for_all = np.interp(Mass,Mass_match,Luminosity_match)

# Mass_match
plt.plot(Mass_match,Luminosity_match,'b')
plt.xscale('log')
#~ plt.plot(Mass,lumi_for_all,'.r')
plt.yscale('log')
plt.ylabel('Luminosity')
plt.xlabel('Halo Mass Msun/h')
plt.savefig ('Mass_lum_calc.pdf')
if show_flag: plt.show()
plt.show()
plt.clf()

### Saving the Output file for use in next part
np.savetxt('output_of_3_1.txt',np.transpose([Mass,lumi_for_all,X,Y,Z]), fmt = ['%.6e','%.6e','%.6e','%.6e','%.6e'],header='Mass in h-1M_sun\tLuminosity in L_sun\tX in h-1Mpc\tY in h-1Mpc \tZ in h-1Mpc')


#~ print("--- %s seconds ---" % (time.time() - start_time))
lumi_for_all_sort=np.sort(lumi_for_all)
luminosityFunction_SanityCheck=np.arange(lumi_for_all_sort.size)/float(lumi_for_all_sort.size)

plt.plot(luminosity,luminosityFunction,label="Cdf from Yang Data",color='g')
plt.plot(lumi_for_all_sort,luminosityFunction_SanityCheck,'r--',label="Cdf from Matched Luminosity")
plt.xlabel('Luminosity')
plt.ylabel('Cumulative Distribution Function')
plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.title('Cumulative Distribution Function of Yang Data and Matched Mock Luminosity ')
plt.savefig('Cdf_SanityCheck.pdf')
if show_flag: plt.show()
plt.clf()
#~ bins=np.linspace(min(np.log10(luminosity)),max(np.log10(luminosity)),10)
bins=10
hist_yang,edge_yang=np.histogram(np.log10(luminosity),bins)
hist_mock,edge_mock=np.histogram(np.log10(lumi_for_all_sort),bins)

bin_yang = edge_yang[1:]-edge_yang[:-1]
bin_mock = edge_mock[1:]-edge_mock[:-1]
ind_zero = np.where(hist_mock>=1e-9)[0]
ind_yang = np.where(hist_yang>=1e-9)[0]
plt.plot(10**edge_yang[:-1][ind_yang],hist_yang[ind_yang]/(191)**3/bin_yang[ind_yang],'g',label='Yang Data')
plt.plot(10**edge_mock[:-1][ind_zero],hist_mock[ind_zero]/(300)**3/bin_mock[ind_zero],'r',label='Mock Galaxy Data')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Luminosity')
plt.ylabel(r'Normalised number density of galaxies (in $(h^{-1}Mpc)^{-3}$ $(ln (L))^{-1}$) ')
plt.legend()
plt.title('Luminosity function')
plt.savefig('Histogram_SanityCheck.pdf')
if show_flag: plt.show()
print 'Abundance matching done'
fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(M,MFunction,linewidth=2.5,color='g')
ax1.plot([1.9468e12,1.9468e12],[0,0.8],'b')
ax1.set_title('Halo Mass Cumulative Distribution Function')
ax1.set_xlabel('Halo Mass M')
ax1.set_ylabel('$n(<M)$')
ax1.set_xscale('log')
plt.grid()
ax2.plot(luminosity,luminosityFunction,linewidth=2.5,color='g')
ax2.plot([1.372e10,1.372e10],[0,0.8],'b')

ax2.set_title('Luminosity Cumulative Distribution Function')
ax2.set_xlabel('Luminosity L')
ax2.set_ylabel('$n(<L)$')
ax2.set_xscale('log')

plt.grid()
transFigure = fig.transFigure.inverted()

coord1 = transFigure.transform(ax1.transData.transform([1.9468e12,0.8]))
coord2 = transFigure.transform(ax2.transData.transform([1.372e10,0.8]))


line = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
                               transform=fig.transFigure)
                               
fig.lines = line,

plt.savefig('AbundanceM.pdf')
plt.clf()
