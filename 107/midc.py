import numpy             as np
import matplotlib.pyplot as plt

Ps, H, Ts, RHs = np.loadtxt('midc_input.txt', dtype=float, comments=None, skiprows=1, unpack='true')

f, ax = plt.subplots(1, 2, sharey='row')

ax[0] . plot(Ts, Ps, 'k-o')
ax[0] . set_xlim(-5,30)
ax[0] . set_ylim(1013,500)
ax[0] . set_xlabel(r'Temperature ($^o$C)', size = 14)
ax[0] . set_ylabel(r'Pressure (hPa)', size = 14)
#
ax[1] . plot(RHs, Ps, 'b--')
ax[1] . set_xlim(30,100)
ax[1] . set_xlabel(r'RH (%)', size = 14)

plt.savefig('midc.png', dpi = 300)
plt.show()
