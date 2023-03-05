import pandas as pd
import numpy as np
from ple import hp
import streamlit as st

@st.cache
def calc_4(df5,ex):
    data = pd.concat([1240/df5['em'][1:],df5[ex][1:]],axis = 1)
    return([data]) 

@st.cache
def cut(data,min_em,max_em):
    data = data[data['em']> min_em]
    data = data[data['em']< max_em]
    return(data)    

@st.cache
def calc_3(data,nosie_can2,wb):
    y = data.iloc[:,1]
    x = data.iloc[:,0]
    x = x.reset_index(drop = True)
    y = y.reset_index(drop = True)
    
    if nosie_can2 == 'With':
        y = np.array(y)
        y = hp.Hample(y,wb['k'].iloc[0],thr=wb['thr'].iloc[0])
        y = pd.DataFrame(y)[0]
    
    m = y.max()
    return([x,y,m])