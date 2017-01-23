from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def two_pt_distance(r,dr,X,Y,Z):
	'''
	
	
	Determines the number of the galaxies with distance between them within 'r' and 'r+dr' 
	
	Input:
	------------------------
	r			: The lower limit of the distance between two galaxies
	dr			: Difference between upper and lower limit of the galaxies
	X			: X - coordinate of the galaxies
	Y			: Y - coordinate of the galaxies
	Z			: Z - coordinate of the galaxies
	
	Output:
	------------------------
	DD 			: Number of galaxies between r and r+dr
	
	
	'''
	DD = 0				## write the function
	
	return DD


M,L,X,Y,Z = np.loadtxt('output_of_3_1.txt', unpack=True, skiprows=1)
pi = np.pi

r_array = np.arange(1,150,1)
dr = r_array[1]-r_array[0]
for r in r_array:
	
	RR = 4*pi*r**2*dr 		# originally the formula is RR = 4*pi*r**3*d(ln (r)), d () being differential operator
	DD = two_pt_distance(r,dr,X,Y,Z)
	chi = DD/RR-1
