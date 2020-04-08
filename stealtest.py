# # -*- coding: utf-8 -*-
# # @Time    : 2020/4/8 21:14
# # @Author  : DforceL
# import requests
# import os
# from bs4 import BeautifulSoup
# URL="https://www.birdnet.cn/atlas.php?mod=show&action=myatlas&uid=594295"
# html=requests.get(URL).text
# # print(html)
# soup=BeautifulSoup(html,features="lxml")
# # print(soup)
# imgullist=soup.find_all("ul",{"id":"list_show"})
# counter=0
# for imguls in imgullist:
#     imgul=imguls.find_all("img")
#     for il in imgul:
#         imgulfinal=il["src"]
#         counter+=1
#         # print(imgulfinal)
#         imgname=str(counter)+".jpg"
#         pathname="./floder/bird/"+imgname
#         r=requests.get(imgulfinal)
#         with open(pathname,"wb")as fw:
#             fw.write(r.content)
#         print("saved as:{}".format(imgname))

import requests
import os
from bs4 import BeautifulSoup
URL="http://www.sirenji.com/plane/"
html=requests.get(URL).text
# print(html)
soup=BeautifulSoup(html,features="lxml")
urllist=soup.find_all("div",{"class":"carmain"})
counter=0
for urls in urllist:
    urlsreal=urls.find_all("img")
    for urlreal in urlsreal:
        counter+=1
        urlfinal=urlreal["src"]
        r=requests.get(urlfinal)
        filename=str(counter)+".jpg"
        pathname="./floder/airplane/"+filename
        with open(pathname,"wb")as f:
            f.write(r.content)
        print("saved as:{}".format(filename))