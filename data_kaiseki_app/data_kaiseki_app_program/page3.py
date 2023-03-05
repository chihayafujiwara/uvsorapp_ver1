import streamlit as st
import pandas as pd
from ple import glob
from ple import counter
from ple import sp
from ple import spplot


def page3(genre,df5,wb,save_dir):
    st.write('----------------------------------')
    col1, col2, col3 = st.columns([1, 1, 1])
    col1.write('Choose plot type')

    with col1.expander("Plot settig"):
        sele = st.select_slider("Spectrum type:", ["Emission", "Excitation"])
        sel = st.select_slider("Select:", ["Absolute","Normalized"])
        noise = st.select_slider("Hample filter:", ["With", "Without"])
        
    col2.write('Choose plot temprate')    
    with col2.expander('User temprate'):
        path_list, name_list = glob.filesearch('data_kaiseki_app/data_control//fig_para')
        d_name = st.selectbox('Figure type',(name_list))
        dff = counter.counter_para1(d_name)   
    st.write('----------------------------------')
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    if sele == "Emission":
        ex_ = col1.number_input('Excitation wavelength [nm]',value=300)
        ex = int(ex_)
        
        with col1.expander("Emission spectra"):
            color1 = st.color_picker('Pick Fig1 Color', dff[1][0])
            xaxis1 = st.text_input('X axis name1',value=str(dff[1][2]))
            yaxis1 = st.text_input('Y axis name1',value=str(dff[1][4]))
            fig_size_w1 = st.slider('Figure Size 縦1',min_value = 1,max_value =10,value = int(dff[1][6]))
            fig_size_h1 = st.slider('Figure Size 横1',min_value = 1,max_value =10,value = int(dff[1][8]))
            fs1 = st.slider('Font Size1 ',min_value = 1,max_value =20,value = int(dff[1][10]))
            options1 = st.multiselect('Plot type1',['Line', 'scatter'],['Line'])
            lw1 = st.slider('Line width1',min_value = 1,max_value =10,value = 2)
        
        with col1.expander("Excitation spectra"):
            color2 = st.color_picker('Pick Fig2 Color', dff[1][1])
            xaxis2 = st.text_input('X axis name2',value=str(dff[1][3]))
            yaxis2 = st.text_input('Y axis name2',value=str(dff[1][5]))
            fig_size_w2 = st.slider('Figure Size 縦2',min_value = 1,max_value =10,value = int(dff[1][7]))
            fig_size_h2 = st.slider('Figure Size 横2',min_value = 1,max_value =10,value = int(dff[1][9]))
            fs2 = st.slider('Font Size2 ',min_value = 1,max_value =20,value = int(dff[1][11]))
            options2 = st.multiselect('Plot type2',['Line', 'scatter'],['Line'])
            lw2 = st.slider('Line width2',min_value = 1,max_value =10,value = 2)
        
        inte = df5[ex][1:]
        em = df5['em'][1:]            
        em_inte = df5[ex][1:].max()                                
        
        min_em, max_em = col2.slider('Range of Emission wavelength',min_value=100,max_value=1200,value=(300,950))
        em_data = sp.spectrum_1(em,inte,em_inte,noise,sel,wb,min_em,max_em)            
        em_w = float(em_data[em_data['inte_em']==em_data['inte_em'].max()]['em'][0:1])          
        em_int = em_data['inte_em'].max()
        ex_int = df5[df5['em'] == em_w].T[1:]
        ex_w = df5[:1].T[1:][0]
        ex_data = pd.concat([ex_w,ex_int],axis=1)            
        min_ex, max_ex = col3.slider('Range of Exicitation wavelength',min_value=50,max_value=1300,value=(150,500))
        ex_data = sp.spectrum_2(ex_w,ex_int,ex_data,noise,sel,wb,min_ex,max_ex)

        data = pd.concat([em_data,ex_data],axis=1)
        
        fig1 = spplot.spectrum_plot1(data,color1,xaxis1,yaxis1,fig_size_w1,fig_size_h1,fs1,options1,lw1)
        fig2 = spplot.spectrum_plot2(data,color2,xaxis2,yaxis2,fig_size_w2,fig_size_h2,fs2,options2,lw2)
        fig3 = spplot.spectrum_plot3(data,color1,color2,xaxis2,yaxis2,fig_size_w2,fig_size_h2,fs2,options1,options2,lw1,lw2)
        
        col2.pyplot(fig1[0])
        col2.pyplot(fig3[0])
        col3.pyplot(fig2[0])
        
        dp = spplot.parameter(data)
        
        col3.write('Emission wavelength :' + str(dp[0]) + ' nm')
        col3.write('Intensity :' + str(dp[1]) + ' a.u.')
        col3.write('Excitation wavelength :' + str(dp[2]) + ' nm')
        col3.write('Intensity :'+ str(dp[3])+ ' a.u.')
        
        with col1.expander("Save"):
            name = st.text_input('Dataname')
            sv_opt = st.multiselect('Save type',['csv', 'Emission','Excitation','Both'],['csv'])
            if st.button('Save'):
                    if 'csv' in sv_opt:
                        data.to_csv(str(save_dir)+'\\'+str(name)+'_ex'+str(ex)+'.csv')
                    if 'Emission' in sv_opt:
                        fig1[0].savefig(str(save_dir)+'\\'+str(name)+'_ex'+str(ex)+'_emission_spectra.png',dpi =450)
                    if 'Excitation' in sv_opt:                      
                        fig2[0].savefig(str(save_dir)+'\\'+str(name)+'_em'+str(dp[0])+'_excitation_spectra.png',dpi =450)
                    if 'Both' in sv_opt:                      
                        fig3[0].savefig(str(save_dir)+'\\'+str(name)+'_ex'+str(ex)+'_both_spectrum.png',dpi =450)
        
    elif sele == "Excitation":   
        ex_ = col1.number_input('Emission wavelength [nm]',value=600)
        ex = int(ex_)
    
    
        with col1.expander("Excitation spectra"):
            color2 = st.color_picker('Pick Fig2 Color', dff[1][1])
            xaxis2 = st.text_input('X axis name2',value=str(dff[1][3]))
            yaxis2 = st.text_input('Y axis name2',value=str(dff[1][5]))
            fig_size_w2 = st.slider('Figure Size 縦2',min_value = 1,max_value =10,value = int(dff[1][7]))
            fig_size_h2 = st.slider('Figure Size 横2',min_value = 1,max_value =10,value = int(dff[1][9]))
            fs2 = st.slider('Font Size2 ',min_value = 1,max_value =20,value = int(dff[1][11]))
            options2 = st.multiselect('Plot type2',['Line', 'scatter'],['Line'])
            lw1 = st.slider('Line width1',min_value = 1,max_value =10,value = 2)
            
        with col1.expander("Emission spectra"):
            color1 = st.color_picker('Pick Fig1 Color', dff[1][0])
            xaxis1 = st.text_input('X axis name1',value=str(dff[1][2]))
            yaxis1 = st.text_input('Y axis name1',value=str(dff[1][4]))
            fig_size_w1 = st.slider('Figure Size 縦1',min_value = 1,max_value =10,value = int(dff[1][6]))
            fig_size_h1 = st.slider('Figure Size 横1',min_value = 1,max_value =10,value = int(dff[1][8]))
            fs1 = st.slider('Font Size1 ',min_value = 1,max_value =20,value = int(dff[1][10]))
            options1 = st.multiselect('Plot type1',['Line', 'scatter'],['Line'])
            lw2 = st.slider('Line width2',min_value = 1,max_value =10,value = 2)
                
        df7 = (df5['em'][1:]-ex).abs()
        ind = df7.index[df7 == df7.min()][0]
        ex_data = df5[ind:ind+1].T[1:].reset_index()
        ex_data.columns=['ex','inte_ex']
        
        
        min_ex, max_ex = col2.slider('Range of Exicitation wavelength',min_value=50,max_value=800,value=(150,500))
        
        ex_data = sp.spectrum_3(ex_data,noise,sel,wb,min_ex,max_ex)
        ex_w = ex_data[ex_data['inte_ex'] == ex_data['inte_ex'].max()]['ex'].iloc[0]  
        ex_data.columns=['ex','inte_ex']
        
        
        inte = df5[ex_w][1:]
        em = df5['em'][1:]    
        min_em, max_em = col3.slider('Range of Emission wavelength',min_value=100,max_value=1200,value=(300,950))            
        
        
        em_data = sp.spectrum_4(inte,em,noise,sel,wb,min_em,max_em)
        data = pd.concat([em_data,ex_data],axis=1)

        fig1 = spplot.spectrum_plot1(data,color1,xaxis1,yaxis1,fig_size_w1,fig_size_h1,fs1,options1,lw1)
        fig2 = spplot.spectrum_plot2(data,color2,xaxis2,yaxis2,fig_size_w2,fig_size_h2,fs2,options2,lw2) 
        fig3 = spplot.spectrum_plot3(data,color1,color2,xaxis2,yaxis2,fig_size_w2,fig_size_h2,fs2,options1,options2,lw1,lw2)
                
        col2.pyplot(fig2[0])
        col2.pyplot(fig3[0])
        col3.pyplot(fig1[0])

        dp = spplot.parameter(data)
        
        col3.write('Excitation wavelength :' + str(dp[0]) + ' nm')
        col3.write('Intensity :' + str(dp[1]) + ' a.u.')
        col3.write('Emission wavelength :' + str(dp[2]) + ' nm')
        col3.write('Intensity :'+ str(dp[3])+ ' a.u.')

        with col1.expander("Save"):
            name = st.text_input('Dataname')
            sv_opt = st.multiselect('Save type',['csv', 'Emission','Excitation','Both'],['csv'])
            if st.button('Save'):
                    if 'csv' in sv_opt:
                        data.to_csv(str(save_dir)+'\\'+str(name)+'_em'+str(ex)+'.csv')
                    if 'Emission' in sv_opt:
                        fig1[0].savefig(str(save_dir)+'\\'+str(name)+'_em'+str(ex)+'_emission_spectra.png',dpi =450)
                    if 'Excitation' in sv_opt:                      
                        fig2[0].savefig(str(save_dir)+'\\'+str(name)+'_ex'+str(dp[2])+'_excitation_spectra.png',dpi =450)
                    if 'Both' in sv_opt:                      
                        fig3[0].savefig(str(save_dir)+'\\'+str(name)+'_ex'+str(ex)+'_both_spectrum.png',dpi =450)
    
    with col1.expander('User temprate save'):
        name_temp = st.text_input('Temprate name')
        if st.button('図をテンプレートとして保存'):
            dff[1][0] = color1
            dff[1][1] = color2
            dff[1][2] = xaxis1
            dff[1][3] = xaxis2
            dff[1][4] = yaxis1
            dff[1][5] = yaxis2
            dff[1][6] = int(fig_size_w1)
            dff[1][7] = int(fig_size_w2)
            dff[1][8] = int(fig_size_h1)
            dff[1][9] = int(fig_size_h1)
            dff[1][10] = int(fs1)
            dff[1][11] = int(fs2)
            dff.to_csv('data_kaiseki_app/data_control//fig_para//'+str(name_temp)+'.csv', index=False)
