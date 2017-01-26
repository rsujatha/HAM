#Code for generating an outer shell to the existing cubic simulation box 
# Data points to be generated for portion adjoining 6 faces + 12 edges + 8 corners= 26 boxes of data sets
#X axis runs left to right Y axis runs bottom to top Z axis runs inside to outside

import numpy as np
M,L,X,Y,Z = np.loadtxt ('output_of_3_1.txt',unpack=True, skiprows=1)


## Box 1 - Right Face 			R
sel_ind = np.where(X<=75)[0]  
X1=X[sel_ind]+300
Y1=Y[sel_ind]
Z1=Z[sel_ind]

## Box 2 - Left Face 			L
sel_ind = np.where(X>=75)[0]  
X2=X[sel_ind]-300
Y2=Y[sel_ind]
Z2=Z[sel_ind]

## Box 3 - Top Face 			T
sel_ind = np.where(Y<=75)[0]  
X3=X[sel_ind]
Y3=Y[sel_ind]+300
Z3=Z[sel_ind]

## Box 4 - Bottom Face		 	B
sel_ind = np.where(Y>=75)[0]  
X4=X[sel_ind]
Y4=Y[sel_ind]-300
Z4=Z[sel_ind]

## Box 5 - Back Face 			K
sel_ind = np.where(Z>=75)[0]  
X5=X[sel_ind]
Y5=Y[sel_ind]
Z5=Z[sel_ind]-300

## Box 6 - Front Face 			F
sel_ind = np.where(Z<=75)[0]  
X6=X[sel_ind]
Y6=Y[sel_ind]
Z6=Z[sel_ind]+300

## Box 7 - Edge RT
sel_ind = np.where((X<=75) & (Y<=75))[0]  
X7=X[sel_ind]+300
Y7=Y[sel_ind]+300
Z7=Z[sel_ind]

## Box 8 - Edge LT
sel_ind = np.where((X>=75)&(Y<=75))[0]  
X8=X[sel_ind]-300
Y8=Y[sel_ind]+300
Z8=Z[sel_ind]

## Box 9 - Edge KT
sel_ind = np.where((Z>=75)&(Y<=75))[0]  
X9=X[sel_ind]
Y9=Y[sel_ind]+300
Z9=Z[sel_ind]-300

## Box 10 -Edge FT
sel_ind = np.where((Z<=75)&(Y<=75))[0]  
X10=X[sel_ind]
Y10=Y[sel_ind]+300
Z10=Z[sel_ind]+300

## Box 11 - Edge RB
sel_ind = np.where((X<=75) & (Y>=75))[0]  
X11=X[sel_ind]+300
Y11=Y[sel_ind]-300
Z11=Z[sel_ind]

## Box 12 - Edge LB
sel_ind = np.where((X>=75)&(Y>=75))[0]  
X12=X[sel_ind]-300
Y12=Y[sel_ind]-300
Z12=Z[sel_ind]

## Box 13 - Edge KB
sel_ind = np.where((Z>=75)&(Y>=75))[0]  
X13=X[sel_ind]
Y13=Y[sel_ind]-300
Z13=Z[sel_ind]-300

## Box 14 - Edge FB
sel_ind = np.where((Z<=75)&(Y>=75))[0]  
X14=X[sel_ind]
Y14=Y[sel_ind]-300
Z14=Z[sel_ind]+300

## Box 15 - Edge RF  
sel_ind = np.where((X<=75)&(Z<=75))[0]  
X15=X[sel_ind]+300
Y15=Y[sel_ind]
Z15=Z[sel_ind]+300

## Box 16 - Edge LF
sel_ind = np.where((X>=75)&(Z<=75))[0]  
X16=X[sel_ind]-300
Y16=Y[sel_ind]
Z16=Z[sel_ind]+300

## Box 17 - Edge RK
sel_ind = np.where((X<=75)&(Z>=75))[0]  
X17=X[sel_ind]+300
Y17=Y[sel_ind]
Z17=Z[sel_ind]-300

## Box 18 - Edge LK
sel_ind = np.where((X>=75)&(Z>=75))[0]  
X18=X[sel_ind]-300
Y18=Y[sel_ind]
Z18=Z[sel_ind]-300

## Box 19 - Corner RTK
sel_ind = np.where((X<=75)&(Y<=75)&(Z>=75))[0]  
X19=X[sel_ind]+300
Y19=Y[sel_ind]+300
Z19=Z[sel_ind]-300 

## Box 20 - Corner RBK
sel_ind = np.where((X<=75)&(Y>=75)&(Z>=75))[0]  
X20=X[sel_ind]+300
Y20=Y[sel_ind]-300
Z20=Z[sel_ind]-300

## Box 21 - Corner RTF
sel_ind = np.where((X<=75)&(Y<=75)&(Z<=75))[0]  
X21=X[sel_ind]+300
Y21=Y[sel_ind]+300
Z21=Z[sel_ind]+300

## Box 22 - Corner RBF
sel_ind = np.where((X<=75)&(Y>=75)&(Z<=75))[0]  
X22=X[sel_ind]+300
Y22=Y[sel_ind]-300
Z22=Z[sel_ind]+300

## Box 23 - Corner LTK
sel_ind = np.where((X>=75)&(Y<=75)&(Z>=75))[0]  
X23=X[sel_ind]-300
Y23=Y[sel_ind]+300
Z23=Z[sel_ind]-300 

## Box 24 - Corner LBK
sel_ind = np.where((X>=75)&(Y>=75)&(Z>=75))[0]  
X24=X[sel_ind]-300
Y24=Y[sel_ind]-300
Z24=Z[sel_ind]-300

## Box 25 - Corner LTF
sel_ind = np.where((X>=75)&(Y<=75)&(Z<=75))[0]  
X25=X[sel_ind]-300
Y25=Y[sel_ind]+300
Z25=Z[sel_ind]+300

## Box 26 - Corner LBF
sel_ind = np.where((X>=75)&(Y>=75)&(Z<=75))[0]  
X26=X[sel_ind]-300
Y26=Y[sel_ind]-300
Z26=Z[sel_ind]+300


X_shell = np.concatenate((X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26))
Y_shell = np.concatenate((Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21,Y22,Y23,Y24,Y25,Y26))
Z_shell = np.concatenate((Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,Z11,Z12,Z13,Z14,Z15,Z16,Z17,Z18,Z19,Z20,Z21,Z22,Z23,Z24,Z25,Z26))
print X_shell.size, Y_shell.size,Z_shell.size


