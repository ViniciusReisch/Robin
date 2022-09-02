import arrow
from selenium import webdriver


def MB_Crawl():
    # Memory specific data

    pricesProducts = []             # Memory Prices
    namesProducts = []              # Memory Name
    linksProducts = []              # Memory Links
    imgProducts = []                # Memory Image
    local = arrow.utcnow()          # Scraping date and time
    allData = []                    # Memory all data

    for i in range(1, 8):
        driver = webdriver.Chrome()
        link = f'https://www.kabum.com.br/hardware/placas-mae?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
        driver.get(link)

        # Crawling Products == Image
        product = driver.find_elements('class name', 'imageCard')
        for e in product:
            imgProducts.append(e.get_attribute('src'))

        # Crawling Products == Price
        product = driver.find_elements('class name', 'priceCard')  # Possibles class name = jss191, jss69, jss64, jss201
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
        linksProducts = list(dict.fromkeys(linksProducts))
        driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(pricesProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        dataDic = {'Store': 'Kabum', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'MotherBoard', 'Model': '',
                   'DDR': '', 'Format': ''}
        allData.append(dataDic)
    return allData
