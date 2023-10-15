import numpy             as np
import math              as m

n, Sn  = round(float(input('n  :  '))), 1

for i in range(n):
    Sn += 1/m.factorial(i+1)
    
print('Sn = ',  Sn)
print('e  = ', m.e)
