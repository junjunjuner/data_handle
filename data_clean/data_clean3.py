from bs4 import BeautifulSoup
import requests
import re
import json
import requests
import time
import codecs
import pandas as pd
'''''
从txt文件中读取id，然后利用beautifulsoup读取加热方式
'''''
def get_price(ProductID):
    json_url_p='https://item.jd.com/'+ProductID+'.html'
    try:
        web=requests.get(json_url_p).text
        s = BeautifulSoup(web, 'lxml')
        # print(s)
        guige = s.find('div', class_='Ptable')
        # print (guige)
        guige1 = guige.find_all('div', class_='Ptable-item')
        # print (guige1)
        x = {}
        for gg in guige1:
            guige2 = gg.find_all('dt', class_=None)
            guige3 = gg.find_all('dd', class_=None)
            for i in range(len(guige2)):
                dt = re.findall(">(.*?)<", str(guige2[i]))
                dd = re.findall(">(.*?)<", str(guige3[i]))
                x.setdefault(dt[0], dd[0])
        heat=x['加热方式']
    except:
        x = None
        heat=None
    print(heat)
    data = pd.DataFrame({'ProductID': [ProductID],'heat':[heat]})
    table = data.set_index('ProductID')
    table.head()
    data.to_csv('heat_qnq_data.csv',mode='a',header=False)
    print("done save csv....")
if __name__ == '__main__':
    inforead = codecs.open("heat_qnq.txt", 'r', 'utf-8')
    print('Read file:')
    ProductID = inforead.readline()
    while ProductID!="":
        ProductID = ProductID.rstrip('\r\n')
        get_price(ProductID)
        ProductID = inforead.readline()
