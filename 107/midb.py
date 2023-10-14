import numpy             as np
import matplotlib.pyplot as plt
import math              as m

n = np.loadtxt('midb_input.txt')
n = np.delete(n, np.where(n<0))
Sn= np.ones(len(n))

for j in range(len(n)):
    
    for i in range(int(n[j])):
        
        Sn[j] += 1/m.factorial(i+1)

error = abs(Sn - m.e)
data = np.column_stack((n, Sn, error))
np.savetxt('midb.txt', data, fmt='%3d %9.6f %9.2e', header='n        Sn     error')

plt.plot(n, error, 'bo')
plt.xscale('log')
plt.yscale('log')
plt.xlim([1, 50])
plt.xticks([2,4,8,16,32],['2','4','8','16','32'])
plt.xlabel('n', fontsize = 14)
plt.ylabel('error', fontsize = 14)
plt.show()
