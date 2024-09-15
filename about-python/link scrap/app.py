import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


url = "http://127.0.0.1:55469/footer.html"
response = requests.get(url)

bsoup  = bs(response.text, "html.parser")

allLinks = bsoup.findAll("a")

print(len(allLinks))

for link in allLinks:
    print("<url><loc>"+link.get('href')+"</url><loc>")