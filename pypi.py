from typing import Type
import requests
import bs4
import pandas as pd

url ="https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_DD.djhtm"

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,"html.parser")
print(soup.prettify())  #輸出排版後HTML
#print(soup.title.string) #投信買賣超

print(soup.find_all(value='005'))
for x in soup.find_all('option'):
    print(x, end = "\n")

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
