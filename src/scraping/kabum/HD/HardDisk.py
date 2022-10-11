import arrow
from selenium import webdriver


def HD_Crawl():
    # HardDisk specific data

    pricesProducts = []             # HardDisk Prices
    namesProducts = []              # HardDisk Name
    linksProducts = []              # HardDisk Links
    imgProducts = []                # HardDisk Image
    local = arrow.utcnow()          # Scraping date and time
    allData = []                    # HardDisk all data

    driver = webdriver.Chrome()
    link = f'https://www.kabum.com.br/hardware/disco-rigido-hd?page_number=1&page_size=100&facet_filters=eyJQb3J0w6F0aWwiOlsiTsOjbyJdfQ==&sort=most_searched'
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
        if 'hd' in i.get_attribute('href') and 'produto' in i.get_attribute(
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
                   'Logo': 'https://upload.wikimedia.org/wikipedia/commons/7/71/KaBuM%21_Logo2015.png', 'Type': 'HardDisk', 'Model': '', 'Format': '',
                   'Discount': '', 'Old Prices': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData