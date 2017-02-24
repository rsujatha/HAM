from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time

X,Y,Z,M,PID = np.loadtxt('x_y_z_m_sim.txt',unpack=True,skiprows=1)
#~ h=0.7
h=1
TotalMass=np.sum(M)*h
#print TotalMass

Volume=(300/h)**3
BGDensity=TotalMass/Volume
#print BGDensity
M20 = np.loadtxt('mockgalaxySubset_M_less_than_-20.txt',unpack=True,skiprows=1,usecols=[0])
M21 = np.loadtxt('mockgalaxySubset_M_less_than_-21.txt',unpack=True,skiprows=1,usecols=[0])
M22 = np.loadtxt('mockgalaxySubset_M_less_than_-22.txt',unpack=True,skiprows=1,usecols=[0])

M20_min=np.min(M20)*h
M21_min=np.min(M21)*h
M22_min=np.min(M22)*h

Density=BGDensity*178

R20=(3/(4*np.pi)*M20_min/Density)**(1/3)
R21=(3/(4*np.pi)*M21_min/Density)**(1/3)
R22=(3/(4*np.pi)*M22_min/Density)**(1/3)

print R20,R21,R22











