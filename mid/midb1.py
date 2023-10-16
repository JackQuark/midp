import numpy             as np
import matplotlib.pyplot as plt
import midfunc           as f
"""
"""
#declare some required variables and array.
ea, eb  = np.linspace(0, 1, 100), np.linspace(0, 1, 100)
ae, be  = np.meshgrid(ea,eb)

Ta  = np.zeros((100, 100))
Tb  = np.zeros((100, 100))
Ts  = np.zeros((100, 100))

#calclate by defined function
Ta, Tb, Ts  = f.func(ae, be, 0.3)

#draw 3 figures
f, ax = plt.subplots(3, 1, figsize=(5,10), sharex = 'col', sharey = 'col')
r     = np.arange(210, 321, 10)

#figure 1
ax[0] . set_title('Ta [K]')
ax[0] . set_ylabel(r'$\epsilon_b$')
ax[0] . set_yticks(np.linspace(0.0, 1.0, 6))
ax[0] . set_xlim(0, 1)
ax[0] . set_ylim(0, 1)
CS1   = ax[0].contourf(ea, eb, Ta, levels = r, cmap = plt.cm.jet, extend = 'both')
cbar1 = plt.colorbar(CS1, ax=ax[0], orientation='vertical')

#figure 2
ax[1] . set_title('Tb [K]')
ax[1] . set_ylabel(r'$\epsilon_b$')
ax[1] . set_yticks(np.linspace(0.0, 1.0, 6))
ax[1] . set_xlim(0, 1)
ax[1] . set_ylim(0, 1)
CS2   = ax[1].contourf(ea, eb, Tb, levels = r, cmap = plt.cm.jet, extend = 'both')
cbar2 = plt.colorbar(CS2, ax=ax[1], orientation='vertical')

#figure 3
ax[2] . set_title('Ts [K]')
ax[2] . set_ylabel(r'$\epsilon_b$')
ax[2] . set_xlabel(r'$\epsilon_a$')
ax[2] . set_xticks(np.linspace(0.0, 1.0, 11))
ax[2] . set_yticks(np.linspace(0.0, 1.0, 6))
ax[2] . set_xlim(0, 1)
ax[2] . set_ylim(0, 1)
CS3   = ax[2].contourf(ea, eb, Ts, levels = r, cmap = plt.cm.jet, extend = 'both')
cbar3 = plt.colorbar(CS3, ax=ax[2], orientation='vertical')

#save figure
plt.savefig("midb1_emissivity.png", bbox_inches='tight', dpi=100)
"""
"""