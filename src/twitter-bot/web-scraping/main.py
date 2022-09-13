import arrow
from selenium import webdriver

passPricesProducts = []
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
prices = product.find_elements('class name', 'jss145')
passPrices = product.find_elements('class name', 'jss154')
img = product.find_elements('tag name', 'img')
links = product.find_elements('tag name', 'a')

for i in names:
    if i.text == "":
        continue
    namesProducts.append(i.text)

for i in prices:
    if i.text == "":
        continue
    pricesProducts.append(i.text)

for i in passPrices:
    if i.text == "":
        continue
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
    if '.' in pricesProducts[i]:
        pricesProducts[i] = pricesProducts[i].replace('.', '')
    changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
    if '.' in passPricesProducts[i]:
        passPricesProducts[i] = passPricesProducts[i].replace('.', '')
    changeablePassedPrices = passPricesProducts[i].replace('de R$ ', '').replace(',', '.').replace(' por:', '')
    dataDic = {'Store': 'Pichau', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
               'Passed Prices': [passPricesProducts[i], float(changeablePassedPrices)],
               'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss')}
    allData.append(dataDic)
