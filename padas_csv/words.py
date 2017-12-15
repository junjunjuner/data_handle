
import pandas as pd

'''''''''
处理关键字,按照品牌对关键字进行分类
'''''''''
#对关键词进行分类
word1={"包装完好":["包装完好","包装仔细","包装给力","包装结实"],
        "宝贝不错":["真的很不错","不错","宝贝不错","不错不错","东西很不错","东西不错","还不错","还不错还不错","很不错很不错","真心不错","挺好的","挺好挺好","挺不错的哦","还可以吧","还好","烤箱不错","烤箱实用"],
        "东西很好":["东西很好","很好五分","很好很好","很好用很好用","很好的东东","烤箱很好","棒棒棒","非常好用","非常满意","非常好"],
        "材质很赞":["材质很赞","材质大器"],
        "操作方便":["操作简单","操作方便","操作便捷"],
        "大容量":["大容量","大","容量大"],
        "服务态度好":["服务超级好","服务态度好","服务不错","服务到位","服务好","服务很好","售后服务好","售后好","售后很好","态度好"],
        "质量好":["质量很好","质量不错","质量还不错"],
        "值得购买":["值得拥有","值得购买"],
        "外观漂亮":["外观漂亮","产品美观","外观大气","造型别致","款式好看","款式漂亮","时尚外观","外观时尚","美观","样子好看"],
        "性价比高":["性价比高","性价比超高","性比价高","性价比挺高",],
        "物流快":["物流速度快","物流超快","发货送货都很快","快递给力"],
        "价格划算":["价格划算","价格便宜","价格实惠","价格适宜"],
        "方便使用":["方便使用","方便好用","方便快捷"],
        "质量可靠":['质量非常不错','质量非常好','质量很不错','质量还是很好的','质量好','质量有保证','质量有保障'],
        "制热效果好":['制热效果快','制热效果好便宜','制热快外观美观']}

'''''''''''
取出销量前20的品牌
'''''''''''
writer=pd.ExcelWriter("取暖器.xlsx")
df=pd.read_excel('qnq_items.xlsx',sheetname='Sheet1')
df['sales']=df['PreferentialPrice']*df['CommentCount']
df=df.drop_duplicates()
df1 = df.groupby(by=['brand'])['sales'].sum()
df1=df1.to_frame()
# print (df1)
df1=df1.sort(columns="sales", ascending=False)
# df1['brand']=df1.index
# df1=df1.reset_index(drop=True)
# print(df1)
process=df1.head(20).index.values
print(process)

# # df1=pd.read_csv('ktguiji.csv',encoding='utf-8')
# # df1.to_excel('ktguiji.xlsx')
# df=pd.read_excel("xwj.xlsx",sheetname='Sheet1')
# # process=["海尔","格力","奥克斯","美的","惠而浦","TCL","长虹","扬子","科龙","海信","志高","大金","三菱电机","格兰仕","伊莱克斯"]    #柜机
# process=["西门子","美的","老板","海尔","方太","松下","徳兆","九阳","惠而浦","村田","CAL","HUMANTOUCH","伊莱克斯","亨利华","华帝","奥克斯","乐创","森太","美诺","内芙"]
# # process=["格兰仕","格力"]
brand=df["brand"].values
# print (brand)
keyword=df["keyword"].values
ser_info=pd.DataFrame(keyword,index=brand)
ser_info=ser_info.dropna()
df4=pd.DataFrame()
for p in process:
    try:
        ser=ser_info.loc[p].values
        # print (ser)
    except:               #若某个品牌没有关键词,ser=[]
        print (p)
        ser=[' ']
        # print(ser)
    ser_list=[]
    # print (ser)
    if len(ser)>1:
        for i in range(len(ser)):
            ser_list.extend(ser[i])
        data_str=' '.join(ser_list)
        data=data_str.replace('"','').replace(',',' ').replace('。','')
        data_list=data.split(' ')
        # print (data_list)
        x={}
        for k in data_list:
            if len(k)>0:

                # 关键词分类
                k=k.replace('!', '')
                for key, value in word1.items():
                    if k in value:
                        k = key

                if k in x.keys():
                    x[k]=x[k]+1
                else:
                    x.setdefault(k,1)
        df2=pd.DataFrame(x,index=["评论数"]).T
        df2["品牌"]=p
        df3=df2.sort(columns="评论数",ascending=False)
        # df3.to_excel(writer,p)
        df4 = df4.append(df3)
        # print (x)
    else:            #若某品牌只有一个关键词
        data_str=' '.join(ser)
        data=data_str.replace('"','').replace(',',' ').replace('。','')
        data_list=data.split(' ')
        # print (data_list)
        x={}
        for k in data_list:
            if len(k)>0:

                #关键词分类
                k=k.replace('!','')
                for key, value in word1.items():
                    if k in value:
                        k = key

                if k in x.keys():
                    x[k]=x[k]+1
                else:
                    x.setdefault(k,1)
        # df2=pd.DataFrame(x,index=[p]).T
        # df3=df2.sort(columns=p,ascending=False)
        # df3.to_excel(writer,p)
        df2 = pd.DataFrame(x, index=["评论数"]).T
        df2["品牌"] = p
        df3 = df2.sort(columns="评论数", ascending=False)
        df4=df4.append(df3)
        # print(x)
# df4['评论关键字']=df4.index
# df4=df4.reset_index(drop=True)
df4.index.name="评论关键词"
df.to_excel(writer,"取暖器",index=None)
df4.to_excel(excel_writer=writer,sheet_name="取暖器_词云图")
df1.to_excel(excel_writer=writer,sheet_name="销量")
writer.save()


