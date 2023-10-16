import math              as m 
import numpy             as np
import matplotlib.pyplot as plt
"""
"""
#define a function to calculate temperature in each layer
def func(ea, eb, a):
    S0 = 1361.0

    eTOA= S0/4 *(1-a)

    eTs = eTOA * ( (4-(ea*eb)) / ((2-ea)*(2-eb)) )
    Ts  = (eTs/(5.678E-8))**0.25

    eTa = eTs * ( (2-eb) / (4-ea*eb) )
    Ta  = (eTa/(5.678E-8))**0.25

    eTb = eTs * ( (2+ea-ea*eb) / (4-ea*eb) )
    Tb  = (eTb/(5.678E-8))**0.25

    return(Ta, Tb, Ts)
"""
"""