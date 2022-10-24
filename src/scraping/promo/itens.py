import arrow
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def Crawl_Kabum():
    # Memory specific data

    passPriceProducts = []
    pricesProducts = []
    namesProducts = []
    linksProducts = []
    imgProducts = []
    local = arrow.utcnow()
    allData = []

    for i in range(1, 11):
        driver = webdriver.Chrome()
        link = f'https://www.kabum.com.br/hardware?page_number={i}&page_size=100&facet_filters=eyJoYXNfb2ZmZXIiOlsidHJ1ZSJdfQ==&sort=most_searched'
        driver.get(link)

        # Crawling Products == Image
        product = driver.find_elements('class name', 'imageCard')
        for e in product:
            imgProducts.append(e.get_attribute('src'))

        # Crawling Products == Price
        product = driver.find_elements('class name', 'oldPriceCard')
        for i in product:
            if ',' in i.text:
                passPriceProducts.append(i.text)

        # Crawling Products == Price
        product = driver.find_elements('class name', 'priceCard')
        for i in product:
            if ',' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Name
        product = driver.find_elements('class name', 'nameCard')
        for i in product:
            if i.text == "":
                continue
            namesProducts.append(i.text)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if i.get_attribute('href') is None:
                continue
            if 'produto' in i.get_attribute('href'):  # Only separate images with product in the name
                linksProducts.append(i.get_attribute('href'))
        driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(pricesProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')

        if '.' in passPriceProducts[i]:
            passPriceProducts[i] = passPriceProducts[i].replace('.', '')
        changeablePassedPrices = passPriceProducts[i].replace('R$', '').replace(',', '.')

        discountProduct = ((float(changeablePassedPrices) - float(changeablePrices)) * 100) / float(changeablePassedPrices)
        dataDic = {'Store': 'Kabum', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [0, 0],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://logodownload.org/wp-content/uploads/2017/11/kabum-logo.png',
                   'Type': 'Promo', 'Model': '', 'Format': '', 'Discount': round(discountProduct, 2), 'Old Prices': float(changeablePassedPrices),
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData


def Crawl_Terabyte():

    passPriceProducts = []
    pricesProducts = []
    namesProducts = []
    linksProducts = []
    imgProducts = []
    local = arrow.utcnow()
    allData = []

    # WEB CRAWLER

    driver = webdriver.Chrome()
    link = 'https://www.terabyteshop.com.br/promocoes'
    driver.get(link)

    # Crawling Products == Image
    product = driver.find_elements('tag name', 'img')
    for e in product:
        if 'produto' in e.get_attribute('src'):  # Only separate images with product in the name
            imgProducts.append(e.get_attribute('src'))
    imgProducts = list(dict.fromkeys(imgProducts))

    # Crawling Products == Price
    product = driver.find_elements('class name', 'prod-new-price')  # Possibles class name = jss191, jss69
    for i in product:
        if 'R$' in i.text:
            pricesProducts.append(i.text)

    # Crawling Products == Installment Price
    product = driver.find_elements('class name', 'prod-old-price')  # Possibles class name = jss199, jss77
    for i in product:
        passPriceProducts.append(i.text)

    # Crawling Products == Name
    product = driver.find_elements('tag name', 'h2')
    for i in product:
        if i.text == "":
            continue
        namesProducts.append(i.text)

    # Crawling Products == Links
    links = driver.find_elements('tag name', 'a')
    for i in links:
        if 'produto' in i.get_attribute('href'):
            linksProducts.append(i.get_attribute('href'))
    linksProducts = list(dict.fromkeys(linksProducts))
    driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(pricesProducts)):
        if '.' in passPriceProducts[i]:
            passPriceProducts[i] = passPriceProducts[i].replace('.', '')
        passPriceProducts[i] = passPriceProducts[i].replace('De: R$ ', '').replace(' por:', '').replace(',', '.')
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.').replace(' à vista', '')
        discountProduct = ((float(passPriceProducts[i]) - float(changeablePrices)) * 100) / float(passPriceProducts[i])
        dataDic = {'Store': 'Terabyte', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [0, 0],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://img.terabyteshop.com.br/terabyte-logo.svg', 'Type': 'Promo', 'Model': '',
                   'Format': '',  'Discount': round(discountProduct, 2), 'Old Prices': passPriceProducts[i],
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData
