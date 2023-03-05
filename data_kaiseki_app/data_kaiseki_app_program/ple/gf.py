import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

def gaussian(df,x,y,m):
    y = y/m
    def func(x, *params):

    #paramsの長さでフィッティングする関数の数を判別。
        num_func = int(len(params)/3)

        #ガウス関数にそれぞれのパラメータを挿入してy_listに追加。
        y_list = []
        for i in range(num_func):
            y = np.zeros_like(x)
            param_range = list(range(3*i,3*(i+1),1))
            amp = params[int(param_range[0])]
            ctr = params[int(param_range[1])]
            wid = params[int(param_range[2])]
            y = y + amp * np.exp( -((x - ctr)/wid)**2)
            y_list.append(y)

        #y_listに入っているすべてのガウス関数を重ね合わせる。
        y_sum = np.zeros_like(x)
        for i in y_list:
            y_sum = y_sum + i

        #最後にバックグラウンドを追加。
        y_sum = y_sum + params[-1]

        return y_sum

    def fit_plot(x, *params):
        num_func = int(len(params)/3)
        y_list = []
        for i in range(num_func):
            y = np.zeros_like(x)
            param_range = list(range(3*i,3*(i+1),1))
            amp = params[int(param_range[0])]
            ctr = params[int(param_range[1])]
            wid = params[int(param_range[2])]
            y = y + amp * np.exp( -((x - ctr)/wid)**2) + params[-1]
            y_list.append(y)
        return y_list

    num = 1
    while num < 4:
        if num == 1:
            guess = []
            guess.append([df['fit 1'][0],df['fit 1'][1],df['fit 1'][2]]) #[amp,ctr,wid]
            #バックグラウンドの初期値
            background = df['base'][0]
            guess_total = []
            for i in guess:
                guess_total.extend(i)
            guess_total.append(background)
            popt, pcov = curve_fit(func, x, y, p0=guess_total)
            fit = func(x, *popt)
            y_list = fit_plot(x, *popt)
            residuals1 = y - fit
            rss = np.sum(residuals1**2) #残渣二乗和
            tss = np.sum((y-np.mean(y))**2) #平均からの差の二乗和
            r_squared1 = 1 - (rss/tss)
            baseline = np.zeros_like(x) + popt[-1]
            #df1 = fit
            residuals1=pd.DataFrame(residuals1)
            residuals1.columns=['resi']
            df1_1 = pd.DataFrame(y_list[0])
            df1_1.columns = ['fit sum']
            df1_2 = pd.DataFrame(y_list[0])
            df1_2.columns = ['fit 1']
            df1 = df1_1.join(df1_2)
            print(r_squared1)
            parameter1 = popt
            print(parameter1)
            num = num + 1
            continue
        
        elif num == 2:
            guess = []
            guess.append([df['fit 2'][0],df['fit 2'][1],df['fit 2'][2]])
            guess.append([df['fit 2'][3],df['fit 2'][4],df['fit 2'][5]])
        #バックグラウンドの初期値
            background =  df['base'][0]
            guess_total = []
            for i in guess:
                guess_total.extend(i)
            guess_total.append(background)
            popt, pcov = curve_fit(func, x, y, p0=guess_total)
            fit = func(x, *popt)
            y_list = fit_plot(x, *popt)
            residuals2 = y - fit
            rss = np.sum(residuals2**2) #残渣二乗和
            tss = np.sum((y-np.mean(y))**2) #平均からの差の二乗和
            r_squared2 = 1 - (rss/tss)
            baseline = np.zeros_like(x) + popt[-1]
            residuals2=pd.DataFrame(residuals2)
            residuals2.columns=['resi']
            df1_2 = pd.DataFrame(y_list[0])
            df1_2.columns = ['fit 1']
            df2_2 = pd.DataFrame(y_list[1])
            df2_2.columns = ['fit 2']
            df2_fit = pd.DataFrame(fit)
            df2_fit.columns = ['fit sum']
            df2_ = df1_2.join(df2_2)
            df2 = df2_fit.join(df2_)
            print(r_squared2)
            parameter2 = popt
            print(parameter2)
            num = num + 1
            continue
            
        elif num == 3:
            guess = []
            guess.append([df['fit 3'][0],df['fit 3'][1],df['fit 3'][2]])
            guess.append([df['fit 3'][3],df['fit 3'][4],df['fit 3'][5]])
            guess.append([df['fit 3'][6],df['fit 3'][7],df['fit 3'][8]])
        #バックグラウンドの初期値
            background =  df['base'][0]
            guess_total = []
            for i in guess:
                guess_total.extend(i)
            guess_total.append(background)
            popt, pcov = curve_fit(func, x, y, p0=guess_total)
            fit = func(x, *popt)
            y_list = fit_plot(x, *popt)
            residuals3 = y - fit
            rss = np.sum(residuals3**2) #残渣二乗和
            tss = np.sum((y-np.mean(y))**2) #平均からの差の二乗和
            r_squared3 = 1 - (rss/tss)
            baseline = np.zeros_like(x) + popt[-1]
            residuals3=pd.DataFrame(residuals3)
            residuals3.columns=['resi']
            df1_3 = pd.DataFrame(y_list[0])
            df1_3.columns = ['fit 1']
            df2_3 = pd.DataFrame(y_list[1])
            df2_3.columns = ['fit 2']
            df3_3 = pd.DataFrame(y_list[2])
            df3_3.columns = ['fit 3']
            df3_fit = pd.DataFrame(fit)
            df3_fit.columns = ['fit sum']
            df3j1 = df3_fit.join(df1_3)
            df3j2 = df2_3.join(df3_3)
            df3 = df3j1.join(df3j2)
            print(r_squared3)
            parameter3 = popt
            print(parameter3)
            num = num + 1
            continue
    
    dfx = np.array(['1','2','3'])
    dfy = np.array([r_squared1,r_squared2,r_squared3])
    dfx = pd.DataFrame(dfx)
    dfy = pd.DataFrame(dfy)
    r_matome = pd.concat([dfx,dfy],axis = 1)
    r_matome.columns = 'comp','R^2'

    x = pd.DataFrame(x)
    x.columns = ['wave']
    y = pd.DataFrame(y)
    y.columns = ['Raw data']

    #m = y.max()
    
    data1= pd.concat([x,y*m,df1*m,residuals1*100],axis =1)
    data2 = pd.concat([x,y*m,df2*m,residuals2*100],axis =1)
    data3 = pd.concat([x,y*m,df3*m,residuals3*100],axis =1)

    fit1 =[['fit1',round(r_squared1,3),round(parameter1[-1]*m,3),round(parameter1[0]*m,3),round(parameter1[1],3),round(parameter1[2],3)]]
    fit2 =[['fit2',round(r_squared2,3),round(parameter2[-1]*m,3),round(parameter2[0]*m,3),round(parameter2[1],3),round(parameter2[2],3),round(parameter2[3]*m,3),round(parameter2[4],3),round(parameter2[5],3)]]
    fit3 =[['fit3',round(r_squared3,3),round(parameter3[-1]*m,3),round(parameter3[0]*m,3),round(parameter3[1],3),round(parameter3[2],3),round(parameter3[3]*m,3),round(parameter3[4],3),round(parameter3[5],3),round(parameter3[6]*m,3),round(parameter3[7],3),round(parameter3[8],3)]]
    fit1 = pd.DataFrame(fit1)
    fit2 = pd.DataFrame(fit2)
    fit3 = pd.DataFrame(fit3)
    fit1.columns = 'number of component','R^2','base','a1','b1','c1'
    fit2.columns = 'number of component','R^2','base','a1','b1','c1','a2','b2','c2'
    fit3.columns = 'number of component','R^2','base','a1','b1','c1','a2','b2','c2','a3','b3','c3'
    
    fit_al = pd.concat([fit1,fit2],axis=0)
    fit_all = pd.concat([fit_al,fit3],axis=0)
    fit_all = fit_all.set_index('number of component')

    return([data1,data2,data3,fit_all,r_matome])