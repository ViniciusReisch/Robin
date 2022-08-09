import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0'}
link = requests.get("https://www.terabyteshop.com.br/hardware/memorias/ddr4",
                    headers=header)
soup = BeautifulSoup(link.text, "html.parser")

price_list = soup.find_all('div', {"class": "prod-juros"})
print(price_list)

print(link)