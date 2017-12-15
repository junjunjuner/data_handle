import pandas as pd
import numpy as np
import re

df=pd.read_excel("dkx.xlsx")
pd.set_option('display.max_rows',None)
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    # if type(brand_list[i])==str:
    #     brand_list[i]=re.sub('\(.*?\)','',brand_list[i])
    if brand_list[i] == "ACA":
        brand_list[i] = "北美电器"
    if brand_list[i] == "UKOEO":
        brand_list[i] = "约肯意欧"
    if brand_list[i] == "IRIS":
        brand_list[i] = "爱丽思"
    if brand_list[i] == "IRIS OHYAMA":
        brand_list[i] = "爱丽思"
    if brand_list[i] == "greenis":
        brand_list[i] = "格丽思"
    if brand_list[i] == "Baumatic":
        brand_list[i] = "博曼帝克"
    if brand_list[i] == "CASDON":
        brand_list[i] = "凯度"
    if brand_list[i] == "COUSS":
        brand_list[i] = "卡士"
    if brand_list[i] == "卡氏":
        brand_list[i] = "卡士"
    if brand_list[i] == "daogrs":
        brand_list[i] = "迪奥格斯"
    if brand_list[i] == "Depelec":
        brand_list[i] = "德普"
    if brand_list[i] == "DEGURU":
        brand_list[i] = "地一"
    if brand_list[i] == "NOSTALGIA ELECTRICS":
        brand_list[i] = "诺思得其"
    if brand_list[i] == "sansui":
        brand_list[i] = "山水"
    if brand_list[i] == "WHITE TIGER":
        brand_list[i] = "威泰戈"

# print(brand_list)
df.brand=brand_list
# print(df.brand)
df2=df.loc[df.PreferentialPrice>70]
df2=df2[~(df2.p_Name.str.contains("烘焙工具")|df2.p_Name.str.contains("烘焙套餐")|df2.p_Name.str.contains("烘焙工具套餐")|df2.p_Name.str.contains("烘培模具")
          |df2.p_Name.str.contains("电磁炉")|df2.p_Name.str.contains("烟机")|df2.p_Name.str.contains("酒柜")
          |df2.p_Name.str.contains("冰箱")|df2.p_Name.str.contains("单拍不发货")|df2.p_Name.str.contains("烘焙套装")|df2.p_Name.str.contains("秤"))]
# df=df.sort(columns="PreferentialPrice")
df2.to_excel("dkx3.xlsx",columns=df.columns,index=None)