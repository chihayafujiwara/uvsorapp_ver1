import matplotlib.pyplot as plt
import streamlit as st

def plot(x,y):
    fig1 = plt.figure(figsize=(3,3))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ax1 = fig1.add_subplot(1,1,1)
    ax1.set_xlabel('file number ',fontsize = 8)
    ax1.set_ylabel('Integrate value [a.u.]',fontsize = 8)
    ax1.grid()
    ax1.plot(x,y)
    return(fig1)    

