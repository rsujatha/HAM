import numpy as np
import matplotlib.pyplot as plt
import pylab



X,Y,Z,M200b,PID  = np.loadtxt("out_1.parents",skiprows=16,usecols=[8,9,10,20,41],unpack=True)
np.savetxt('x_y_z_m_sim.txt',np.transpose([X,Y,Z,M200b,PID]),fmt=['%.6f','%.6f','%.6f','%.5e','%.6f'], header = 'X\tY\tZ\tM200b\tPID')

## Calculating 


rho_L=75320/(191)**3.0
print ("rhol=",rho_L)
m=1e10   ## initial mass
dm=1e10  ## small increment in mass

i=1e-2
rho_m=1.48*i  ## initial density of mass from simulation
while not ((rho_m <= 1.1016*i) and (rho_m >= 1.0584*i)): ## This range is within 2% of rho_L


 range_m = np.where((M200b>= m)&(M200b<=1e15))[0]
 N=range_m.size
 print N
 rho_m=N/(300)**3.0
 m= dm+m
print rho_m
X1=X[range_m] 
Y1=Y[range_m]
Z1=Z[range_m]
M200b_new= M200b[range_m] 
print M200b_new
print X1
np.savetxt('x1_y1_z1_m_sim.txt',np.transpose([X1,Y1,Z1,M200b_new]),fmt=['%.6f','%.6f','%.6f','%.5e'], header = 'X1\tY1\tZ1\tM200b_new')










