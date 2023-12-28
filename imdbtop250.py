import requests

from bs4 import BeautifulSoup

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url=url,headers=header)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("a",{"class":"ipc-title-link-wrapper"})

puanlar = soup.find_all("span",{"class":"sc-43986a27-1 fVmjht"})


for baslik,puan in zip(basliklar,puanlar):
    print(baslik.text,"\n",puan.text[:3])
    print("*******************")
