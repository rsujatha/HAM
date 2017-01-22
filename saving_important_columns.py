import numpy as np

yang_data = np.loadtxt("yangDR7_centrals.txt",skiprows=1,usecols=[0],unpack=True)

X,Y,Z,M200b,PID  = np.loadtxt("out_1.parents",skiprows=16,usecols=[8,9,10,20,41],unpack=True)
#out_data = np.loadtxt("out_1.parents",skiprows=16,unpack=True)
#print np.shape(yang_data),np.shape(out_data)
np.savetxt('abs_mag_data.txt',yang_data,fmt=['%.6f'])
np.savetxt('x_y_z_m_sim.txt',np.transpose([X,Y,Z,M200b,PID]),fmt=['%.6f','%.6f','%.6f','%.5e','%.6f'], header = 'X\tY\tZ\tM200b\tPID')
