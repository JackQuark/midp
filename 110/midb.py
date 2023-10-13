import numpy             as np
import matplotlib.pyplot as plt

Po, Rd, Rv, E, Cp, Lv = 1000, 287, 461.5, 0.622, 1004, 2.5E6
T0, q0, H, g = 298, 0.015, 8500, 9.8
z     = np.linspace(0, 12000, 601)
Tp    = np.append( 298, np.zeros(600))
P     = np.append(1000, np.zeros(600))
Theta = np.empty(601)
qvsp  = np.empty(601)
n     = np.arange(600)

#calculate
P [1:]= P[0] * np.exp(-z[1:] / H)
Tp[1:]= T0 - (g * 20 / Cp) * (n+1)
Theta = Tp[:] * (1000/P[:]) ** (Rd/Cp)
es    = 6.11 * np.exp( (Lv/Rv)*((1/273.15) - (1/Tp)) )
qvsp  = E*es / ( P - (1-E)*es )

iqv   = np.where(q0 >= qvsp, qvsp, np.nan)
LCL   = np.nanargmax(iqv)

f, ax = plt.subplots(1, 3, sharey = 'row')
#
ax[0] . plot(Theta, z, 'g--')
ax[0] . plot(Tp, z, 'r:')
ax[0] . set_title('temperature')
ax[0] . set_xlabel('[K]')
ax[0] . set_ylabel('height [m]')
ax[0] . set_xlim(180, 300)
ax[0] . set_ylim(0, 12000)
ax[0] . set_xticks(np.linspace(180, 300, 5))
ax[0] . legend([r'$\theta_p$', r'$T_p$'])
#
ax[1] . plot( qvsp*1000, z, 'r')
ax[1] . plot([q0*1000, q0*1000], [0,12000], 'k:')
ax[1] . plot( q0*1000, z[LCL], 'bo')
ax[1] . set_title('mixing ratio')
ax[1] . set_xlabel('[g/kg]')
ax[1] . set_xlim(0, 20)
ax[1] . set_xticks(np.linspace(0, 20, 5))
ax[1] . legend([r'$q_vsp$', r'$q_0$', 'LCL'])
#
ax[2] . plot(P, z, 'k-')
ax[2] . set_title('pressure')
ax[2] . set_xlabel('[hPa]')
ax[2] . set_xlim(200, 1000)
ax[2] . set_xticks(np.linspace(200, 1000, 5))



