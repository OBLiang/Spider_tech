from bs4 import BeautifulSoup
import requests
import os
URL="http://www.ngchina.com.cn/animals/"
html=requests.get(url=URL).text
soup=BeautifulSoup(html,features="lxml")
imgul=soup.find_all("ul",{"class":"img_list"})
for ul in imgul:
    imgs=ul.find_all("img")
    for img in imgs:
        url=img['src']
        r=requests.get(url,stream=True)
        img_name=url.split('/')[-1]
        filename="./floder/"+img_name
        with open(filename,"wb") as f:
            f.write(r.content)
        print("saved as:{}".format(img_name))
