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

produto = driver.find_elements('tag name', 'h2')
for i in produto:
    if i.text == "":
        continue
    namesProducts.append(i.text)

produto = driver.find_elements('tag name', 'span')
for i in produto:
    if i.text == "":
        continue
    pricesProducts.append(i.text)
