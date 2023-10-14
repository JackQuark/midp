import numpy             as np
import matplotlib.pyplot as plt
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

f, ax = plt.subplots(2, 2, sharey = 'row')
#
ax[0,0] . set_title('temperature (K)')
ax[0,0] . set_ylabel('P(hPa)')
ax[0,0] . set_xlim(260, 320)
ax[0,0] . set_ylim(1000, 700)
ax[0,0] . set_xticks(np.linspace(260, 320, 4))
ax[0,0] . plot(Th, P, 'g--')
ax[0,0] . plot( T, P, 'r:')
ax[0,0] . legend([r'$\theta$', r'$T$'])
#
ax[0,1] . set_title('mixing ratio (kg/kg)')
ax[0,1] . set_xlabel('[g/kg]')
ax[0,1] . set_xlim(0, 0.020)
ax[0,1] . set_xticks(np.linspace(0, 0.020, 5))
ax[0,1] . plot(q, P, 'g--')
ax[0,1] . plot(qs, P, 'r:')
ax[0,1] . legend([r'$q$', r'$q_s$'])
#
ax[1,0] . set_ylabel('P(hPa)')
ax[1,0] . set_ylim(1000, 700)
ax[1,0] . set_xlabel('vapor pressure (hPa)')
ax[1,0] . set_xlim(0, 30)
ax[1,0] . set_xticks(np.linspace(0, 30, 4))
ax[1,0] . plot(e, P, 'g--')
ax[1,0] . plot(es, P, 'r:')
ax[1,0] . legend([r'$e$', r'$e_s$'])
#
ax[1,1] . set_xlabel('relative humidity')
ax[1,1] . set_xlim(0, 2.0)
ax[1,1] . set_xticks(np.linspace(0, 2.0, 5))
ax[1,1] . plot(RH, P, 'r-')
ax[1,1] . plot([1,1], [1000, 700], 'k:')

plt.savefig('mida.png', dpi = 300)