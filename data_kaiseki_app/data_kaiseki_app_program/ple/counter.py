import pandas as pd


def counter_para(d_name):
    dff = pd.read_csv('data_kaiseki_app/data_control/2dmap_para/'+str(d_name)+'.csv',encoding="shift-jis")        
    dff.columns = 0,1,2
    return(dff)

def counter_para1(d_name):
    dff = pd.read_csv('data_kaiseki_app/data_control/fig_para/'+str(d_name)+'.csv',encoding="shift-jis")        
    dff.columns = 0,1,2
    return(dff)