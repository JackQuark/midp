import numpy             as np
import matplotlib.pyplot as plt
import sys
"""
"""
#input x0 and y0
x0 = int(sys.argv[1])
y0 = int(sys.argv[2])

#if x0 or y0 out of range, end this code.
if(x0 > 100) or (y0 > 100):
    print('error')
    sys.exit()

#declare some arrays and variables
t    = np.arange(0, 100.1, 0.1)
dt   = 0.1
x    = np.zeros(1001)
y    = np.zeros(1001)
x[0] = x0
y[0] = y0

#calculate all value of x and y by Euler method
for i in range(1000):
    x[i+1] = x[i] + (0.1*x[i] - 0.002*x[i]*y[i] ) * dt
    y[i+1] = y[i] + (0.0025*x[i]*y[i] - 0.2*y[i]) * dt

#draw and save figure
plt.subplots(1, figsize=(8,6))
plt.plot(t, x, 'r-')
plt.plot(t, y, 'b-.')
plt.xlim([0, 100])
plt.ylim([0, 500])
plt.title(r'$X_0$=%d, $Y_0$=%d' %(x0, y0))
plt.legend(['X', 'Y'])
plt.savefig('mida_%04d_%04d.png' %(x0, y0), bbox_inches='tight', dpi=100)
"""
"""