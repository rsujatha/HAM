import numpy as np
import matplotlib.pyplot as plt

#~ chatter =True
chatter=False

X,Y,Z,M200b = np.loadtxt("x_y_z_m_sim_selected.txt",skiprows=1,unpack=True)
L=np.loadtxt("abs_mag_data.txt",unpack=True)
No_of_L=L.size


## Calculating 


rho_L=No_of_L/(191)**3.0
if chatter:print ("Number density of Yang data:",rho_L)
massmin=3e11   ## initial mass
massmax=np.max(M200b)
if chatter:print "Maximum mass and minimum mass in simulation",massmin, massmax
dm=1e8  ## small increment in mass

rho_m=1.48e-2 ## initial number density of simulation data
err = 0.007
while not ((rho_m <= rho_L*(1+err)) and (rho_m >= rho_L*(1-err))): ## This range is within 2% of rho_L
	range_m = np.where((M200b>= massmin)&(M200b<=massmax))[0]
	N=range_m.size
	rho_m=N/(300)**3.0
	massmin= dm+massmin

if chatter:print 'Reduced number density:',rho_m
X1=X[range_m] 
Y1=Y[range_m]
Z1=Z[range_m]
M200b_new= M200b[range_m] 
np.savetxt('x1_y1_z1_m_sim_selected.txt',np.transpose([X1,Y1,Z1,M200b_new]),fmt=['%.6f','%.6f','%.6f','%.5e'], header = 'X1\tY1\tZ1\tM200b_new')
print 'Lower limit of mass of simulation is determined; \t', '{0:.4e}'.format(massmin)

###Check
if chatter:print "density of yang data:",No_of_L/(191)**3.0
#~ print "No",No_of_L
if chatter:print "density calculated in the code:",N/(300)**3.0 

