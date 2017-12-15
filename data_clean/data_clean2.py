import pandas as pd
import re

''''''''''
对csv文件数据进行清理
'''''''''''
df=pd.read_csv("jdqnq.csv")
pd.set_option('display.max_rows',None)

brand_list=[]
for i in range(len(df.brand)):
    brand_list.append(df.brand[i])
    #品牌处理
    brand=str(brand_list[i])
    # print(brand)
    if 'pocatan' in brand:
        brand = 'pocatan'
    if ('戴森' or 'dyson' or 'Dyson') in brand:
        brand = '戴森'
    if ('巴慕达' or 'BALMUDA') in brand:
        brand = '巴慕达'
    if 'AUX' in brand:
        brand = 'AUX'
    if ('Beurer' or '博雅') in brand:
        brand = '博雅'
    if 'BOKUK' in brand:
        brand = 'BOKUK'
    if 'BUSHENGDIANQI' in brand:
        brand = '步升电器'
    if ('CHIGO' or '志高') in brand:
        brand = '志高'
    if ('DeLonghi' or '德龙') in brand:
        brand = '德龙'
    if ('Honeywell' or '霍尼韦尔') in brand:
        brand = '霍尼韦尔'
    # if 'HYUNDAI' in brand:
    #     brand = '韩国现代'
    if 'IRIS' in brand:
        brand = '爱丽思'
    # if 'JY吉毅' in brand:
    #     brand = '吉毅'
    if 'Keyeon' in brand:
        brand = '凯易欧'
    if ('KONKA' or '康佳') in brand:
        brand = '康佳'
    if 'MIH' in brand:
        brand = '米拉德'
    if 'MORITA' in brand:
        brand = '森田'
    if 'namunani' in brand:
        brand = '纳木那尼'
    if ('NOIROT' or '诺朗') in brand:
        brand = '诺朗'
    if 'Paosecuxinv' in brand:
        brand = '普森斯瑞'
    if ('PHILCO' or '飞歌') in brand:
        brand = '飞歌'
    if 'renebelle' in brand:
        brand = 'renebelle'
    if 'Re-life' in brand:
        brand = 'Re-life'
    if 'RuiXinDa' in brand:
        brand = '瑞鑫达'
    if 'sichler' in brand:
        brand = 'sichler'
    if 'SANAU' in brand:
        brand = '三诺'
    if 'SANSHIAH' in brand:
        brand = '三夏'
    if 'Semptec' in brand:
        brand = 'Semptec'
    if 'SEGI' in brand:
        brand = '世纪'
    if 'SheerAIRE' in brand:
        brand = '席爱尔'
    if 'SK' in brand:
        brand = '艾斯凯杰'
    if 'Smart Frog' in brand:
        brand = '卡蛙'
    if 'SONGX' in brand:
        brand = '松心'
    if 'SVIII' in brand:
        brand = '山湖'
    if 'TCL' in brand:
        brand = 'TCL'
    if ('AKAI' or '雅佳') in brand:
        brand = '雅佳'
    if ('singfun' or '先锋') in brand:
        brand = '先锋'
    if ('Tefal' or '特福') in brand:
        brand = '特福'
    if ('Stadler Form' or '斯泰得乐') in brand:
        brand = '斯泰得乐'
    if ('奥克斯' or 'AUX') in brand:
        brand = '奥克斯'
    if 'YOSTAR' in brand:
        brand = 'YOSTAR'
    if '长虹' in brand:
        brand = '长虹'
    if '美的' in brand:
        brand = '美的'
    if '惠而浦' in brand:
        brand = '惠而浦'
    if '海尔' in brand:
        brand = '海尔'
    if '澳洲阳光' in brand:
        brand = '澳洲阳光'
    if 'Soleil' in brand:
        brand = 'Soleil'
    if 'World Marketing' in brand:
        brand = 'World Marketing'
    if 'Dura Heat' in brand:
        brand = 'Dura Heat'
    if 'Mr. Heater' in brand:
        brand = 'Mr. Heater'
    if 'Comfort Glow' in brand:
        brand = 'Comfort Glow'
    if 'Dyna-Glo' in brand:
        brand = 'Dyna-Glo'
    if 'Lasko' in brand:
        brand = 'Lasko'
    if 'Optimus' in brand:
        brand = 'Optimus'
    if ('百奥耐尔' or 'Bionaire') in brand:
        brand = '百奥耐尔'
    if 'Lifesource' in brand:
        brand = 'Lifesource'
    if '美的' in brand:
        brand = '美的'
    if ('格力' or 'GREE') in brand:
        brand = '格力'
    # print(brand)
    # print(brand)
    brand_list[i]=brand
    # print(df.loc[i].brand)
df.brand = brand_list

X_type_list=[]
for i in range(len(df.X_type)):
    #类型处理
    X_type_list.append(df.X_type[i])
    X_type=str(X_type_list[i])
    if X_type=="其他":
        X_type="其它"
    if X_type=="冷暖型":
        X_type="冷暖一体"
    if '电热膜' in X_type:
        X_type='电热膜'
    X_type_list[i]=X_type
df.X_type = X_type_list

gear_list=[]
for i in range(len(df.gear)):
    #档位处理
    # print (gear)
    # print(type(gear))
    gear_list.append(df.gear[i])
    gear=str(gear_list[i])
    gear =re.sub('调温','',gear)
    gear =re.sub('位','',gear)
    gear =re.sub('二','2',gear)
    gear = re.sub('三', '3', gear)
    gear = re.sub('四', '4', gear)
    gear = re.sub('五', '5', gear)
    gear_list[i]=gear
df.gear = gear_list

adapt_area_list=[]
for i in range(len(df.adapt_area)):
    #适用面积处理
    adapt_area_list.append(df.adapt_area[i])
    adapt_area=str(adapt_area_list[i])
    adapt_area=re.sub('以及','',adapt_area)
    adapt_area=re.sub('平米','㎡',adapt_area)
    if re.findall('\d',adapt_area[-1]):
        adapt_area=adapt_area[:]+'㎡'
    if adapt_area=='10㎡以下':
        adapt_area='10㎡以及以下'
    if '-' in adapt_area:
        a1=int(adapt_area.split('-')[0][:])
        a2=int(adapt_area.split('-')[1][:-1])
        if a1>=10 and a2<=20:
            adapt_area="11-20㎡"
        if a1>=20 and a2<=30:
            adapt_area="21-30㎡"
        if a1>=30 and a2<=40:
            adapt_area="31-40㎡"
        if a1>=40:
            adapt_area="40㎡以上"
    adapt_area_list[i] = adapt_area
df.adapt_area = adapt_area_list

    # print(brand_list[i)
    # print(brand_list[i)
    # print(df.loc[i].brand_list[i)
df.to_excel("qunuanqi1.xlsx",columns=df.columns,index=None)