import arrow
from selenium import webdriver

# Memory specific data

installmentPriceProducts = []  # Memory Installment Prices
pricesProducts = []  # Memory Prices
namesProducts = []  # Memory Name
linksProducts = []  # Memory Links
imgProducts = []  # Memory Image
allData = []  # Memory all data
local = arrow.utcnow()

# Specific memory lists

# Double Data Rate
memoryDDR5 = []
memoryDDR4 = []
memoryDDR3 = []

# Capacity

# DDR5
memoryDDR5_8gb = []
memoryDDR5_16gb = []
memoryDDR5_32gb = []

# DDR4
memoryDDR4_4gb = []
memoryDDR4_8gb = []
memoryDDR4_16gb = []
memoryDDR4_32gb = []

# DDR3
memoryDDR3_4gb = []
memoryDDR3_8gb = []
memoryDDR3_16gb = []
memoryDDR3_32gb = []

# Frequency

# 4gb List
# 4gb and DDR4
memoryDDR4_4gb_2400Mhz = []
memoryDDR4_4gb_1600Mhz = []

# 4gb and DDR3
memoryDDR3_4gb_1600Mhz = []
memoryDDR3_4gb_1333Mhz = []

# 8gb List
# 8gb and DDR4
memoryDDR4_8gb_3200Mhz = []
memoryDDR4_8gb_3000Mhz = []
memoryDDR4_8gb_2666Mhz = []

# 8gb and DDR3
memoryDDR3_8gb_1600Mhz = []
memoryDDR3_8gb_1866Mhz = []

# 16gb List
# 16gb and DDR4
memoryDDR4_16gb_3600Mhz = []
memoryDDR4_16gb_3200Mhz = []
memoryDDR4_16gb_3000Mhz = []
memoryDDR4_16gb_2666Mhz = []

# 16gb and DDR3
memoryDDR3_16gb_1600Mhz = []
memoryDDR3_16gb_1866Mhz = []

# 16gb and DDR5
memoryDDR5_16gb_4800Mhz = []

# 32gb List
# 32gb and DDR4
memoryDDR4_32gb_3600Mhz = []
memoryDDR4_32gb_3200Mhz = []
memoryDDR4_32gb_3000Mhz = []
memoryDDR4_32gb_2666Mhz = []

# 32gb and DDR3
memoryDDR3_32gb_1600Mhz = []

# 32gb and DDR5
memoryDDR5_32gb_5600Mhz = []
memoryDDR5_32gb_6000Mhz = []

for i in range(9):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/memorias?page='
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
    product = driver.find_elements('class name', 'jss191')  # Possibles class name = jss191
    for i in product:
        if 'R$' in i.text:
            pricesProducts.append(i.text)

    # Crawling Products == Installment Price
    product = driver.find_elements('class name', 'jss199')  # Possibles class name = jss199
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
        if 'memoria' in i.get_attribute('href'):
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
        memoryDDR5.append(data)

# FILTER == DDR4
    if 'DDR4' in data['Name']:
        memoryDDR4.append(data)

# FILTER == DDR3
    if 'DDR3' in data['Name']:
        memoryDDR3.append(data)

# Capacity / DDR5

# FILTER == 8gb
for data in memoryDDR5:
    if '8GB' in data['Name']:
        memoryDDR5_8gb.append(data)

# FILTER == 16gb
    if '16GB' in data['Name']:
        memoryDDR5_16gb.append(data)

# FILTER == 32gb
    if '32GB' in data['Name']:
        memoryDDR5_32gb.append(data)

    else:
        lostData += 1

# Capacity / DDR4

# FILTER == 4gb
for data in memoryDDR4:
    if '4GB' in data['Name']:
        memoryDDR4_4gb.append(data)

# FILTER == 8gb
    if '8GB' in data['Name']:
        memoryDDR4_8gb.append(data)

# FILTER == 16gb
    if '16GB' in data['Name']:
        memoryDDR4_16gb.append(data)

# FILTER == 32gb
    if '32GB' in data['Name']:
        memoryDDR4_32gb.append(data)

    else:
        lostData += 1

# Capacity / DDR3

# FILTER == 4gb
for data in memoryDDR3:
    if '4GB' in data['Name']:
        memoryDDR3_4gb.append(data)

# FILTER == 8gb
    if '8GB' in data['Name']:
        memoryDDR3_8gb.append(data)

# FILTER == 16gb
    if '16GB' in data['Name']:
        memoryDDR3_16gb.append(data)

# FILTER == 32gb
    if '32GB' in data['Name']:
        memoryDDR3_32gb.append(data)

    else:
        lostData += 1

# Frequency / DDR5

# FILTER == 16gb
for data in memoryDDR5_16gb:  # 4800Mhz 16gb DDR5
    if '4800MHz' in data['Name']:
        memoryDDR5_16gb_4800Mhz.append(data)

# FILTER == 32gb
for data in memoryDDR5_32gb:
    if '5600MHz' in data['Name']:  # 5600Mhz 32gb DDR5
        memoryDDR5_32gb_5600Mhz.append(data)
    if '6000MHz' in data['Name']:  # 6000Mhz 32gb DDR5
        memoryDDR5_32gb_6000Mhz.append(data)

# Frequency / DDR4

# FILTER == 4gb
for data in memoryDDR4_4gb:
    if '2400MHz' in data['Name']:  # 2600Mhz 4gb DDR4
        memoryDDR4_4gb_2400Mhz.append(data)
    if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR4
        memoryDDR4_4gb_1600Mhz.append(data)

# FILTER == 8gb
for data in memoryDDR4_8gb:
    if '2666MHz' in data['Name']:  # 2666MHz 8gb DDR4
        memoryDDR4_8gb_2666Mhz.append(data)
    if '3000MHz' in data['Name']:  # 3000MHz 8gb DDR4
        memoryDDR4_8gb_3000Mhz.append(data)
    if '3200MHz' in data['Name']:  # 3200MHz 8gb DDR4
        memoryDDR4_8gb_3200Mhz.append(data)

# FILTER == 16gb
for data in memoryDDR4_16gb:
    if '2666MHz' in data['Name']:  # 2666MHz 16gb DDR4
        memoryDDR4_16gb_2666Mhz.append(data)
    if '3600MHz' in data['Name']:  # 3600MHz 16gb DDR4
        memoryDDR4_16gb_3600Mhz.append(data)
    if '3000MHz' in data['Name']:  # 3000MHz 16gb DDR4
        memoryDDR4_16gb_3000Mhz.append(data)
    if '3200MHz' in data['Name']:  # 3200MHz 16gb DDR4
        memoryDDR4_16gb_3200Mhz.append(data)

# FILTER == 32gb
for data in memoryDDR4_32gb:
    if '2666MHz' in data['Name']:  # 5600Mhz 32gb DDR4
        memoryDDR4_32gb_2666Mhz.append(data)
    if '3600MHz' in data['Name']:  # 5600Mhz 32gb DDR4
        memoryDDR4_32gb_3600Mhz.append(data)
    if '3000MHz' in data['Name']:  # 5600Mhz 32gb DDR4
        memoryDDR4_32gb_3000Mhz.append(data)
    if '3200MHz' in data['Name']:  # 5600Mhz 32gb DDR4
        memoryDDR4_32gb_3200Mhz.append(data)

# Frequency / DDR3

# FILTER == 4gb
for data in memoryDDR3_4gb:
    if '2400MHz' in data['Name']:  # 2400MHz 4gb DDR3
        memoryDDR3_4gb_1600Mhz.append(data)
    if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR3
        memoryDDR3_4gb_1333Mhz.append(data)

# FILTER == 8gb
for data in memoryDDR3_8gb:
    if '1600MHz' in data['Name']:  # 1600MHz 8gb DDR3
        memoryDDR3_8gb_1600Mhz.append(data)
    if '1866MHz' in data['Name']:  # 1866MHz 8gb DDR3
        memoryDDR3_8gb_1866Mhz.append(data)

# FILTER == 16gb
for data in memoryDDR3_16gb:
    if '1600MHz' in data['Name']:  # 1600MHz 16gb DDR3
        memoryDDR3_16gb_1600Mhz.append(data)
    if '1866MHz' in data['Name']:  # 1866MHz 16gb DDR3
        memoryDDR3_16gb_1866Mhz.append(data)

# FILTER == 32gb
for data in memoryDDR3_32gb:
    if '1600MHz' in data['Name']:  # 1600MHz 32gb DDR3
        memoryDDR3_32gb_1600Mhz.append(data)
