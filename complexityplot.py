import numpy as np
import matplotlib.pyplot as plt

n,t1,t2,t3,t4=np.loadtxt('Time.txt',unpack=True, skiprows=1)
plt.plot(n,t1,'-o',label='bruteforce')
plt.plot(n,t2,'-o',label='kdtree')
plt.plot(n,t3,'-o',label='bruteforce_cubical')
plt.plot(n,t4,'-o',label='bruteforce_spherical')
plt.legend()
plt.title('Time Complexity Analysis')
plt.xlabel('No of Points')
plt.ylabel('Time in secs')
plt.savefig('TimeAnalysis_fewmore.pdf')
plt.show()
