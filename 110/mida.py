nb, nt, t = 10, 4, 0

for i in range(nb+nt):
    if(i < nt):
        print('0'* (nt-1-i) + '1'* (2*i+1) + '0'* (nt-1-i))
        
        if(i == nt-3):t = i
        
    else:
        print('0'* (nt-1-t) + '1'* (2*t+1) + '0'* (nt-1-t))
