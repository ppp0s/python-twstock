#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from binascii import a2b_hex
from pydoc import classname
import string
from subprocess import HIGH_PRIORITY_CLASS
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
#f = open(path+"output.txt", "w",encoding='utf-8') #開啟檔案並指定編碼類型
#f.write(str(soup))  #寫入*.txt檔案
#f.close()           #關閉檔案

'''
print(soup.find_all("div", class_="t11")) # [<div class="t11">日期：09/06</div>]
soup.find_all("html_element", class_="your_class_name") #find_all語法
'''
#print(soup.find("div", class_="t11").string[3:]) # 日期：09/06 -> 0906

def ccdp(high,low,c):
    CDP = (H+L+2*C)/4
    Pt = H - L #震幅
    ah = CDP + Pt
    nh = 2*CDP - L
    nl = 2*CDP - H
    al = CDP - Pt

    print(str(round(ah,2)))  #追買
    print(str(round(nh,2)))  #賣出
    print(str(round(CDP,2))) #CDP
    print(str(round(nl,2)))  #買進
    print(str(round(al,2)))  #追賣

#print(round(Pt,2))

if __name__ == '__main__': #主程式進入點
    H = 120.5 #最高
    L = 113.0 #最低
    C = 119.0 #收
    ccdp(H,L,C)
