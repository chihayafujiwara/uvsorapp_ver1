import numpy as np
import streamlit as st

def Hampel(y, k, thr):
    arraySize = len(y)
    idy = np.arange(arraySize)
    output_y = y.copy()
    output_Idy = np.zeros_like(y)

    for i in range(arraySize):
        mask1 = np.where( idy >= (idy[i] - k) ,True, False)
        mask2 = np.where( idy <= (idy[i] + k) ,True, False)
        #検索範囲
        kernel = np.logical_and(mask1, mask2)
        #検索範囲の中央値
        median = np.median(y[kernel])
        
        std = 1.4826 * np.median(np.abs(y[kernel] - median))

        if np.abs(y[i] - median) > thr * std:
            output_Idy[i] = 1
            output_y[i] = median

    # return output_x, output_Idx.astype(bool)
    return output_y
