import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import re
import csv

# Memória ram 8gb DDR4
namesProducts = []
header = {'user-agent': 'Mozilla/5.0'}
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422", headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

for name in soup.select('.MuiTypography-h6'):
    namesProducts.append(name.text)

navegador = webdriver.Chrome()
navegador.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')
product = navegador.find_elements('class name', 'jss191')
priceProducts = []
sleep(2)
for i in product:
    if i.text == "":
        continue
    priceProducts.append(i.text)
    sleep(1)

allLinkProducts = []
linkProducts = navegador.find_element_by_xpath('//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[1]/a')
sleep(2)
for i in linkProducts:
    if i.text == "":
        continue
    allLinkProducts.append(i.text)
    sleep(1)
print(allLinkProducts)

# Reunindo dados em json
allData = []
for i in range(len(priceProducts)):
    if len(priceProducts[i]) >= 10:
        priceProducts[i] = priceProducts[i].replace('.', '')
    changeablePriceProducts = priceProducts[i].replace('R$', '').replace(',', '.')
    dataDic = {
        "Name": namesProducts[i],
        "Price": [priceProducts[i], float(changeablePriceProducts)]
    }
    allData.append(dataDic)
print(allData)

