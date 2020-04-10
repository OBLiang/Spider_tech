# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 16:06
# @Author  : DforceL
import requests
import re
from bs4 import BeautifulSoup
URL="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E7%A9%BA%E4%B8%AD%E6%B0%94%E7%90%83"
ret=requests.get(URL)
response=ret.content.decode()
# soup=BeautifulSoup(re,features="lxml")
urls= re.findall(r'thumbURL.*?\.jpg', response)
# print(soup)
# print(urls)
counter=0
for url in urls:
    # print(url[11:])
    counter+=1
    imagename=str(counter)+".jpg"
    filename="./floder/baiduimage_balloon/"+imagename

    with open(filename,"wb") as f:
        f.write(requests.get(url[11:]).content)
    print("saved as:{}".format(imagename))
