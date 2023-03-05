import pandas as pd
import numpy as np
from ple import hp
import streamlit as st

@st.cache(suppress_st_warning=True)
def spectrum_1(em,inte,em_inte,noise,sel,wb,min_em,max_em):
    if noise == 'With':
        inte = np.array(inte)
        inte = hp.Hample(inte,wb['k'].iloc[0],thr=wb['thr'].iloc[0])
        inte = pd.DataFrame(inte)[0]
    
    if sel == "Normalized":
        em_data = pd.concat([em,inte/em_int],axis=1)            
    elif sel == "Absolute":
        em_data = pd.concat([em,inte],axis=1)  
                
    em_data.columns = 'em','inte_em'        
    em_data = em_data[em_data['em']<max_em]
    em_data = em_data[em_data['em']>min_em]  
    em_data = em_data.reset_index(drop=True)
    return(em_data)

@st.cache(suppress_st_warning=True)
def spectrum_2(ex_w,ex_int,ex_data,noise,sel,wb,min_ex,max_ex):    
    if sel == "Normalized":
        ex_data = pd.concat([ex_w,ex_int/ex_int.max()],axis=1)            
    elif sel == "Absolute":
        ex_data = pd.concat([ex_w,ex_int],axis=1)
    
    ex_data.columns = 'ex','inte_ex'
    ex_data = ex_data[ex_data['ex']< max_ex]
    ex_data = ex_data[ex_data['ex']> min_ex]
    ex_data = ex_data.reset_index(drop=True)           
    return(ex_data)

@st.cache(suppress_st_warning=True)
def spectrum_3(ex_data,noise,sel,wb,min_ex,max_ex):

    ex_data = ex_data[ex_data['ex']<max_ex]
    ex_data = ex_data[ex_data['ex']>min_ex]         
    
    if sel == "Normalized":
        ex_data['inte_ex'] = ex_data['inte_ex']/ex_data['inte_ex'].max()
        
    elif sel == "Absolute":
        ex_data=ex_data        
        
    ex_data.columns= 'ex','inte_ex'
    ex_data = ex_data.reset_index(drop=True)
    return(ex_data)

@st.cache(suppress_st_warning=True)
def spectrum_4(inte,em,noise,sel,wb,min_em,max_em):            
    if noise == 'With':
        inte = np.array(inte)
        inte = hp.Hample(inte,wb['k'].iloc[0],thr=wb['thr'].iloc[0])
        inte = pd.DataFrame(inte)[0]            

    if sel == "Normalized":
        em_data = pd.concat([em,inte/em_int],axis=1)            
    elif sel == "Absolute":
        em_data = pd.concat([em,inte],axis=1)        
    em_data.columns = 'em','inte_em'
    em_data = em_data[em_data['em']<max_em]
    em_data = em_data[em_data['em']>min_em]

    em_data = em_data.reset_index(drop=True)
    return(em_data)