import pandas as pd
'''''''''''
将价格与商品详情合并在一起
'''''''''''
df1=pd.read_csv("jdqnq_items_pn.csv")
df2=pd.read_csv("jdqnq_price.csv")
df3=pd.read_csv("jdqnq_price11.csv")
df4=pd.read_csv("jdqnq_price8000.csv")
df2=df2.append(df3)
df2=df2.append(df4)
df1=df1.merge(df2,on='ProductID')             #以某一列为准将两个数据框合并
# df1=df1.merge(df3,on='ProductID')             #以某一列为准将两个数据框合并
# df1=df1.merge(df4,on='ProductID')             #以某一列为准将两个数据框合并
df1.to_csv("jdqnq.csv")
