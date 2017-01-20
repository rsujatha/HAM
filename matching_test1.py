import numpy as np
import matplotlib.pyplot as plt

show_flag = True
show_flag = False 				# Comment this line if the plots of histogram need to be seen
luminosity = np.loadtxt ('abs_mag_data.txt')

X,Y,Z,M = np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)

lum_hist = np.histogram (luminosity,1000)

plt.plot(lum_hist[1][:-1],lum_hist[0],'.')
plt.xscale('log')
if show_flag:plt.show()
plt.clf()

mass_hist = np.histogram (M,1000)

plt.plot(mass_hist[1][:-1],mass_hist[0],'.')
plt.xscale('log')
if show_flag:plt.show()
plt.clf()

x_max,x_min = np.max(X),np.min(X)
y_max,y_min = np.max(Y),np.min(Y)
z_max,z_min = np.max(Z),np.min(Z)

print 'x_max,x_min:\t',x_max,x_min
print 'y_max,y_min:\t',y_max,y_min
print 'z_max,z_min:\t',z_max,z_min

delta = 1		# in h^(-1)Mpc
Lum_box_length = 191 # in h^(-1)Mpc

origin_array=[]
for x in range (x_min,x_max-Lum_box_length +1,delta):
	for y in range (y_min,y_max-Lum_box_length+1 ,delta):
		for z in range (z_min,z_max-Lum_box_length+1 ,delta):
			ind = np.where (((X<x+Lum_box_length) & (X>=x)) & ((Y<y+Lum_box_length) & (Y>=y)) & ((Z<z+Lum_box_length) & (Z>=z))) [0]
			if abs(ind.size-luminosity.size)<0.1*luminosity.size:
				origin_array.append([x,y,z])
print np.shape(origin_array)[0]
