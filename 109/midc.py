import numpy             as np
import matplotlib.pyplot as plt
import cloud             as L
"""

"""
ThBL      = np.arange(285, 295, 1)
qBL       = np.arange(0.01, 0.0206, 0.0015)
LWP       = np.zeros((8, 10))
ThBL, qBL = np.meshgrid(ThBL, qBL)
for i in range(10):
    for j in range(8):
        LWP[j,i] = L.getLWP(ThBL[j,i], qBL[j,i])

plt.title('LWP (kg/$m^2$)')
plt.xlabel(r'$q_B$$_L$')
plt.ylabel(r'$\alpha_p$')

r  = np.linspace(0, 20, 11)
CS = plt.contourf(qBL, ThBL, LWP, levels = r, cmap = 'ocean')
CS.set_cticks = r
plt.colorbar(CS,orientation='vertical')
plt.savefig("midc.png", dpi=300)


