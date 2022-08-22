import arrow
from selenium import webdriver
import socket

# MotherBoard specific data

installmentPriceProducts = []  # Memory Installment Prices
pricesProducts = []  # Memory Prices
namesProducts = []  # Memory Name
linksProducts = []  # Memory Links
imgProducts = []  # Memory Image
allData = []  # Memory all data
local = arrow.utcnow()

# Specific CPU lists1

# Platform and integrate GPU

# AMD
cpuAMD = []
apuAMD = []

# Intel
cpuIntel = []
apuIntel = []

# Socket
cpuAM4 = []  # AMD AM4 and AMD AM4G
cpuFM2 = []  # FM2+
cpuLGA1150 = []  # LGA1150
cpuLGA1151 = []  # LGA1151
cpuLGA1200 = []  # LGA1200
cpuLGA1700 = []  # LGA1700
cpuLGA2066 = []  # LGA2066

hostIP = socket.gethostname()
IPAddr = socket.gethostbyname(hostIP)
for i in range(2):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/processadores?page='
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
    if IPAddr == '192.168.2.38':  # Id verification
        product = driver.find_elements('class name', 'jss69')  # Possibles class name = jss191, jss69
        for i in product:
            if 'R$' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Installment Price
        product = driver.find_elements('class name', 'jss77')  # Possibles class name = jss199, jss77
        for i in product:
            if 'R$' in i.text:
                installmentPriceProducts.append(i.text)
    else:  # Different ID

        # Crawling Products == Price
        product = driver.find_elements('class name', 'jss191')  # Possibles class name = jss191, jss69
        for i in product:
            if 'R$' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Installment Price
        product = driver.find_elements('class name', 'jss69')  # Possibles class name = jss199, jss77
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
        if 'processador' in i.get_attribute('href'):
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
               'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
               'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png'}
    allData.append(dataDic)
lostData = 0

# Platform

# AMD
# FILTER == AMD APU integrate GPU
for data in allData:
    if 'AMD' in data['Name']:
        if '0G' in data['Name'] or '0GE' in data['Name'] or 'FM2+' in data['Name']:
            apuAMD.append(data)

        # FILTER == AMD CPU without GPU
        else:
            cpuAMD.append(data)

# Intel
# FILTER == Intel CPU without GPU
for data in allData:
    if 'Intel' in data['Name']:
        if '5F' in data['Name'] or '0KF' in data['Name'] or '0X' in data['Name'] or '0F' in data['Name']:
            cpuIntel.append(data)

        # FILTER == Intel APU integrate GPU
        else:
            apuIntel.append(data)

# Socket

# FILTER == AMD AM4 and AMD AM4G
for data in allData:
    if 'AM4' in data['Name']:
        cpuAM4.append(data)

    # FILTER == FM2+
    if 'FM2+' in data['Name']:
        cpuFM2.append(data)

    # FILTER == LGA1150
    if 'LGA1150' in data['Name']:
        cpuLGA1150.append(data)

    # FILTER == LGA1151
    if 'LGA1151' in data['Name']:
        cpuLGA1151.append(data)

    # FILTER == LGA1200
    if 'LGA1200' in data['Name']:
        cpuLGA1200.append(data)

    # FILTER == LGA1700
    if 'LGA1700' in data['Name']:
        cpuLGA1700.append(data)

    # FILTER == LGA2066
    if 'LGA2066' in data['Name']:
        cpuLGA2066.append(data)
