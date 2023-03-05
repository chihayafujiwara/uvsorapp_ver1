import numpy as np
import streamlit as st

@st.cache(suppress_st_warning=True)
def calc_2(df5):    
    p2 = np.array(df5)
    yy,zz = [],[]
    y = p2[0,:]#全ての列の0行目を取得(10,11,,,5000)
    z = p2[:,0]#全ての行の0列目を取得(0,1,2,,,)
    y = y[1:]
    z = z[1:]

    for num in range(len(z)):
        yy.append(y)
    for num in range(len(y)):
        zz.append(z)

    X = np.array(yy)
    Y = np.array(zz).T

    p2 = np.delete(p2,0,1)
    p2 = np.delete(p2,0,0)

    return(X,Y,p2)