import numpy as np
def cal_cf(Ps, RHs):
    
    CF = (30 + 185 * (1 - Ps/1000)) * np.exp( (RHs-100)/20 )

    return(CF)