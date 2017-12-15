import pandas as pd
'''''''''''
将三个网站的数据合并在一个表中
'''''''''''

df1=pd.read_excel("jdqnq_items.xlsx",encoding='utf8')
df2=pd.read_csv("gmqnq_items.csv")
df3=pd.read_csv("snqnq_items.csv")
df1=df1.append(df2)
df1=df1.append(df3)
df1.to_excel("qnq_items.xlsx",index=None)



