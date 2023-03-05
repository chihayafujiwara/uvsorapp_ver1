import matplotlib.pyplot as plt
import streamlit as st
from ple import round


def spectrum_plot1(data_all,color1,xaxis,yaxis,h,w,fs1,options1,lw):        
    fig1 = plt.figure(figsize=(h,w))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ax1 = fig1.add_subplot(1,1,1)
    
    if 'Line' in options1:
        ax1.plot(data_all['em'],data_all['inte_em'],c=color1,lw=lw)
    if 'scatter' in options1:
        ax1.scatter(data_all['em'],data_all['inte_em'],c=color1)
    
    ax1.set_xlabel(str(xaxis),fontsize = fs1)
    ax1.set_ylabel(str(yaxis),fontsize = fs1)
    ax1.grid()
    return([fig1])

def spectrum_plot2(data_all,color2,xaixs,yaxis,h,w,fs2,options2,lw):        
    fig2 = plt.figure(figsize=(h,w))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ax2 = fig2.add_subplot(1,1,1)
            
    if 'Line' in options2:
        ax2.plot(data_all['ex'],data_all['inte_ex'],c=color2,lw=lw)
    if 'scatter' in options2:
        ax2.scatter(data_all['ex'],data_all['inte_ex'],c=color2)
    
    ax2.set_xlabel(str(xaixs),fontsize = fs2)
    ax2.set_ylabel(str(yaxis),fontsize = fs2)
    ax2.grid()
    return([fig2])

def spectrum_plot3(data_all,color1,color2,xaixs,yaxis,h,w,fs2,options1,options2,lw1,lw2):        
    fig3 = plt.figure(figsize=(h,w))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ax1 = fig3.add_subplot(1,1,1)
    
    if 'Line' in options1:
        ax1.plot(data_all['em'],data_all['inte_em'],c=color1,lw=lw1)
    if 'scatter' in options1:
        ax1.scatter(data_all['em'],data_all['inte_em'],c=color1)

    
    if 'Line' in options2:
        ax1.plot(data_all['ex'],data_all['inte_ex'],c=color2,lw=lw2)
    if 'scatter' in options2:
        ax1.scatter(data_all['ex'],data_all['inte_ex'],c=color2)

    ax1.set_xlabel(str(xaixs),fontsize = fs2)
    ax1.set_ylabel(str(yaxis),fontsize = fs2)
    ax1.grid()
    return([fig3])

def parameter(data_all):
    em_center = data_all[data_all['inte_em'] == data_all['inte_em'].max()]['em'].iloc[0]
    em_inte = data_all['inte_em'].max()
    ex_center = data_all[data_all['inte_ex'] == data_all['inte_ex'].max()]['ex'].iloc[0]
    ex_inte = data_all['inte_ex'].max()
    return([round.round_it(em_center,3),round.round_it(em_inte,3),round.round_it(ex_center,3),round.round_it(ex_inte,3)])