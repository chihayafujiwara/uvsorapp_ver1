import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

import page1
import page2
import page3
import page4

from ple import uvsor1
from ple import uvsor2



def aple(save_dir):
    col1, col2, col3 = st.columns([1,2, 1])
    image = Image.open('../data_control/image.png')
    (width, height) = (image.width // 2, image.height // 2)
            # 画像をリサイズする
    img_resized = image.resize((width, height))
    col2.image(image)
    

    step = 0
    fir = 0
    ex_ = 0

    with st.sidebar.expander("RAW DATA"): 
        uploaded_file = st.file_uploader("Choose a file")
        fir_ = int(st.number_input('スタートの波長 [nm]'))
        step_ = float(st.number_input('スッテプ間隔 [nm]')) 

    if not uploaded_file:
        st.warning('Please input raw data')
        # 条件を満たないときは処理を停止する
        st.stop()
    if not fir_:
        st.warning('Please input Initial excitation wavelength[nm]')
        # 条件を満たないときは処理を停止する
        st.stop()
    if not step_:
        st.warning('Please input step [nm]')
        # 条件を満たないときは処理を停止する
        st.stop()
    
    genre = st.sidebar.selectbox(
        "Analysis type",
        ('Main page','2DMAP', 'Spectrum','Multi gaussian fit',))

    st.sidebar.write('------------------------------------------------')

    left_column,right_column = st.columns(2)

#ページ側の構成
    #--------------------------      
    fir = int(fir_)
    step = float(step_)
    df5= uvsor1.calc(uploaded_file,fir,step)
    database = uvsor2.calc_2(df5) 
    X = database[0]          
    Y = database[1]
    p2 = database[2]
    #dff = counter_para()
    wb = pd.read_table('../data_control/Hample.csv',sep=',')   
    #-------------------------- 

    if genre == 'Main page':
        page1.page1(genre)
        
    if genre == '2DMAP':
        page2.page2(genre,X,Y,p2,save_dir)

    if genre == 'Spectrum':
        page3.page3(genre,df5,wb,save_dir)
                 
    if genre == 'Multi gaussian fit':
        page4.page4(genre,df5,wb,save_dir)
