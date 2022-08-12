import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Memória ram 8gb
namesProducts = []
imgProducts = []
allData = []
linksProducts = []
pricesProducts = []
header = {'user-agent': 'Mozilla/5.0'}
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422",
                        headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

for nome in soup.select('.MuiTypography-h6'):
    namesProducts.append(nome.text)

driver = webdriver.Chrome()
driver.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')
produto = driver.find_elements('class name', 'jss64')

for i in produto:
    if i.text == "":
        continue
    pricesProducts.append(i.text)

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
    allData.append(dataDic)
print(allData)

