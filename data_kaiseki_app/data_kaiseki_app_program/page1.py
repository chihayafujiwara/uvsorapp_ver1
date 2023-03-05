import streamlit as st

def page1(genre):
    col1, col2, col3 = st.columns([1,2,1])
    col2.write("""##### A tool for analyzing and visualizing UVSOR BL3B data""")
    col2.write("""###### Created by FUJIWARA, Chihaya , chihaya.fujiwara.r5@dc.tohoku.ac.jp""")
    st.write('----------------------------------')
    st.write("""### About this tool""")
    col1,col2 = st.columns([1,1])
    
    markdown1 = """
    ###### UVSOR BL3Bにおいて計測したデータを解析・可視化を迅速に簡単に行うためのアプリケーションです。拡張子が.2dpleのdataを使用してください。左のAnalysis typeのタブから行いたい解析・可視化のタイプを選択してください。このアプリケーション内で行うことができることは以下の通りです。
    * **Main page** ： 現在のページ
    * **2DMAP** ：  縦軸,横軸にそれぞれ発光波長と励起波長とり,カラーマップを強度とした2DMAPを作成します。詳細な図の設定も変更可能です。 
    * **Spectrum** :    任意の励起波長(発光波長)時の発光(励起)スペクトルをデータより可視化します。詳細な図の設定，スペクトルデータの出力も可能です。
    * **Multi gaussian fit** : 任意の発光スペクトルに対し，マルチガウシアンフィットを行います。外部CSVファイルからパラメータを入力してください。
    """
    col1.markdown(markdown1)

    markdown2 = """
    ###### This is an application for quick and easy analysis and visualization of data measured at UVSOR BL3B . (Output data format is .2dple.) Select the type of analysis/visualization you wish to perform from the Analysis type tab on the left. The following is what you can do in this application.        
    * **Main page** ： We are here.
    * **2DMAP** ：  The vertical and horizontal axes are the emission wavelength and excitation wavelength, respectively, and a 2DMAP is created with the intensity as a color map. The detailed figure settings can also be changed. 
    * **Spectrum** :    The emission (excitation) spectrum at any excitation wavelength (emission wavelength) is visualized from the data. Detailed diagram settings and spectral data output are also available.。
    * **Multi gaussian fit** : Performs a multi-Gaussian fit to an arbitrary emission spectrum. Enter parameters from an external CSV file。
    """

    col2.markdown(markdown2)        

    st.write('----------------------------------')

