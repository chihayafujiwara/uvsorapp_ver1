import numpy as np

def Hample(x, k, thr=3):
    arraySize = len(x)
    idx = np.arange(arraySize)
    output_x = x.copy()
    output_Idx = np.zeros_like(x)

    for i in range(arraySize):
        mask1 = np.where( idx >= (idx[i] - k) ,True, False)
        mask2 = np.where( idx <= (idx[i] + k) ,True, False)
        kernel = np.logical_and(mask1, mask2)
        median = np.median(x[kernel])
        std = 1.4826 * np.median(np.abs(x[kernel] - median))

        if np.abs(x[i] - median) > thr * std:
            output_Idx[i] = 1
            output_x[i] = median

    # return output_x, output_Idx.astype(bool)
    return output_x