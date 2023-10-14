import numpy             as np
import matplotlib.pyplot as plt
import midd_f            as f

Ps, H, Ts, RHs = np.loadtxt('midc_input.txt', dtype=float, comments=None, skiprows=1, unpack='true')

P  = np.delete( Ps, np.where(Ps < 700))
RH = np.delete(RHs, np.argwhere(Ps < 700))
CF = f.cal_cf (P, RH)

P20  = np.delete( P, np.argwhere(CF <= 20))
CF20 = np.delete(CF, np.argwhere(CF <= 20))

plt.plot(CF, P, 'g-.')
plt.plot(CF20, P20, 'gd')
plt.plot(CF20[len(CF20)-1], min(P20), 'rd')
plt.xlim(5   , 40)
plt.ylim(1013,700)
plt.xlabel(r'CF (%)',         size = 14)
plt.ylabel(r'Pressure (hPa)', size = 14)
plt.legend(['CF','CF>20%','top of CF>20%'], fontsize=12)
plt.savefig('midd.png', dpi = 300)