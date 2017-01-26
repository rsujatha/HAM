##plot to visualise the galaxies in the dark matter potential
##Blue is the dark matter while yellow are the galaxies 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)
#L=np.sort(L)
#print L[0],L[-1]
fig=plt.figure()
ax = fig.add_subplot(1,2,1, projection='3d')
s = [float(n)/len(X) for n in range(len(X))]
ax.scatter(X,Y,Z,'.',color='#a52a2a',s=0.03)
ax.scatter(X,Y,Z,'.',color='y',s=L/2e13)
ax.set_facecolor('black')
ax.view_init(elev=30., azim=58)
ax.w_xaxis.set_pane_color((0,0,0))
ax.w_yaxis.set_pane_color((0,0,0))
ax.w_zaxis.set_pane_color((0,0,0))
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.tick_params(axis='z',colors='white')
ax.set_title('Galaxies in Dark Matter',color='white',rotation='vertical',x=1,y=1)

ax = fig.add_subplot(1,2,2, projection='3d')
ax.scatter(X,Y,Z,'.',color='#a52a2a',s=0.03)
ax.set_facecolor('black')
ax.view_init(elev=30., azim=58)
ax.w_xaxis.set_pane_color((0,0,0))
ax.w_yaxis.set_pane_color((0,0,0))
ax.w_zaxis.set_pane_color((0,0,0))
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.tick_params(axis='z',colors='white')
ax.set_title( 'Dark Matter',color='white',rotation='vertical',x=0.8,y=1)
for angle in range(0, 360):
    ax.view_init(elev=30., azim=58+angle)
    plt.draw()
    plt.pause(.001)
plt.show()
