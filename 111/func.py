import numpy             as np

def func_SAT(theta, P):
    
    T = theta * (P/1000)**(287/1004)
    e = 6.11 * np.exp((2.5E6/461.0) * ((1/273)-(1/T)))
    
    return(e)