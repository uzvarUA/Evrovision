import requests
from bs4 import BeautifulSoup
url= 'https://eurovision.ua/5513-suspilne-ogolosylo-desyatku-finalistiv-naczvidboru-na-yevrobachennya-2024/'
res= requests.get(url)
page= res.text
soup= BeautifulSoup(page, 'html.parser')
app= soup.find_all('div', class_='wpb_wrapper')
for app in app:
	print(app.text.strip())