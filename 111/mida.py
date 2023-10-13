import numpy             as np

X, Y = np.empty(10), np.empty(10)
A =  0.845
B =  0.035
C =  0.000
D = -0.030
E =  0.820
F =  1.600
n = np.arange(0, 10) 

X[0] = float(input('input X\u2081:'))
Y[0] = float(input('input Y\u2081:'))

for i in range(9):
    X[i+1] = round(A*X[i]+B*Y[i]+C, 3)
    Y[i+1] = round(D*X[i]+E*Y[i]+F, 3)

data = np.column_stack((n, X, Y))
np.savetxt('Aout_format.txt', data, fmt='%3d %5.3f %5.3f', header='n X     Y')