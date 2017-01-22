import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X,Y,Z,M = np.loadtxt ('x_y_z_m_sim_selected.txt',unpack=True, skiprows=1)
fig=plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot(X,Y,Z,'.',markersize='.02')
ax.view_init(elev=30., azim=58)
ax.set_xlabel('$U_{3n-2}$')
ax.set_ylabel('$U_{3n-1}$')
ax.set_zlabel('$U_{3n}$')
ax.set_title('3-D distribution PiE',rotation='vertical',x=1,y=1)
plt.show()
