import numpy             as np
def getLWP(Th1, q1):
    P0, Rd, Cp, Lv, Rv = 1000, 287, 1004, 2.5E6, 461

    P  = np.arange(700,1001,1)
    Th = np.append(np.linspace(300,300,150),np.linspace(Th1,Th1,151))
    q  = np.append(np.linspace(0.001,0.001,150),np.linspace(q1,q1,151))

    T  = Th * (P/P0)**(Rd/Cp)
    es = 6.11 * np.exp( (Lv/Rv)*((1/273) - (1/T)) )
    qs = 0.6226 * es / (P-es)
    RH = q/qs
    e  = q * P / 0.6226

    icloud = np.argwhere(RH > 1)
    icb = np.max(icloud)
    ict = np.min(icloud)
    LWP = (100/9.8) * (np.trapz(q[ict:icb+1]-qs[ict:icb+1], P[ict:icb+1], 1, axis = 0))
    
    return(LWP)    