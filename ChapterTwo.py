from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span",{"class":"green"})
nametimes = bsObj.findAll(text="the prince")
# print(len(nametimes))
for name in nameList:
    pass
    # print(name.get_text())
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)