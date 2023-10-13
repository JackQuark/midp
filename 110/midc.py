import numpy             as np
import matplotlib.pyplot as plt
import RET               as RET

So = np.arange(1300, 1401, 2)
ap = np.arange(0.1, 0.91, 0.02)

So, ap = np.meshgrid(np.arange(1300, 1401, 2), np.arange(0.1, 0.91, 0.02))
Te = RET.Myfun_Te(So, ap)

plt.title('Radiative Equilibrium Temperature')
plt.xlabel(r'$S_\odot$(Wm$^-$$^2$)')
plt.ylabel(r'$\alpha_p$')
r = np.arange(150, 276, 5)
plt.plot(1361, 0.3, 'ko')
plt.text(1361, 0.25, 'Earth')
CS = plt.contourf(So, ap, Te, levels = r, cmap = 'inferno')
CS.set_cticks = r
plt.colorbar(CS,orientation='vertical')
plt.savefig("midc.png", dpi=300)