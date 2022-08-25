import arrow
from selenium import webdriver
import socket

# Graphic Card specific data

installmentPriceProducts = []  # Memory Installment Prices
pricesProducts = []  # Memory Prices
namesProducts = []  # Memory Name
linksProducts = []  # Memory Links
imgProducts = []  # Memory Image
allData = []  # Memory all data
local = arrow.utcnow()

# Specific Graphic Card lists

# Graphic Board

hostIP = socket.gethostname()
IPAddr = socket.gethostbyname(hostIP)
for i in range(5):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/placa-de-video?page='
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
        if 'placa-de-video' in i.get_attribute('href'):
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
    dataDic = {'Store': 'Pichau', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
               'Installment price': [installmentPriceProducts[i], float(changeableInstallmentPriceProducts)],
               'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
               'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png'}
    allData.append(dataDic)
lostData = 0

# Graphic Board

# FILTER == GT 1030 2GB
for data in allData:
    if 'GT 1030 2GB' in data['Name']:
        motherBoardDDR5.append(data)

# FILTER == GT 610 2GB
    if 'GT 610 2GB' in data['Name']:
        motherBoardDDR4.append(data)

# FILTER == GT 710 1GB
    if 'GT 710 1GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GT 710 2GB
    if 'GT 710 2GB' in data['Name']:
        motherBoardDDR5.append(data)

# FILTER == GT 730 2GB
    if 'GT 730 2GB' in data['Name']:
        motherBoardDDR4.append(data)

# FILTER == GT 730 4GB
    if 'GT 730 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GT240 1GB
    if 'GT240 1GB' in data['Name']:
        motherBoardDDR5.append(data)

# FILTER == GTX 1050 2Gb
    if 'GTX 1050 2Gb' in data['Name']:
        motherBoardDDR4.append(data)

# FILTER == GTX 1050 3GB
    if 'GTX 1050 3GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1050 Ti 4Gb
    if 'GTX 1050 Ti 4Gb' in data['Name']:
        motherBoardDDR5.append(data)

# FILTER == GTX 1060 3GB
    if 'GTX 1060 3GB' in data['Name']:
        motherBoardDDR4.append(data)

# FILTER == GTX 1060 6GB
    if 'GTX 1060 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1070 8GB
    if 'GTX 1070 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1070 Ti 8GB
    if 'GTX 1070 Ti 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1080 8GB
    if 'GTX 1080 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1080 Ti 11GB
    if 'GTX 1080 Ti 11GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1630 4GB
    if 'GTX 1630 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1650 4GB
    if 'GTX 1650 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1630 4GB
    if 'GTX 1650 Super' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1660 6GB
    if 'GTX 1660 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1660 Super
    if 'GTX 1660 Super' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 1660 TI 6GB
    if 'GTX 1660 TI 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 750 Ti 2GB
    if 'GTX 750 Ti 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 750 Ti 4GB
    if 'GTX 750 Ti 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == GTX 980 TI 6GB
    if 'GTX 980 TI 6GBB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == NVS 810 4GB
    if 'NVS 810 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == PRO W6600 8GB
    if 'PRO W6600 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro P1000 4GB
    if 'Quadro P1000 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro P2000 5GB
    if 'Quadro P2000 5GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro P400 2GB
    if 'Quadro P400 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro P4000 8GB
    if 'Quadro P4000 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro P620 2GB
    if 'Quadro P620 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX 4000 8GB
    if 'Quadro RTX 4000 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX A2000 12GB
    if 'Quadro RTX A2000 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX A2000 6GB
    if 'Quadro RTX A2000 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX A4000 16GB
    if 'Quadro RTX A4000 16GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX A4500 16GB
    if 'Quadro RTX A4500 16GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro RTX A5000 24GB
    if 'Quadro RTX A5000 24GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro T1000 4GB
    if 'Quadro T1000 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro T1000 8GB
    if 'Quadro T1000 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro T400 2GB
    if 'Quadro T400 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == Quadro T600 4GB
    if 'Quadro T600 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == R5 220 2GB
    if 'R5 220 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == R5 230 1GB
    if 'R5 230 1GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == R5 230 2GB
    if 'R5 230 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == R7 240
    if 'R7 240' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2060 12GB
    if 'RTX 2060 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2060 6GB
    if 'RTX 2060 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2060 SUPER 8GB
    if 'RTX 2060 SUPER 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2070 8GB
    if 'RTX 2070 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2070 SUPER 8GB
    if 'RTX 2070 SUPER 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2080 8GB
    if 'RTX 2080 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2080 SUPER 8GB
    if 'RTX 2080 SUPER 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 2080 Ti 11GB
    if 'RTX 2080 Ti 11GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3050 4GB
    if 'RTX 3050 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3050 8GB
    if 'RTX 3050 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3060 12GB
    if 'RTX 3060 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3060 TI 8GB
    if 'RTX 3060 TI 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3070 8GB
    if 'RTX 3070 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3070 Ti 8GB
    if 'RTX 3070 Ti 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3080 10GB
    if 'RTX 3080 10GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3080 12GB
    if 'RTX 3080 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3080 TI 12GB
    if 'RTX 3080 TI 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3090 24GB
    if 'RTX 3090 24GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RTX 3090 TI 24GB
    if 'RTX 3090 TI 24GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 460 2GB
    if 'RX 460 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 550 2GB
    if 'RX 550 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 550 4GB
    if 'RX 550 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 5500 4GB
    if 'RX 5500 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 5500 XT 4GB
    if 'RX 5500 XT 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 5500 XT 8GB
    if 'RX 5500 XT 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 560 2GB
    if 'RX 560 2GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 560 4GB
    if 'RX 560 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RRX 5600 XT 6GB
    if 'RX 5600 XT 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 570 4GB
    if 'RX 570 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 570 8GB
    if 'RX 570 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 5700 8GB
    if 'RX 5700 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 5700 XT 8GB
    if 'RX 5700 XT 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 580 4GB
    if 'RX 580 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 580 8GB
    if 'RX 580 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 590 8GB
    if 'RX 590 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 560 4GB
    if 'RX 560 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6400 4GB
    if 'RX 5600 XT 6GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6500 XT 4GB
    if 'RX 6500 XT 4GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6600 8GB
    if 'RX 6600 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6600 XT 8GB
    if 'RX 6600 XT 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6650 XT 8GB
    if 'RX 6650 XT 8GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6700 XT 12GB
    if 'RX 6700 XT 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6750 XT 12GB
    if 'RX 6750 XT 12GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6800 16GB
    if 'RX 6800 16GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6800 XT 16GB
    if 'RX 6800 XT 16GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6900 XT 16GB
    if 'RX 6900 XT 16GB' in data['Name']:
        motherBoardDDR3.append(data)

# FILTER == RX 6950 XT 16GB
    if 'RX 6950 XT 16GB' in data['Name']:
        motherBoardDDR3.append(data)
