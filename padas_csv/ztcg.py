import pandas as pd

df=pd.read_excel("ztcg.xlsx")

'''''''''''
取出销量前20的品牌
'''''''''''
# df1 = df.groupby(by=['brand'])['sales'].sum()
# df1=df1.to_frame()
# # print (df1)
# df1=df1.sort(columns="sales", ascending=False)
# # df1['brand']=df1.index
# # df1=df1.reset_index(drop=True)
# # print(df1)
# x=df1.head(20).index.values
# print(x)
# df1.to_excel("cg.xlsx")

# #一
# df_new=pd.DataFrame()
# df1 = df.groupby(by=['brand'])['sales'].sum()
# df1=df1.to_frame()
# # print (df1)
# df1=df1.sort(columns="sales", ascending=False)
# # df1['brand']=df1.index
# # df1=df1.reset_index(drop=True)
# # print(df1)
# pro=df1.head(120).index.values
# for p in pro:
#     df2=df[df.brand==p]
#     df_new=df_new.append(df2)
# df_new=df_new[~(df_new.X_type=="拉手")]
# df_new=df_new[df_new.p_Name.str.contains("橱柜")]
# df_new=df_new[~df_new.p_Name.str.contains("衣柜")]
# df_new.to_excel("cg.xlsx")


# 二
# df1=df[~((df.X_type=='拉手')|(df.X_type=='抽屉导轨')|(df.X_type=='铰链')|(df.X_type=='开关')|(df.X_type=='洗衣机柜')
#         |df.X_type.str.contains("工具")|df.X_type.str.contains("水槽")|(df.X_type.str.contains("浴")))]
# # df1=df1[df1.p_Name.fillna("none").str.contains("厨柜")]
# df1=df1[~(df1.p_Name.str.contains("衣柜")|df1.p_Name.str.contains("酒柜")|df1.p_Name.str.contains("鞋柜")
#           |df1.p_Name.str.contains("书柜")|df1.p_Name.str.contains("水篮")|df1.p_Name.str.contains("衣帽"))]
# df1.to_excel("cg1.xlsx",index=None)
# df2=pd.read_excel("cg1.xlsx")
# df2=df2[~(df2.p_Name.str.contains("摆件")|df2.p_Name.str.contains("脚")|df2.p_Name.str.contains("刀")
#           |df2.p_Name.str.contains("消毒柜")|df2.p_Name.str.contains("卡尺")|df2.p_Name.str.contains("浴"))]
# df2.to_excel("cg2.xlsx",index=None)
# df2=pd.read_excel("cg2.xlsx")
# df2=df2[~(df2.p_Name.str.contains("钻")|df2.p_Name.str.contains("模型")|df2.p_Name.str.contains("资料")
#           |df2.p_Name.str.contains("开孔器")|df2.p_Name.str.contains("灯")|df2.p_Name.str.contains("茶几")|
#           df2.p_Name.str.contains("档案柜") |df2.p_Name.str.contains("榻榻米"))]
# df2=df2.drop_duplicates('ProductID')
# df2.to_excel("cg3.xlsx",index=None)
df2=pd.read_excel("cg3.xlsx")
df2=df2[~(df2.p_Name.str.contains("餐边柜")|df2.p_Name.str.contains("简易"))]
df2=df2.drop_duplicates('ProductID')
df2.to_excel("cg4.xlsx",index=None)
