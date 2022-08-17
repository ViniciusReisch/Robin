import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import re

# Memória ram 8gb
namesProducts = []
imgProducts = []
allData = []
installmentPriceProducts = []
linksProducts = []
pricesProducts = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
response = requests.get("https://www.pichau.com.br/hardware/memorias",
                        headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

for nome in soup.select('.MuiTypography-h6'):
    namesProducts.append(nome.text)

for img in soup.select('.MuiGrid-grid-xl-2:nth-child(9) .jss52 , .jss50'):
    imgProducts.append(soup.get('src'))

for img in soup.findAll('img'):
    imgProducts.append(img.get('src'))

print(imgProducts)

driver = webdriver.Chrome()
driver.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')

produto = driver.find_elements('class name', 'jss69')
for i in produto:
    if i.text == "":
        continue
    pricesProducts.append(i.text)

# produto = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "MuiGrid-grid-xl-2", " " )) and (((count(preceding-sibling::*) + 1) = 9) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "jss52", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "jss50", " " ))]')
# print(produto)
# for i in produto:
#     if i.text == "":
#         continue
#     imgProducts.append(i.text)

xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "jss50", " " ))]'

link_elements = driver.find_elements('xpath', xpath)
for link in link_elements:
    src = link.get_attribute("src")
    print(src)
    imgProducts.append(src)

produto = driver.find_elements('class name', 'jss77')
for i in produto:
    if i.text == "":
        continue
    installmentPriceProducts.append(i.text)

links = driver.find_elements('tag name', 'a')
for i in links:
    if 'memoria' in i.get_attribute('href'):
        linksProducts.append(i.get_attribute('href'))

# linksImg = driver.find_elements('tag name', 'img')
# print(linksImg)
# for i in linksImg:
#     imgProducts.append(i.get_attribute('src'))

# Reunindo dados em dictionary
for i in range(len(pricesProducts)):
    if '.' in pricesProducts[i]:
        pricesProducts[i] = pricesProducts[i].replace('.', '')
    changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
    if '.' in installmentPriceProducts[i]:
        installmentPriceProducts[i] = installmentPriceProducts[i].replace('.', '')
    changeableInstallmentPriceProducts = installmentPriceProducts[i].replace('R$', '').replace(',', '.')
    dataDic = {'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)], 'Installment price': [installmentPriceProducts[i], float(changeableInstallmentPriceProducts)] , 'Link': linksProducts[i]}
    allData.append(dataDic)
print(allData)