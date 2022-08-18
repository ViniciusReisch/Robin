import requests
from bs4 import BeautifulSoup
from selenium import webdriver

namesProducts = []
imgProducts = []
allData = []
installmentPriceProducts = []
linksProducts = []
pricesProducts = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
response = requests.get("https://www.terabyteshop.com.br/hardware/memorias/ddr4",
                        headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

driver = webdriver.Chrome()
driver.get('https://www.terabyteshop.com.br/hardware/memorias/ddr4')

product = driver.find_elements('tag name', 'h2')
for i in product:
    if i.text == "":
        continue
    namesProducts.append(i.text)

product = driver.find_elements('class name', 'prod-new-price')
for i in product:
    if i.text == "":
        continue
    pricesProducts.append(i.text)

product = driver.find_elements('class name', 'commerce_columns_item_image')
for i in product:
    linksProducts.append(i.get_attribute('href'))
linksProducts = list(dict.fromkeys(linksProducts))
linksProducts.remove(None)

product = driver.find_elements('tag name', 'img')
for i in product:
    if 'produto' in i.get_attribute('src'):
        imgProducts.append(i.get_attribute('src'))

for i in range(len(pricesProducts)):
    pricesProducts[i] = pricesProducts[i].replace(' à vista', '')
    if '.' in pricesProducts[i]:
        pricesProducts[i] = pricesProducts[i].replace('.', '')
    changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
    dataDic = {'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)], 'Links': linksProducts[i], 'Images': imgProducts[i]}
    allData.append(dataDic)
print(allData)