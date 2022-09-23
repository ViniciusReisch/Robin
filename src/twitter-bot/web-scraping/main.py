import arrow
from selenium import webdriver

passPricesProducts = []
priceTag = 0
passPriceTag = 0
pricesProducts = []             # Memory Prices
namesProducts = []              # Memory Name
linksProducts = []              # Memory Links
imgProducts = []                # Memory Image
local = arrow.utcnow()          # Scraping date and time
allData = []                    # Memory all data
driver = webdriver.Chrome()
link = f'https://www.pichau.com.br/'
driver.get(link)
height = driver.execute_script("return document.body.scrollHeight")
scroll = 0
driver.fullscreen_window()

# Crawling Products == Name
product = driver.find_element('class name', 'jss59')
names = product.find_elements('class name', 'MuiTypography-h6')

prices = product.find_elements('class name', 'jss145')  # jss224, jss145
priceTagList = ['jss224', 'jss139', 'jss212']
while len(prices) == 0:
    prices = product.find_elements('class name', priceTagList[priceTag])
    priceTag += 1

passPrices = product.find_elements('class name', 'jss154')  # jss233, jss154
passPriceTagList = ['jss233', 'jss148', 'jss221']
while len(passPrices) == 0:
    passPrices = product.find_elements('class name', passPriceTagList[passPriceTag])
    passPriceTag += 1

img = product.find_elements('tag name', 'img')
links = product.find_elements('tag name', 'a')

for i in names:
    namesProducts.append(i.text)

for i in prices:
    pricesProducts.append(i.text)

for i in passPrices:
    passPricesProducts.append(i.text)

while scroll < height:
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    img = product.find_elements('tag name', 'img')
    for e in img:
        if 'product' in e.get_attribute('src'):  # Only separate images with product in the name
            imgProducts.append(e.get_attribute('src'))
    scroll += 200
imgProducts = list(dict.fromkeys(imgProducts))

for i in links:
    linksProducts.append(i.get_attribute('href'))

for i in range(len(pricesProducts)):
    if passPricesProducts[i] is not None:
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        if '.' in passPricesProducts[i]:
            passPricesProducts[i] = passPricesProducts[i].replace('.', '')
        changeablePassedPrices = passPricesProducts[i].replace('de R$ ', '').replace(',', '.').replace(' por:', '')
        discountProduct = ((float(changeablePassedPrices) - float(changeablePrices)) * 100) / float(changeablePassedPrices)
    dataDic = {'Store': 'Pichau', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
               'Passed Prices': [passPricesProducts[i], float(changeablePassedPrices)],
               'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
               'Discount': str(round(discountProduct, 2)) + '%'}
    text = f'{namesProducts[i]} com desconto de {str(round(discountProduct, 2))}% de R${changeablePassedPrices} por R${changeablePrices}'
    print(text)

    allData.append(dataDic)
driver.close()
