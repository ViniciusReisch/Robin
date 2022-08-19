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

driver = webdriver.Chrome()
driver.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199&tipo_de_memoria=422')

# IMG
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 1000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 1500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 2000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 2500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 3000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 3500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 4000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 4500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 5000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
imgProducts = list(dict.fromkeys(imgProducts))
driver.execute_script("window.scrollTo(0, 5500);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 6000);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
driver.execute_script("window.scrollTo(0, 6300);")
product = driver.find_elements('tag name', 'img')
for i in product:
    if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
        imgProducts.append(i.get_attribute('src'))
imgProducts = list(dict.fromkeys(imgProducts))

product = driver.find_elements('class name', 'jss69')
for i in product:
    if i.text == "":
        continue
    pricesProducts.append(i.text)

product = driver.find_elements('class name', 'jss77')
for i in product:
    if i.text == "":
        continue
    installmentPriceProducts.append(i.text)

links = driver.find_elements('tag name', 'a')
for i in links:
    if 'memoria' in i.get_attribute('href'):
        linksProducts.append(i.get_attribute('href'))
driver.close()

# Reunindo dados em dictionary
for i in range(len(pricesProducts)):
    if '.' in pricesProducts[i]:
        pricesProducts[i] = pricesProducts[i].replace('.', '')
    changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
    if '.' in installmentPriceProducts[i]:
        installmentPriceProducts[i] = installmentPriceProducts[i].replace('.', '')
    changeableInstallmentPriceProducts = installmentPriceProducts[i].replace('R$', '').replace(',', '.')
    dataDic = {'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
               'Installment price': [installmentPriceProducts[i], float(changeableInstallmentPriceProducts)],
               'Link': linksProducts[i], 'Image': imgProducts[i]}
    allData.append(dataDic)
print(allData)