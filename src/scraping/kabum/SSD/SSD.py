import arrow
from selenium import webdriver


def SSD_Crawl():
    # SSD specific data

    pricesProducts = []             # SSD Prices
    namesProducts = []              # SSD Name
    linksProducts = []              # SSD Links
    imgProducts = []                # SSD Image
    local = arrow.utcnow()          # Scraping date and time
    allData = []                    # SSD all data

    driver = webdriver.Chrome()
    link = f'https://www.kabum.com.br/hardware/ssd-2-5/ssd-m-2-sata?page_number=1&page_size=100&facet_filters=&sort=most_searched'
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
        j = i.text.replace('"', '')
        namesProducts.append(j)

    # Crawling Products == Links
    links = driver.find_elements('tag name', 'a')
    for i in links:
        if i.get_attribute('href') is None:
            continue
        if 'ssd' in i.get_attribute('href') and 'produto' in i.get_attribute(
                'href'):  # Only separate images with product in the name
            linksProducts.append(i.get_attribute('href'))
    driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(pricesProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        dataDic = {'Store': 'Kabum', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [0, 0],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'SSD', 'Model': '', 'Format': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)

    for i in range(1, 4):
        driver = webdriver.Chrome()
        link = f'https://www.kabum.com.br/hardware/ssd-2-5/ssd-pcie-nvme?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
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
            j = i.text.replace('"', '')
            namesProducts.append(j)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if i.get_attribute('href') is None:
                continue
            if 'ssd' in i.get_attribute('href') and 'produto' in i.get_attribute(
                    'href'):  # Only separate images with product in the name
                linksProducts.append(i.get_attribute('href'))
        driver.close()

    for i in range(1, 4):
        driver = webdriver.Chrome()
        link = f'https://www.kabum.com.br/hardware/ssd-2-5/ssd-sata?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
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
            j = i.text.replace('"', '')
            namesProducts.append(j)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if i.get_attribute('href') is None:
                continue
            if 'ssd' in i.get_attribute('href') and 'produto' in i.get_attribute(
                    'href'):  # Only separate images with product in the name
                linksProducts.append(i.get_attribute('href'))
        driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(pricesProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        dataDic = {'Store': 'Kabum', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [0, 0],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'SSD','Model': '', 'Format': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)

    return allData

