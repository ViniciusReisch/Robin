import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Memória ram 8gb
namesProducts = []
imgProducts = []
allData = []
installmentPriceProducts = []
linksProducts = []
pricesProducts = []

for i in range(10):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/memorias?page='
    driver.get(link + str(page))

    # Crawling Products == Image
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
    driver.execute_script("window.scrollTo(0, 6700);")
    product = driver.find_elements('tag name', 'img')
    for i in product:
        if 'product' in i.get_attribute('src'):  # Only separate images with product in the name
            imgProducts.append(i.get_attribute('src'))
    imgProducts = list(dict.fromkeys(imgProducts))

    # Crawling Products == Price
    product = driver.find_elements('class name', 'jss69')
    for i in product:
        if 'R$' in i.text:
            pricesProducts.append(i.text)

    # Crawling Products == Installment Price
    product = driver.find_elements('class name', 'jss77')
    for i in product:
        if 'R$' in i.text:
            installmentPriceProducts.append(i.text)

    # Crawling Products == Name
    product = driver.find_elements('tag name', 'h2')
    for i in product:
        if i.text == "":
            continue
        namesProducts.append(i.text)

    # Crawling Products == Links
    links = driver.find_elements('tag name', 'a')
    for i in links:
        if 'memoria' in i.get_attribute('href'):
            linksProducts.append(i.get_attribute('href'))
    driver.close()

# Separating data in dictionary for better reading
for i in range(len(installmentPriceProducts)):
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

    # FILTER == 8gb 3200mhz
    data8gb3200mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)

    # FILTER == 8gb 3000mhz
    data8gb3000mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)

    # FILTER == 8gb 3200mhz
    data8gb3200mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)

    # FILTER == 8gb 3200mhz
    data8gb3200mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)

    # FILTER == 8gb 3200mhz
    data8gb3200mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)

    # FILTER == 8gb 3200mhz
    data8gb3200mhz = []
    for data in allData:
        if '(1x8GB)' in data['Name'] and '3200MHz' in data['Name']:
            data8gb3200mhz.append(data)