import requests
from bs4 import BeautifulSoup



def tuna():
    url = "http://www.baidu.com/"

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
       # href = "https://buckysroom.org" + link.get('href')
        title = link.string
        title=str(title).replace("N","ewewewew")
        #print(href)
        print(title)
tuna()