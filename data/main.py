from data import  My_DataFrame
import pandas as pd
m=pd.read_csv("geli1.csv")
m['ask']=m['ask'].fillna(method='pad')
m['href']=m['href'].fillna(method='pad')
m=m.sort_values(['title','time_now'])
m['mark']=1
m['num']=range(len(m))
m=m.set_index('num')
# m.to_excel('gree.xlsx')
m=m.fillna('none')
DF=My_DataFrame(m)
DF.my_mergewr_excel('000_2.xlsx',['title'],['title','ask','href'])
df=pd.read_excel('000_2.xlsx',encoding='utf-8',na_values='none')
df.to_excel('000_3.xlsx',columns=df.columns,index=None)