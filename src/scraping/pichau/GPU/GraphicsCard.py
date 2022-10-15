import arrow
from selenium import webdriver
import socket


# Graphic Board
def GPU_Crawl():
    # Graphic Card specific data

    installmentPriceProducts = []           # Graphic Card Installment Prices
    pricesProducts = []                     # Graphic Card Prices
    namesProducts = []                      # Graphic Card Name
    linksProducts = []                      # Graphic Card Links
    imgProducts = []                        # Graphic Card Image
    local = arrow.utcnow()                  # Scraping date and time
    hostIP = socket.gethostname()           # IP Local
    IPAddr = socket.gethostbyname(hostIP)   # Specif IP
    allData = []                            # Memory all data

    for i in range(1):
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
        product = driver.find_elements('class name', 'jss193')
        for i in product:
            if 'R$' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Installment Price
        product = driver.find_elements('class name', 'jss201')
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
            if 'placa-de-video-' in i.get_attribute('href'):
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
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'GPU',  'Model': '', 'Format': '',
                   'Discount': '', 'Old Prices': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData
