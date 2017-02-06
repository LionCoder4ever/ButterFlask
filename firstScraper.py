from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        try:
            someTag = bsObj.h1
        except AttributeError as e:
            print("tag was not found")
        else:
            if someTag is None:
                print("tag was not found")
            else:
                print(someTag)

