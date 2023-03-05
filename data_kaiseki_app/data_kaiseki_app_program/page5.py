import streamlit as st
import numpy as np
import pandas as pd
from tl import sp
from tl import hp
from tl import plot

def page5(uploaded_file):
    st.write('----------------------------------')
    col1, col2 ,col3  = st.columns([1,2,2])
    
    i = int(col1.number_input('Insert a frame number',value = 1))
    
    df1 = sp.sp(uploaded_file)
    
    df2 = sp.sp1(df1,i)
    
    with col1.expander('Hample filter parameter'):
        k = st.number_input('Fitler size',value=4)
        thr = st.number_input('Threshold', value=3)
        
    x = df2['Wavelength']
    y = df2['Intensity']
    y_ = np.array(y)
    y_h = hp.Hampel(y_,k,thr)
    y_h = pd.DataFrame(y_h)[0]
    
    fig1 = plot.plot(x,y)
    fig2 = plot.plot(x,y_h)
    
    col2.subheader('Filter 無し')
    col3.subheader('Filter あり')
    col2.pyplot(fig1)
    col3.pyplot(fig2)
    
    
        
    
