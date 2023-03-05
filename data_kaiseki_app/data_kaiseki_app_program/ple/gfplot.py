import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec

def g_plot(data1,data2,data3,r_matome):
    #色指定
    c1,c2,c3,c4,c5,c6 = "darkorange","black","red",'pink','blue','gold'

    fig1 = plt.figure(figsize=(6,4))
    fig2 = plt.figure(figsize=(6,4))
    fig3 = plt.figure(figsize=(6,4))
    fig4 = plt.figure(figsize=(6,4))

    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    #plt.subplots_adjust(hspace=0.5,wspace=0.5)

    spec = gridspec.GridSpec(ncols=1, nrows=2,
                        height_ratios=[3, 1])   

    
    #ax1 = fig1.add_subplot(2,1,1)
    ax1 = fig1.add_subplot(spec[0])
    ax5 = fig1.add_subplot(spec[1])
    #ax5 = fig1.add_subplot(2,1,2)
    ax2 = fig2.add_subplot(spec[0])
    ax6 = fig2.add_subplot(spec[1])
    #ax2 = fig2.add_subplot(1,1,1)
    ax3 = fig3.add_subplot(spec[0])
    ax7 = fig3.add_subplot(spec[1])  
    #ax3 = fig3.add_subplot(1,1,1)
    ax4 = fig4.add_subplot(1,1,1)


    fs = 12

    ax1.set_ylabel('Normalized \n Intensity [a.u.]',fontsize = fs,color=c2)
    #ax1.set_xlabel('Emission wavelength [nm]',fontsize = fs,color=c2)
    ax2.set_ylabel('Normalized \n Intensity [a.u.]',fontsize = fs,color=c2)
    #ax2.set_xlabel('Emission wavelength [nm]',fontsize = fs,color=c2)
    ax3.set_ylabel('Normalized \n Intensity [a.u.]',fontsize = fs,color=c2)
    #ax3.set_xlabel('Emission wavelength [nm]',fontsize = fs,color=c2)
    ax4.set_ylabel('R^2',fontsize = fs)
    ax4.set_xlabel('Number of Gaussian bands',fontsize = fs)
    ax5.set_xlabel('Energy [eV]',fontsize = fs,color=c2)
    ax5.set_ylabel('Residuals [%]',fontsize = fs,color=c2)
    ax6.set_xlabel('Energy [eV]',fontsize = fs,color=c2)
    ax6.set_ylabel('Residuals [%]',fontsize = fs,color=c2)
    ax7.set_xlabel('Energy [eV]',fontsize = fs,color=c2)
    ax7.set_ylabel('Residuals [%]',fontsize = fs,color=c2)


    ax1.tick_params(labelsize=fs,length=4, width=1,color=c2)    
    ax2.tick_params(labelsize=fs,length=4, width=1,color=c2)
    ax3.tick_params(labelsize=fs,length=4, width=1,color=c2)    
    ax5.tick_params(labelsize=fs,length=4, width=1,color=c2)
    ax6.tick_params(labelsize=fs,length=4, width=1,color=c2)  
    ax7.tick_params(labelsize=fs,length=4, width=1,color=c2)      
    #ax4.tick_params(labelsize=fs-10,length=1, width=1)

    sp = 1
    ax1.spines["top"].set_linewidth(sp)
    ax1.spines["left"].set_linewidth(sp)
    ax1.spines["bottom"].set_linewidth(sp)
    ax1.spines["right"].set_linewidth(sp)
    ax1.spines['top'].set_color(c2)
    ax1.spines['bottom'].set_color(c2)
    ax1.spines['left'].set_color(c2)
    ax1.spines['right'].set_color(c2)

    ax2.spines["top"].set_linewidth(sp)
    ax2.spines["left"].set_linewidth(sp)
    ax2.spines["bottom"].set_linewidth(sp)
    ax2.spines["right"].set_linewidth(sp)
    ax2.spines['top'].set_color(c2)
    ax2.spines['bottom'].set_color(c2)
    ax2.spines['left'].set_color(c2)
    ax2.spines['right'].set_color(c2)


    ax3.spines["top"].set_linewidth(sp)
    ax3.spines["left"].set_linewidth(sp)
    ax3.spines["bottom"].set_linewidth(sp)
    ax3.spines["right"].set_linewidth(sp)
    ax3.spines['top'].set_color(c2)
    ax3.spines['bottom'].set_color(c2)
    ax3.spines['left'].set_color(c2)
    ax3.spines['right'].set_color(c2)


    ax4.spines["top"].set_linewidth(sp)
    ax4.spines["left"].set_linewidth(sp)
    ax4.spines["bottom"].set_linewidth(sp)
    ax4.spines["right"].set_linewidth(sp)
    ax4.spines['top'].set_color(c2)
    ax4.spines['bottom'].set_color(c2)
    ax4.spines['left'].set_color(c2)
    ax4.spines['right'].set_color(c2)

    ax5.spines["top"].set_linewidth(sp)
    ax5.spines["left"].set_linewidth(sp)
    ax5.spines["bottom"].set_linewidth(sp)
    ax5.spines["right"].set_linewidth(sp)
    ax5.spines['top'].set_color(c2)
    ax5.spines['bottom'].set_color(c2)
    ax5.spines['left'].set_color(c2)
    ax5.spines['right'].set_color(c2)

    ax6.spines["top"].set_linewidth(sp)
    ax6.spines["left"].set_linewidth(sp)
    ax6.spines["bottom"].set_linewidth(sp)
    ax6.spines["right"].set_linewidth(sp)
    ax6.spines['top'].set_color(c2)
    ax6.spines['bottom'].set_color(c2)
    ax6.spines['left'].set_color(c2)
    ax6.spines['right'].set_color(c2)

    ax7.spines["top"].set_linewidth(sp)
    ax7.spines["left"].set_linewidth(sp)
    ax7.spines["bottom"].set_linewidth(sp)
    ax7.spines["right"].set_linewidth(sp)
    ax7.spines['top'].set_color(c2)
    ax7.spines['bottom'].set_color(c2)
    ax7.spines['left'].set_color(c2)
    ax7.spines['right'].set_color(c2)

    ax1.plot(data1['wave'],data1['Raw data'], c=c2 , lw = 2,label="Raw data")
    ax1.plot(data1['wave'],data1['fit sum'], c=c5, lw = 2,label="fit_sum")
    #ax1.plot(x,residuals1, c=c6, lw = 2,label="residual")

    ax2.plot(data2['wave'],data2['Raw data'], c=c2, lw =2,label="Raw data")
    ax2.plot(data2['wave'],data2['fit sum'],c=c5, lw =2,label="fit sum")
    ax2.plot(data2['wave'],data2['fit 1'], c=c1,lw =1,label="comp.1")
    ax2.plot(data2['wave'],data2['fit 2'], c=c3,lw=1,label="comp.2")
    #ax2.plot(x,residuals2, c=c6, lw = 2,label="residual")

    ax3.plot(data3['wave'],data3['Raw data'], c = c2, lw =2,label="Raw data")
    ax3.plot(data3['wave'],data3['fit sum'],c=c5, lw =2,label="fit sum")
    ax3.plot(data3['wave'],data3['fit 1'], c=c3,lw =1,label="comp.1")
    ax3.plot(data3['wave'],data3['fit 2'], c=c1,lw =1,label="comp.2")
    ax3.plot(data3['wave'],data3['fit 3'], c=c4,lw=1,label="comp.3")
    #ax3.plot(x,residuals3, c=c6, lw = 2,label="residual")


    #ax4.scatter(r_matome['comp'],r_matome['R^2'],linestyle='solid', s = 5 ,marker="o" , linewidths=2, ec=c2,c=c2)
    #ax4.plot(r_matome['comp'],r_matome['R^2'],linestyle='solid',c = c2)
    #ax4.set_xticks([0,1,2,3])
    ax4.bar(r_matome['comp'],r_matome['R^2'],align="center")

    ax5.plot(data1['wave'],data1['resi']) 
    ax6.plot(data2['wave'],data2['resi'])
    ax7.plot(data3['wave'],data3['resi'])

    ax1.legend(fontsize=10)
    ax2.legend(fontsize=10)
    ax3.legend(fontsize=10)

    ax1.grid()
    ax2.grid()
    ax3.grid()
    ax5.grid()
    ax6.grid()
    ax7.grid()
    
    ax4.set_xlim(-1,3)
    #ax5.set_ylim(-10,10)
    #ax6.set_ylim(-10,10)
    #ax7.set_ylim(-10,10)    

    fig1.subplots_adjust(wspace=0.4, hspace=0)
    fig2.subplots_adjust(wspace=0.4, hspace=0)
    fig3.subplots_adjust(wspace=0.4, hspace=0)
    
    return([fig1,fig2,fig3,fig4])