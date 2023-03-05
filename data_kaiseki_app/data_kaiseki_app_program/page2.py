import streamlit as st
from ple import glob
from ple import counter
from ple import map
import matplotlib.pyplot as plt


def page2(genre,X,Y,p2,save_dir):
    st.write('----------------------------------')
    col1, col2 ,col3  = st.columns([5,2,2])

    with col2.expander('User temprate'):
        path_list, name_list = glob.filesearch('data_kaiseki_app/data_control//2dmap_para')
        d_name = st.selectbox('Figure type',(name_list))
        dff = counter.counter_para(d_name)

    with col2.expander("Plot settig"):
        fig_color = st.selectbox('Figure Design',('viridis','jet','gray','ocean','plasma'))
        xaxis = st.text_input('X axis name',value=str(dff[1][9]))
        yaxis = st.text_input('Y axis name',value=str(dff[1][10]))
        fs = st.slider('Font Size ',min_value = 1,max_value =20,value = int(dff[1][0]))
        fig_size_w = st.slider('Figure Size 縦',min_value = 1,max_value =10,value = int(dff[1][2]))
        fig_size_h = st.slider('Figure Size 横',min_value = 1,max_value =20,value = int(dff[1][1]))

    with col3.expander("Axis setting"):
        min_inte = 0
        max_inte = st.number_input('2DMAP図強度調整',value = float(100))
        bins = st.slider('ビン',0,30,int(dff[1][7]))
        min_ex = st.number_input('Ex min',value=(int(dff[1][5]))) 
        max_ex = st.number_input('Ex max',value=(int(dff[1][6]))) 
        min_em = st.number_input('Em min',value=(int(dff[1][3])))    
        max_em = st.number_input('Em max',value=int(dff[1][4]))    
        
    with col3.expander('User temprate save'):
        name_temp = st.text_input('Temprate name')
        if st.button('図をテンプレートとして保存'):
            dff[1][0] = fs
            dff[1][1] = fig_size_h
            dff[1][2] = fig_size_w
            dff[1][3] = min_em
            dff[1][4] = max_em
            dff[1][5] = min_ex
            dff[1][6] = max_ex
            dff[1][7] = bins
            dff[1][9] = xaxis
            dff[1][10] = yaxis
            dff.to_csv('data_kaiseki_app/data_control/2dmap_para/'+str(name_temp)+'.csv', index=False)

    
    with col2.expander("File setting"):
        name_counter = st.text_input('ファイル名','image')
        extention = st.selectbox('拡張子',('png','jpg','tif'))
            

    col1.write('2DMAP(Emission vs Excitation)')
    fig = map.counter(fig_size_h,fig_size_w,min_em,max_em,min_ex,max_ex,min_inte,max_inte,bins,fs,fig_color,xaxis,yaxis,X,Y,p2)
        
    col1.pyplot(fig)
        
    if col3.button('Download image'):    
        plt.savefig(str(save_dir)+'\\'+str(name_counter)+'.'+str(extention),dpi=450,transparent=True)
