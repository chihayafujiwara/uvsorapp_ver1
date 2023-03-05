import streamlit as st
import subprocess
from ple import glob
from ple import counter
from ple import precalc
from ple import plot
import pandas as pd
from ple import gf
from ple import gfplot

def page4(genre,df5,wb,save_dir):
    st.write('----------------------------------')
    col1, col2, col3 = st.columns([1, 1, 1])
    col3.write('パラメータエクセルファイル')
    
    if col3.button('パラメータ入力ファイル open'):
        EXCEL = 'data_kaiseki_app/data_control/fittpara.csv'
        subprocess.Popen(['start',EXCEL], shell=True)

    col2.write('Choose the setting')

    with col2.expander("Settig"):
        sele = st.select_slider("出力形式:", ["選択data 出力", "全data 出力"])
        nosie_can2 = st.select_slider("Hample filter:", ["With", "Without"])
        name = st.text_input('dataname')

    col1.write('Choose the data setting')        
    with col1.expander("Gaussian fit setting"):
        st.write('ガウシアンフィットを行います。各種parameterを入れてください。')
        st.write('y = base + Σ (ai * exp((x-bi)^2/ci^2) )')
        r = round(st.number_input('ガウシアンフィットR^2閾値',value =round(0.99,5)),5)
        st.write('The current number is',r)
    
        ex_ = st.number_input('励起波長 [nm]',value=300)
        
    st.write('----------------------------------')
    col1, col2, col3 = st.columns([1, 1, 1])
    min_em, max_em = col1.slider('fitting範囲',min_value=0.1,max_value=5.0,value=(1240/950,1240/300))

    ex = int(ex_)
    data = precalc.calc_4(df5,ex)
    data = precalc.cut(data[0],min_em,max_em)
    predata = precalc.calc_3(data,nosie_can2,wb)
    
    x = predata[0]
    y = predata[1]
    m = predata[2]

    
    fig1 = plot.plot(x,y)
    col1.write('Raw data')
    col1.pyplot(fig1[0])

    # 条件を満たないときは処理を停止する
    if col1.button('Run gaussian fit'):   
        ex = int(ex_)
        df = pd.read_csv('data_kaiseki_app/data_control/fittpara.csv',encoding="shift-jis")[0:11]
        data = gf.gaussian(df,x,y,m)
        csv = gfplot.g_plot(data[0],data[1],data[2],data[4])

        
        col2.write('Fitting 1')
        col2.pyplot(csv[0])
        col2.write('Fitting 2')
        col2.pyplot(csv[1])
        col2.write('Fitting 3')
        col2.pyplot(csv[2])
        col3.write('R^2 result')
        col3.pyplot(csv[3])
        col3.write('Fitting parameter')
        col3.dataframe(data[3])
    
    if sele == "選択data 出力":     
        for i in range(0,3,1):
            
            if data[3]['R^2'][i] >= r:
                col3.write('Fitting Result')
                col3.write('The number of gaussian component = '+str(i+1))
                data_para = data[3][i:i+1]
                data_raw = data[i]
                data_para.to_csv(str(save_dir)+'\\'+str(name)+'_ex'+str(ex_)+'_fitting_'+str(i+1)+'_parameter.csv')
                data_raw.to_csv(str(save_dir)+'\\'+str(name)+'_ex'+str(ex_)+'_fitting_'+str(i+1)+'.csv')
                break
    else:
        for i in range(0,3,1):
            data_para = data[3][i:i+1]
            data_raw = data[i]
            data_para.to_csv(str(save_dir)+'\\'+str(name)+'_ex'+str(ex_)+'_fitting_'+str(i+1)+'_parameter.csv')
            data_raw.to_csv(str(save_dir)+'\\'+str(name)+'_ex'+str(ex_)+'_fitting_'+str(i+1)+'.csv')