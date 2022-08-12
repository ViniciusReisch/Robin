import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import re
import csv

# Memória ram 8gb DDR4
namesProducts = []
imgProducts = []
allData = []
linksProducts = []
pricesProducts = []
header = {'user-agent': 'Mozilla/5.0'}
<<<<<<< HEAD
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422", headers=header)
=======
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422",
                        headers=header)
>>>>>>> edab21b0b3498838eff5a8255edae015090aa5bf
soup = BeautifulSoup(response.text, 'html.parser')

for name in soup.select('.MuiTypography-h6'):
    namesProducts.append(name.text)

<<<<<<< HEAD
navegador = webdriver.Chrome()
navegador.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')
product = navegador.find_elements('class name', 'jss191')
priceProducts = []
sleep(2)
for i in product:
=======
driver = webdriver.Chrome()
driver.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')
produto = driver.find_elements('class name', 'jss64')

for i in produto:
>>>>>>> edab21b0b3498838eff5a8255edae015090aa5bf
    if i.text == "":
        continue
    pricesProducts.append(i.text)

<<<<<<< HEAD
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
=======
links = driver.find_elements('tag name', 'a')
for i in links:
    if 'memoria' in i.get_attribute('href'):
        linksProducts.append(i.get_attribute('href'))

linksImg = driver.find_elements('tag', 'img')
print(linksImg)
for i in linksImg:
    imgProducts.append(i.get_attribute('src'))

# Reunindo dados em dictionary
for i in range(len(pricesProducts)):
    if '.' in pricesProducts[i]:
        pricesProducts[i] = pricesProducts[i].replace('.', '')
    changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
    dataDic = {'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)], 'Link': linksProducts[i], 'Img': imgProducts[i]}
>>>>>>> edab21b0b3498838eff5a8255edae015090aa5bf
    allData.append(dataDic)
print(allData)

