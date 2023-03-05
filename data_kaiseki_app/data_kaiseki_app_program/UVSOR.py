from binascii import crc32
from cProfile import label
from distutils.command.build_scripts import first_line_re
import pandas as pd
import numpy as np
import streamlit as st
from urllib3 import encode_multipart_formdata
from PIL import Image
import page1
import page2
import page3
import page4
import aple
import atl

from ple import uvsor1
from ple import uvsor2



st.set_page_config(
    page_title="UVSOR Analysis app",
    layout="wide",
    initial_sidebar_state="expanded",
)

image1 = Image.open('../data_control/image1.png')
st.sidebar.image(image1)

with st.sidebar.expander("Select"):
    g = st.selectbox("Tool type", ('PLE','TL'))
    save_dir = st.text_input('ファイル保存先')

if not save_dir:
    save_dir = '../data_output'

if g == 'PLE': 
    aple.aple(save_dir)
    
if g == 'TL':
    atl.atl(save_dir)
    
