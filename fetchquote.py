import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://www.brainyquote.com/search_results.html?q="
stext = input("Enter Keyword\n")
url = url+stext
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
try:
    html = urlopen(req)
except urllib.error.HTTPError as err:
    print()
soup = BeautifulSoup(html,"html.parser")

for script in soup(["script", "style"]):
    script.extract()
    
for content in soup.findAll('a',{'class':'b-qt'}):
    print(content.text)
