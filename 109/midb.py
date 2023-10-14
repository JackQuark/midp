import numpy             as np
"""

"""
P0, Rd, Cp, Lv, Rv = 1000, 287, 1004, 2.5E6, 461

P  = np.arange(700,1001,1)
Th = np.append(np.linspace(300,300,150),np.linspace(290,290,151))
q  = np.append(np.linspace(0.001,0.001,150),np.linspace(0.01,0.01,151))

T  = Th * (P/P0)**(Rd/Cp)
es = 6.11 * np.exp( (Lv/Rv)*((1/273) - (1/T)) )
qs = 0.6226 * es / (P-es)
RH = q/qs
e  = q * P / 0.6226

icloud = np.argwhere(RH > 1)
icb = np.max(icloud)
ict = np.min(icloud)
LWP = (100/9.8) * (np.trapz(q[ict:icb+1]-qs[ict:icb+1], P[ict:icb+1], 1, axis = 0))
print('Pcb (hPa)= %6.2f' %(P[icb]))
print('Pct (hPa)= %6.2f' %(P[ict]))
print('LWP (kg/m2)= %3.2f' %(LWP))

data = np.column_stack((P, Th, q, RH))
np.savetxt('midb.txt', data, fmt='%8.1f %8.1f %8.3f %8.3f', header=' P(hPa)''   Th(K)''    q(kg/kg)'' RH')