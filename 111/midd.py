import numpy             as np
import matplotlib.pyplot as plt
import matplotlib.cm     as cm
import func              as f

theta, P = np.meshgrid(np.arange(275,  311,  1), np.arange(850, 1051, 10))
es       = f.func_SAT(theta, P)

plt.title( r'$e_s$ (hPa)' )
plt.xticks(np.arange(275,  311,  5))
plt.yticks(np.arange(850, 1051, 50))
plt.xlabel(r'$\theta$ (K)')
plt.ylabel('P (hPa)')
CS=plt.contour(theta, P, es, levels = np.linspace(5, 55, 11), cmap = plt.cm.hsv)
plt.clabel(CS, inline=1, fontsize=12, fmt = '%5.3f')
plt.savefig("midd.png", dpi=300)
