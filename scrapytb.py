from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(html):
    html = urlopen(html)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h3",{"class":"tb-main-title"})
    print(title.attrs['data-title'])


getTitle("https://item.taobao.com/item.htm?spm=2013.1.w4023-7221286617.7.FeKCXb&id=542094602004")