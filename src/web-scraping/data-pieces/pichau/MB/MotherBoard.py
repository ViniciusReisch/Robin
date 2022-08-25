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
DDR = {
    "motherBoardDDR5": [],
    "motherBoardDDR4": [],
    "motherBoardDDR3": []
}
Format = {
    "motherBoardATX": [],
    "motherBoardE_ATX": [],
    "motherBoardMicro_ATX": [],
    "motherBoardMini_ITX": []
}
Socket = {
    "motherBoardAM4": [],
    "motherBoardLGA1700": [],
    "motherBoardLGA1200": [],
    "motherBoardLGA1150": [],
    "motherBoardLGA1151": [],
    "motherBoardLGA1155": [],
    "motherBoardFM2": []
}

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
        product = driver.find_elements('class name', 'jss199')  # Possibles class name = jss199, jss77
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
    dataDic = {'Store': 'Pichau', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
               'Installment price': [installmentPriceProducts[i], float(changeableInstallmentPriceProducts)],
               'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
               'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png'}
    allData.append(dataDic)
lostData = 0

# Double Data Rate
allDDR = ['DDR5', 'DDR4', 'DDR3']
key = list(DDR.values())
for i in range(len(allDDR)):
    for data in allData:
        if allDDR[i] in data['Name']:
            key = list(DDR.values())
            key[i].append(data)

# Format
allFormat = ['ATX', 'E-ATX', 'Micro-ATX', 'Mini-ITX']
key = list(Format.values())
for i in range(len(allFormat)):
    for data in allData:
        if allFormat[i] in data['Name']:
            key = list(Format.values())
            key[i].append(data)

# Socket
allSocket = ['AM4', 'LGA1700', 'LGA1200', 'LGA1150', 'LGA1151', 'LGA1155', 'FM2+']
key = list(Socket.values())
for i in range(len(allSocket)):
    for data in allData:
        if allSocket[i] in data['Name']:
            key = list(Socket.values())
            key[i].append(data)
