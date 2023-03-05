import streamlit as st
import numpy as np
import pandas as pd
from tl import sp
from tl import hp
from tl import inte
from tl import plot2

def page6(uploaded_file,save_dir):
    st.write('----------------------------------')
    col1, col2 ,col3  = st.columns([1,2,2])
    df1 = sp.sp(uploaded_file)
    
    with col1.expander('Hample filter parameter'):
        k = st.number_input('Fitler size',value=4)
        thr = st.number_input('Threshold', value=3)
    
    name = col1.text_input('filename')
    # 条件を満たないときは処理を停止する
    
    if col1.button('Calculate'):  
        
        latest_iteration = st.empty()
        
        data_all =[]
        for i in range(1,int(len(df1)/1340)+1,1):
           data = inte.inte(k,thr,df1,i)
           data_all.append([data[0],data[1],data[2]])
           latest_iteration.text(f'time {i+1} / '+str(int(len(df1)/1340)+1))
           
        data_all = pd.DataFrame(data_all)
    
    fig1 = plot2.plot(data_all[0],data_all[1])
    fig2 = plot2.plot(data_all[0],data_all[2])
    
    col2.subheader('Filter 無し')
    col3.subheader('Filter あり')
    col2.pyplot(fig2)
    col3.pyplot(fig1)
    
    data_all.to_csv(str(save_dir)+'\\'+str(name)+'_TL.csv', index=False)
    return(data_all)