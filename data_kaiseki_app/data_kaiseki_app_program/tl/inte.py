from scipy import integrate
import numpy as np
import pandas as pd
from tl import hp

def inte(k,thr,df1,i):
    df2 = df1[df1['Frame'] == i]
    x = df2['Wavelength']
    y = df2['Intensity']
    # pandasデータフレームをnpに変換
    y = np.array(y)
    y_h = hp.Hampel(y,k,thr)

        #除去無し
    y_int_Simps_r = integrate.simps(y, x)
    y_int_Simps = integrate.simps(y_h, x)
    
    return([i,y_int_Simps,y_int_Simps_r])
