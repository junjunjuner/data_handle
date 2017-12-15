import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import re


'''
下面的命令合并文件用，注意修改为所需文件名称，并且文件在此代码文件同级目录下
'''


df1=pd.read_csv('jd_dkx.csv',encoding='utf-8')
df2=pd.read_csv('gm_dkx.csv',encoding='utf-8')
df3=pd.read_csv('sn_dkx.csv',encoding='utf-8')
# sum_df=pd.concat([df1,df3],axis=0,ignore_index=True)
# sum_df=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
sum_df=df1.append(df2).append(df3)
# sum_df.to_csv('kt_guiji.csv',columns=df3.columns,index=None)

#计算销量
sum_df['sales']=sum_df['PreferentialPrice']*sum_df['CommentCount']
# print(sum_df['sales'])
sum_df.to_excel('dkx.xlsx',index=None)