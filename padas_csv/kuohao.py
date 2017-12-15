import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import re


'''
下面的命令即可去掉括号的，注意修改为所需文件名称，并且文件在此代码文件同级目录下
'''

df=pd.read_excel('ktbgs.xlsx',encoding='utf-8')
# print(df.columns)
pd.set_option('display.max_rows',None)
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    if type(brand_list[i])==str:
        brand_list[i]=re.sub('\(.*?\)','',brand_list[i])
    if brand_list[i] == "Panasonic":
        brand_list[i] = "松下"
    if brand_list[i] == "CHEBLO":
        brand_list[i] = "樱花"
    if brand_list[i] == "MBO":
        brand_list[i] = "美博"
    if brand_list[i] == "YAIR":
        brand_list[i] = "扬子"
    if brand_list[i] == "PHLGCO":
        brand_list[i] = "飞歌"
    if brand_list[i] == "FZM":
        brand_list[i] = "方米"
    if brand_list[i] == "inyan":
        brand_list[i] = "迎燕"
    if brand_list[i] == "JENSANY":
        brand_list[i] = "金三洋"
# print(brand_list)
df.brand=brand_list
# print(df.brand)
df.to_excel('ktbgs_new.xlsx',columns=df.columns,index=None)
