import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Memory specific data

installmentPriceProducts = []  # Memory Installment Prices
pricesProducts = []  # Memory Prices
namesProducts = []  # Memory Name
linksProducts = []  # Memory Links
imgProducts = []  # Memory Image
allData = []  # Memory all data

# Specific memory lists

# Double Data Rate
memoryDDR5 = []
memoryDDR4 = []
memoryDDR3 = []

# Capacity

# DDR5
memoryDDR5_8gb = []
memoryDDR5_16gb = []
memoryDDR5_32gb = []

# DDR4
memoryDDR4_4gb = []
memoryDDR4_8gb = []
memoryDDR4_16gb = []
memoryDDR4_32gb = []

# DDR3
memoryDDR3_4gb = []
memoryDDR3_8gb = []
memoryDDR3_16gb = []
memoryDDR3_32gb = []

# Frequency

# 8gb List
# 8gb and DDR4
memoryDDR4_8gb_3200Mhz = []
memoryDDR4_8gb_3000Mhz = []
memoryDDR4_8gb_2666Mhz = []

# 8gb and DDR3
memoryDDR3_8gb_1600Mhz = []
memoryDDR3_8gb_1866Mhz = []

# 16gb List
# 16gb and DDR4
memoryDDR4_16gb_3600Mhz = []
memoryDDR4_16gb_3200Mhz = []
memoryDDR4_16gb_3000Mhz = []
memoryDDR4_16gb_2666Mhz = []

# 16gb and DDR3
memoryDDR3_16gb_1600Mhz = []
memoryDDR3_16gb_1866Mhz = []

# 16gb and DDR5
memoryDDR5_16gb_4800Mhz = []

# 32gb List
# 32gb and DDR4
memoryDDR4_32gb_3600Mhz = []
memoryDDR4_32gb_3200Mhz = []
memoryDDR4_32gb_3000Mhz = []
memoryDDR4_32gb_2666Mhz = []

# 32gb and DDR3
memoryDDR3_32gb_1600Mhz = []

# 32gb and DDR5
memoryDDR5_32gb_5600Mhz = []
memoryDDR5_32gb_6000Mhz = []


for i in range(10):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/memorias?page='
    new_link = link + str(page)
    driver.get(new_link)
    height = driver.execute_script("return document.body.scrollHeight")
    scroll = 0
    driver.fullscreen_window()

    # Crawling Products == Image
    product = driver.find_elements('tag name', 'img')
    for e in product:
        if 'product' in e.get_attribute('src'):  # Only separate images with product in the name
            imgProducts.append(e.get_attribute('src'))
    while scroll < height:
        driver.execute_script(f"window.scrollTo(0, {scroll});")
        product = driver.find_elements('tag name', 'img')
        for e in product:
            if 'product' in e.get_attribute('src'):  # Only separate images with product in the name
                imgProducts.append(e.get_attribute('src'))
        scroll += 200
    imgProducts = list(dict.fromkeys(imgProducts))

    # Crawling Products == Price
    product = driver.find_elements('class name', 'jss191')  # Possibles class name = jss191
    for i in product:
        if 'R$' in i.text:
            pricesProducts.append(i.text)

    # Crawling Products == Installment Price
    product = driver.find_elements('class name', 'jss199')  # Possibles class name = jss199
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

    # Double Data Rate

    # FILTER == DDR5
    for data in allData:
        if 'DDR5' in data['Name']:
            memoryDDR5.append(data)
            memoryDDR5 = list(dict.fromkeys(memoryDDR5))
            
    # FILTER == DDR4
    for data in allData:
        if 'DDR4' in data['Name']:
            memoryDDR4.append(data)
            memoryDDR4 = list(dict.fromkeys(memoryDDR4))

    # FILTER == DDR3
    for data in allData:
        if 'DDR3' in data['Name']:
            memoryDDR3.append(data)
            memoryDDR4 = list(dict.fromkeys(memoryDDR4))
            
    # Capacity

    # DDR5
    # FILTER == 8gb



