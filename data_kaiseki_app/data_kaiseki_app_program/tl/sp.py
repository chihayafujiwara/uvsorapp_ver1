import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

@st.cache
def sp(uploaded_file):
    df1 = pd.read_csv(uploaded_file,sep=',')
    return(df1)

def sp1(df1,i):    
    df2 = df1[df1['Frame'] == i]
    return(df2)

    
    

