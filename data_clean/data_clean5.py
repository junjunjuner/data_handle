import pandas as pd
import re
df=pd.read_excel("qnq_items.xlsx")

#品牌处理
brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    brand=str(brand_list[i])
    if brand=='DYSON':
        brand='戴森'
    if brand=='AUX':
        brand='奥克斯'
    if brand=='Dyna Glo':
        brand='Dyna-Glo'
    if brand=='GEWAIHAO':
        brand='格外好'
    if brand=='SANAU':
        brand='三诺'
    if brand=='Keyeon':
        brand='凯易欧'
    if brand=='CIH':
        brand='沸尔圣'
    if brand=='Delonghi':
        brand='德龙'
    if brand=='JY吉毅':
        brand='吉毅'
    if brand=='SK':
        brand='艾斯凯杰'
    if brand=='TURBO':
        brand='德宝'
    brand_list[i] = brand
df.brand = brand_list

#商品类型处理
X_type_list=[]
for i in range(len(df.X_type)):
    X_type_list.append(df.X_type[i])
    X_type=str(X_type_list[i])
    if X_type=='电热油汀':
        X_type="油汀"
    if X_type=='电油汀':
        X_type='油汀'
    if X_type=='对衡式取暖器':
        X_type='取暖器'
    if X_type=='欧式对流快热炉':
        X_type='欧式快热炉'
    if X_type=='暖脚炉':
        X_type='暖脚器'
    if X_type=='其他':
        X_type='其它'
    X_type_list[i] = X_type
df.X_type = X_type_list

color_list=[]
for i in range(len(df.color)):
    color_list.append(df.color[i])
    color=str(color_list[i])
    if re.findall('\d',color[0]):
        color='nan'
    if color=='-':
        color='nan'
    if color=='.':
        color='nan'
    if color[0]=='/':
        color='nan'
    if re.findall('\w',color[0]):
        color='nan'
    color=re.sub('色','',color)
    color_list[i] = color
df.color = color_list
df.to_excel("qunuanqi2.xlsx",columns=df.columns,index=None)