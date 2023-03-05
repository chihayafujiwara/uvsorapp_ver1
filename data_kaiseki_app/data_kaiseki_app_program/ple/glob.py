import os 
from glob import glob
import glob

def filesearch(dir):
    path_list = glob.glob(dir + '/*')       # 指定dir内の全てのファイルを取得

    # パスリストからファイル名を抽出
    name_list = []
    for i in path_list:
        file = os.path.basename(i)          
        name, ext = os.path.splitext(file)  
        name_list.append(name)              
    return path_list, name_list