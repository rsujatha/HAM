#Generates three subsets of mock galaxy catalogs.
import numpy as np

## Defininig the value of magnitude and converting it into Luminosity
mags=np.array([-20,-21,-22])
luminosity	 = 10**(-(mags-4.77)/2.5)

## Loading input file
M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)

## Selecting three mocks
i=0
for lum_lim in luminosity:
	index=np.where(L>lum_lim)
	L_new=L[index]
	X_new=X[index]
	Y_new=Y[index]
	Z_new=Z[index]
	M_new=M[index]
	string='mockgalaxySubset_M<_'+str(mags[i])+'.txt'
	np.savetxt(string,np.transpose([M_new,L_new,X_new,Y_new,Z_new]), fmt = ['%.6e','%.6e','%.6e','%.6e','%.6e'],header='Mass in h-1M_sun\tLuminosity in L_sun\tX in h-1Mpc\tY in h-1Mpc \tZ in h-1Mpc')
	print string," created"
	print "Sanity Check: Luminosity limit is:",str(luminosity[i])," and Luminosity minimum of saved txt is:",np.min(L_new)
	i=i+1
    
