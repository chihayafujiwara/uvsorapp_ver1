import pandas as pd
import streamlit as st
import os
import numpy as np

#users = os.path.join(os.path.join(os.environ['USERPROFILE']),'UVSOR_app\\data_kaiseki_app')

@st.cache(suppress_st_warning=True)
def calc(uploaded_file,fir,step):
    
    df1 = pd.read_table(uploaded_file,sep='\s+',names=['em','inte'])
    
    df2 = {'ex':[(x//1340)*step + fir for x in range(int(len(df1)))]}


    frame1 = pd.DataFrame(df1)
    frame2 = pd.DataFrame(df2)
    data = frame2.join(frame1)
    df = data.pivot(index = 'em', columns = 'ex', values = 'inte').reset_index()
    
    df3 = pd.read_table('data_kaiseki_app/data_control/hoseiuvsor.csv',sep=',')

    set = [i*step + fir for i in range(int(len(df1)/1340))]
    
    a = [0] + set
    data = pd.DataFrame(a)
    df4 = pd.DataFrame(data.T)
    df4.columns = ['em'] + set
    df5 = pd.concat([df4,df],axis = 'index')
    df5 = pd.DataFrame(df5.T)
    df5.columns = [i for i in range(1341)]

    for i in range(1,1341):
        num = df5[i]['em']
        index = df3.index[(df3['nm'] - num).abs().argsort()][0].tolist()
        df7 = df3.at[index,'発光']
        df5[i][1:] = df5[i][1:]/df7
    df5 = df5.T

    for j in np.arange(int(fir),int(len(df1)/1340)-1 + int(fir),step):
        index = df3.index[(df3['nm.1'] - j).abs().argsort()][0].tolist()
        df9 = df3.at[index,'励起光']
        df5[j][1:] = df5[j][1:]/df9
    
    df5 = df5.where(df5 > 0, 0)
    return(df5)
