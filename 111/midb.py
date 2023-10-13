import numpy             as np
import matplotlib.pyplot as plt

nmax = 10000
X, Y = np.empty(nmax), np.empty(nmax)
X[0] = 0.
Y[0] = 0.
A = [ 0.000,  0.845,  0.200, -0.150]
B = [ 0.000,  0.035, -0.260,  0.240]
C = [ 0.000,  0.000,  0.000,  0.000]
D = [ 0.000, -0.030,  0.255,  0.250]
E = [ 0.200,  0.820,  0.245,  0.200]
F = [-0.012,  1.600,  0.290,  0.680]
P = np.random.rand(nmax-1)

for n in range(nmax-1):
    if(P[n] < 0.01):
        i = 0
    elif(0.01 <= P[n] < 0.86):
        i = 1
    elif(0.86 <= P[n] < 0.93):
        i = 2
    else:
        i = 3
    
    X[n+1] = round(A[i]*X[n]+B[i]*Y[n]+C[i], 3)
    Y[n+1] = round(D[i]*X[n]+E[i]*Y[n]+F[i], 3)

plt.plot(X, Y, 'g.')