nb, nt, t = 10, 4, 0

for i in range(nb+nt):
    if(i < nb):
        print('0'* (nb-1-i) + '1'* (2*i+1) + '0'* (nb-1-i))
        
        if(i == nb-3):t = i
        
    else:
        print('0'* (nb-1-t) + '1'* (2*t+1) + '0'* (nb-1-t))