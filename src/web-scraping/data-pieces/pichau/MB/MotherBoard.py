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

# Specific MotherBoard lists

# Double Data Rate
motherBoardDDR5 = []
motherBoardDDR4 = []
motherBoardDDR3 = []

# Format
motherBoardATX = []
motherBoardE_ATX = []
motherBoardMicro_ATX = []
motherBoardMini_ITX = []

# Socket
motherBoardAM4 = []
motherBoardLGA1700 = []
motherBoardLGA1200 = []
motherBoardLGA1150 = []
motherBoardLGA1151 = []
motherBoardLGA1155 = []
motherBoardFM2 = []

hostIP = socket.gethostname()
IPAddr = socket.gethostbyname(hostIP)
for i in range(3):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/placa-m-e?page='
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
        if 'placa-mae' in i.get_attribute('href'):
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

# Double Data Rate

# FILTER == DDR5
for data in allData:
    if 'DDR5' in data['Name']:
        motherBoardDDR5.append(data)

# FILTER == DDR4
    if 'DDR4' in data['Name']:
        motherBoardDDR4.append(data)

# FILTER == DDR3
    if 'DDR3' in data['Name']:
        motherBoardDDR3.append(data)

# Format

# FILTER == AM4
for data in allData:
    if 'ATX' in data['Name']:
        motherBoardATX.append(data)

# FILTER == E-ATX
    if 'E-ATX' in data['Name']:
        motherBoardE_ATX.append(data)

# FILTER == Micro-ATX
    if 'M-ATX' in data['Name']:
        motherBoardMicro_ATX.append(data)

# FILTER == Mini-ITX
    if 'mini-ITX' in data['Name']:
        motherBoardMini_ITX.append(data)

# Socket

# FILTER == ATX
for data in allData:
    if 'AM4' in data['Name']:
        motherBoardAM4.append(data)

# FILTER == LGA1700
    if 'LGA1700' in data['Name']:
        motherBoardLGA1700.append(data)

# FILTER == LGA1200
    if 'LGA1200' in data['Name']:
        motherBoardLGA1200.append(data)

# FILTER == LGA1150
    if 'LGA1150' in data['Name']:
        motherBoardLGA1150.append(data)

# FILTER == LGA1151
    if 'LGA1151' in data['Name']:
        motherBoardLGA1151.append(data)

# FILTER == LGA1155
    if 'LGA1155' in data['Name']:
        motherBoardLGA1155.append(data)

# FILTER == FM2
    if 'FM2+' in data['Name']:
        motherBoardFM2.append(data)