import pandas as pd

df1=pd.read_csv("jddfb_items.csv")
df2=pd.read_csv("jddfb_prices.csv")
# df3=df1.set_index('ProductID')
# df4=df2.set_index('ProductID')
# df4=df4.drop_duplicates()
# print(df2.price)
# print(df4)
df1=df1.merge(df2,on='ProductID')             #以某一列为准将两个数据框合并
# df3["price"]=df4.price
# df3["PreferentialPrice"]=df4["PreferentialPrice"]
df1.to_excel("jd_dfb_new.xlsx",index=None)