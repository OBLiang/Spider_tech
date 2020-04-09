# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 12:45
# @Author  : DforceL
import requests
from bs4 import BeautifulSoup
import os
URL="https://www.msgao.com/xinggan/"
HTML=requests.get(URL).text
# print(HTML)
soup=BeautifulSoup(HTML,features="lxml")
# print(soup)
imgullist=soup.find_all("div",{"class":"listmain left"})
# print(imgullist)
counter=0
for iul in imgullist:
    imgusl=iul.find_all("img")
    for imgul in imgusl:
        ul=imgul["src"]
        counter+=1
        r=requests.get(ul)
        imgname=str(counter)+".jpg"
        pathname="./floder/sexylady/"+imgname
        with open(pathname,"wb") as f:
            f.write(r.content)
        print("saved as:{}".format(imgname))

