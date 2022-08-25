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
Model = {
    'GT 1030 2GB': [],
    'GT 610 2GB': [],
    'GT 710 1GB': [],
    'GT 710 2GB': [],
    'GT 730 2GB': [],
    'GT 730 4GB': [],
    'GT 240 1GB': [],
    'GTX 1050 2GB': [],
    'GTX 1050 3GB': [],
    'GTX 1050 TI 4GB': [],
    'GTX 1060 3GB': [],
    'GTX 1060 6GB': [],
    'GTX 1070 8GB': [],
    'GTX 1070 TI 8GB': [],
    'GTX 1080 8GB': [],
    'GTX 1080 TI 11GB': [],
    'GTX 1630 4GB': [],
    'GTX 1650 4GB': [],
    'GTX 1650 SUPER': [],
    'GTX 1660 6GB': [],
    'GTX 1660 SUPER': [],
    'GTX 1660 TI 6GB': [],
    'GTX 750 TI 2GB': [],
    'GTX 750 TI 4GB': [],
    'GTX 980 TI 6GB': [],
    'NVS 810 4GB': [],
    'PRO W6600 8GB': [],
    'QUADRO P1000 4GB': [],
    'QUADRO P2000 5GB': [],
    'QUADRO P400 2GB': [],
    'QUADRO P4000 8GB': [],
    'QUADRO P620 2GB': [],
    'QUADRO RTX 4000 8GB': [],
    'QUADRO RTX A2000 12GB': [],
    'QUADRO RTX A2000 6GB': [],
    'QUADRO RTX A4000 16GB': [],
    'QUADRO RTX A4500 20GB': [],
    'QUADRO RTX A5000 24GB': [],
    'QUADRO T1000 4GB': [],
    'QUADRO T1000 8GB': [],
    'QUADRO T400 2GB': [],
    'QUADRO T600 4GB': [],
    'R5 220 2GB': [],
    'R5 230 1GB': [],
    'R5 230 2GB': [],
    'R7 240': [],
    'RTX 2060 12GB': [],
    'RTX 2060 6GB': [],
    'RTX 2060 SUPER 8GB': [],
    'RTX 2070 8GB': [],
    'RTX 2070 SUPER 8GB': [],
    'RTX 2080 8GB': [],
    'RTX 2080 SUPER 8GB': [],
    'RTX 2080 TI 11GB': [],
    'RTX 3050 4GB': [],
    'RTX 3050 8GB': [],
    'RTX 3060 12GB': [],
    'RTX 3060 TI 8GB': [],
    'RTX 3070 8GB': [],
    'RTX 3070 TI 8GB': [],
    'RTX 3080 10GB': [],
    'RTX 3080 12GB': [],
    'RTX 3080 TI 12GB': [],
    'RTX 3090 24GB': [],
    'RTX 3090 TI 24 GB': [],
    'RX 460 2GB': [],
    'RX 550 2GB': [],
    'RX 550 4GB': [],
    'RX 5500 4GB': [],
    'RX 5600 XT 6GB': [],
    'RX 570 4GB': [],
    'RX 570 8GB': [],
    'RX 5700 8GB': [],
    'RX 5700 XT 8GB': [],
    'RX 580 4GB': [],
    'RX 580 8GB': [],
    'RX 590 8GB': [],
    'RX 6400 4GB': [],
    'RX 6500 XT 4GB': [],
    'RX 6600 8GB': [],
    'RX 6600 XT 8GB': [],
    'RX 6650 XT 8GB': [],
    'RX 6700 XT 12GB': [],
    'RX 6750 XT 12GB': [],
    'RX 6800 16GB': [],
    'RX 6800 XT 16GB': [],
    'RX 6900 XT 16GB': [],
    'RX 6950 XT 16GB': []
}

VRAM_2gb = {

}

VRAM_4gb = {

}

VRAM_6gb = {

}

VRAM_8gb = {

}

VRAM_10gb = {

}

VRAM_12gb = {

}

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
        product = driver.find_elements('class name', 'jss199')  # Possibles class name = jss199, jss77
        for i in product:
            if 'R$' in i.text:
                installmentPriceProducts.append(i.text)

    # Crawling Products == Name
    product = driver.find_elements('tag name', 'h2')
    for i in product:
        if i.text == "":
            continue
        reformatName = i.text.replace(',', '')  # Some cards are separated by commas as an example [2080TI, 8gb]
        reformatName = reformatName.replace('SUPER', 'Super')
        namesProducts.append(reformatName)

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
allModel = [
    'GT 1030', 'GT 610', 'GT 710 1GB', 'GT 710 2GB', 'GT 730', 'GT 730',
    'GT240', 'GTX 1050 2GB', 'GTX 1050 3GB', 'GTX 1050 TI', 'GTX 1060',
    'GTX 1060', 'GTX 1070', 'GTX 1070 TI', 'GTX 1080', 'GTX 1080 TI',
    'GTX 1630', 'GTX 1650', 'GTX 1650 Super', 'GTX 1660', 'GTX 1660 Super',
    'GTX 1660 TI', 'GTX 750 TI 2GB', 'GTX 750 TI 4GB', 'GTX 980 TI', 'NVS 810',
    'PRO W6600', 'QUADRO P1000', 'QUADRO P2000', 'QUADRO P400', 'QUADRO P4000',
    'QUADRO P620', 'QUADRO RTX 4000', 'QUADRO RTX A2000', 'QUADRO RTX A2000',
    'QUADRO RTX A4000', 'QUADRO RTX A4500', 'QUADRO RTX A5000', 'QUADRO T1000',
    'QUADRO T1000', 'QUADRO T400', 'QUADRO T600', 'R5 220 2GB', 'R5 230 1GB',
    'R5 230 2GB', 'R7 240', 'RTX 2060', 'RTX 2060', 'RTX 2060 Super', 'RTX 2070',
    'RTX 2070 Super', 'RTX 2080', 'RTX 2080 Super', 'RTX 2080 TI', 'RTX 3050',
    'RTX 3050', 'RTX 3060', 'RTX 3060 TI', 'RTX 3070', 'RTX 3070 TI', 'RTX 3080',
    'RTX 3080', 'RTX 3080 TI', 'RTX 3090', 'RTX 3090 TI', 'RX 460', 'RX 550',
    'RX 550', 'RX 5500', 'RX 5600 XT', 'RX 570', 'RX 570', 'RX 5700',
    'RX 5700 XT', 'RX 580', 'RX 580', 'RX 590', 'RX 6400', 'RX 6500 XT',
    'RX 6600', 'RX 6600 XT', 'RX 6650 XT', 'RX 6700 XT', 'RX 6750 XT',
    'RX 6800', 'RX 6800 XT', 'RX 6900 XT', 'RX 6950 XT'
]
key = list(Model.values())
for i in range(len(allModel)):
    for data in allData:
        if allModel[i] in data['Name']:
            key = list(Model.values())
            key[i].append(data)
