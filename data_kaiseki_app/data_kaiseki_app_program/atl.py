import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from tl import sp
import page5
import page6

def atl(save_dir):
    col1, col2, col3 = st.columns([1,2, 1])
    image = Image.open('../data_control/image.png')
    (width, height) = (image.width // 2, image.height // 2)
            # 画像をリサイズする
    img_resized = image.resize((width, height))
    col2.image(image)

    with st.sidebar.expander("RAW DATA"): 
        uploaded_file = st.file_uploader("Choose a file")


    if not uploaded_file:
        st.warning('Please input raw data')
        # 条件を満たないときは処理を停止する
        st.stop()
    
    genre = st.sidebar.selectbox(
        "Analysis type",
        ('Main page','Spectrum','TL Analysis'))

    st.sidebar.write('------------------------------------------------')

    left_column,right_column = st.columns(2)
    


#ページ側の構成

    #if genre == 'Main page':        
        #page1.page1(genre)
        
    if genre == 'Spectrum':
        page5.page5(uploaded_file)
                 
    if genre == 'TL Analysis':
        page6.page6(uploaded_file,save_dir)
