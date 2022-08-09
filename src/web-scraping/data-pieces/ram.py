import requests
from bs4 import BeautifulSoup

precos = []
alvo = "https://www.terabyteshop.com.br/hardware/memorias/ddr4"
response = requests.get(alvo)
print(response)
html = BeautifulSoup(response.text, 'html.parser')
print(html)
for preco in html.select('.prod-new-price span'):
    precos.append(preco.text)

print(precos)

