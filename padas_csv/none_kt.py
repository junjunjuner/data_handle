import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import re


'''
下面的命令即可去掉小写none的，注释部分是增加字段的代码，如有需要去掉注释就可以，注意修改为所需文件名称，并且文件在此代码文件同级目录下
'''
df=pd.read_csv('jd_guiji.csv',encoding='utf-8',na_values='none')
df['source']='京东'
df.to_csv('jd_guiji_new.csv',columns=df.columns,index=None)