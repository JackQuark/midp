import numpy             as np
import matplotlib.pyplot as plt

prec = np.loadtxt('TCCIP_daily_precip_2018-2020.txt', dtype=float, comments=None, skiprows=1)
x1   = np.linspace(1, 1096, 1096)

sprec= np.sort(prec)
prec2= np.where(prec > sprec[-11] , prec , np.nan)

plt.title('TCCIP 2018-2020 precipitation time series', fontsize = 18)
xticks = np.linspace(0, 1100, 12)
yticks = np.linspace(0,  130, 14)
plt.xlim([-10, 1100])
plt.ylim([  0,  130])
plt.xlabel('Days', fontsize = 15)
plt.ylabel('Rainfall [mm/day]', fontsize = 15)
plt.xticks(xticks)
plt.yticks(yticks)
plt.plot(x1, prec, '-', linewidth = 1, color = 'dodgerblue')
plt.plot(x1, prec2, 'r*')
plt.savefig('midc1.png')
plt.show()

bins = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 130])
count= np.empty(11)
x3   = (bins[1:]+bins[:-1]) / 2

for i in range(10):
    times    = prec[(10*(i) <= prec) & (prec < 10*(i+1))]
    count[i] = len(times)
times    = prec[(100 <= prec) & (prec < 130)]
count[10] = len(times)

plt.title('TCCIP 2018-2020 precipitation distribution', fontsize = 18)
xticks = np.append(np.linspace(0, 100, 11), 130)
plt.xlim([  0,  130])
plt.xlabel('Rainfall [mm/day]', size = 15)
plt.ylabel('counts', size = 15)
plt.xticks(xticks)
plt.yscale('log')
plt.plot(x3, count, 'b-o')
plt.savefig('midc2.png')
plt.show()