#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from typing import Type
import requests
import bs4
import time
import os
import pandas as pd

#處理防爬蟲機制 (User-agent)
headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 Edge/17.17134',
}

url ="https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_DD.djhtm"

res = requests.get(url,headers=headers)
soup = bs4.BeautifulSoup(res.text,"lxml")

path = os.path.join(os.path.expanduser("~"), 'Desktop') +'\\' #'c:\\Users\\ppp0\\desktop'
#f = open("d:\\output.txt", "w",encoding='utf-8') 
f = open(path+"output.txt", "w",encoding='utf-8') #開啟檔案並指定編碼類型
f.write(str(soup))  #寫入*.txt檔案
f.close()           #關閉檔案


#print(soup.prettify())  #輸出排版後HTML
#print(soup.title.string) #投信買賣超
#print(soup.find_all(value='005'))

#for x in soup.find_all('option'):
#    print(x, end = "\n")

#data = soup.select('table')[1]

##使用read_html建立DataFrame
#df = pd.read_html(data.prettify())
#dfs = df[0]

#刪減不要的row(index)
#dfs = dfs.drop(0)

#刪減不要的欄(index)
#dfs = dfs.drop(columns=[2,3,4,5, 6, 7, 8, 9], axis=1)

#s = dfs

#ds_reset = s.set_index(0)
#print(ds_reset)
