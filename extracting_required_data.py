import numpy as np

X,Y,Z,M,PID = np.loadtxt('x_y_z_m_sim.txt',unpack=True,skiprows=1)

sel_ind = np.where(PID==-1)[0] 		# Creating a mask for data selection


#Filtering the data according to mask
X,Y,Z,M = X[sel_ind],Y[sel_ind],Z[sel_ind],M[sel_ind]

## Command to save file
np.savetxt('x_y_z_m_sim_selected.txt',np.transpose([X,Y,Z,M]),fmt=['%.6f','%.6f','%.6f','%.5e'], header='X\tY\tZ\tM200b') 
print "Shortened file created"
