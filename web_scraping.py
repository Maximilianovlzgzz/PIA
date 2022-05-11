import urllib.request
def web(url):
    from bs4 import BeautifulSoup
    datos=urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(datos,"html.parser")
    tags=soup('a')
    for tag in tags:
        print(tag.get('href'))
    tags=soup('link')
    for tag in tags:
       print(tag.get('rel'))