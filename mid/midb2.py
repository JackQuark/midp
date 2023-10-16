import numpy             as np
import matplotlib.pyplot as plt
import midfunc           as f
import netCDF4           as nc
import sys
"""
"""
#import selected month and year
mon     = int(sys.argv[2])
year    = int(sys.argv[1])

#loading the .nc file
rootgrp = nc.Dataset("albedo_2016_20.nc")
time    = rootgrp.variables['time'][:]
a       = rootgrp.variables['albedo'][:]
t       = (year - 2016) * 12 + mon - 1 

#calclate by defined function
Ta, Tb, Ts = f.func(0.7, 0.9, a[t])

#draw and save figure
plt.subplots(1, 1, figsize=(6,8))
plt.plot([Ts, Tb, Ta], [0, 1, 2], '-k.')
plt.xlim([220, 320])
plt.ylim([0, 2])
plt.yticks([0, 1, 2], ['Surface', 'Layer B', 'Layer A'])
plt.xlabel('[K]')
plt.title(('albedo=%7.5f / %4d.%02d' %(float(a[t]), year, mon)))
plt.savefig('midb2_%4d_%02d.png' %(year, mon), bbox_inches='tight', dpi=100)
"""
"""