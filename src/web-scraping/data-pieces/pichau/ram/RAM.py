import arrow
from selenium import webdriver
import socket
from time import sleep

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
DDR = {
    "memoryDDR5": [],
    "memoryDDR4": [],
    "memoryDDR3": []
}

# Capacity
capacityDDR5 = {
        "8gb": [],
        "16gb": [],
        "32gb": []
    }
capacityDDR4 = {
    "4gb": [],
    "8gb": [],
    "16gb": [],
    "32gb": []
}
capacityDDR3 = {
        "4gb": [],
        "8gb": [],
        "16gb": [],
        "32gb": []
    }

# Frequency
frequencyDDR5 = {
    # 16gb and DDR5
    "8gb_48000Mhz": [],

    # 16gb and DDR5
    "16gb_4800Mhz": [],

    # 32gb and DDR5
    "32gb_5600Mhz": [],
    "32gb_6000Mhz": []
}
frequencyDDR4 = {
    # 4gb List
    # 4gb and DDR4
    "memoryDDR4_4gb_2400Mhz": [],
    "memoryDDR4_4gb_1600Mhz": [],

    # 4gb and DDR3
    "memoryDDR3_4gb_1600Mhz": [],
    "memoryDDR3_4gb_1333Mhz": [],

    # 8gb List
    # 8gb and DDR4
    "memoryDDR4_8gb_3200Mhz": [],
    "memoryDDR4_8gb_3000Mhz": [],
    "memoryDDR4_8gb_2666Mhz": [],

    # 8gb and DDR3
    "memoryDDR3_8gb_1600Mhz": [],
    "memoryDDR3_8gb_1866Mhz": [],

    # 16gb List
    # 16gb and DDR4
    "memoryDDR4_16gb_3600Mhz": [],
    "memoryDDR4_16gb_3200Mhz": [],
    "memoryDDR4_16gb_3000Mhz": [],
    "memoryDDR4_16gb_2666Mhz": [],

    # 16gb and DDR3
    "memoryDDR3_16gb_1600Mhz": [],
    "memoryDDR3_16gb_1866Mhz": [],



    # 32gb List
    # 32gb and DDR4
    "memoryDDR4_32gb_3600Mhz": [],
    "memoryDDR4_32gb_3200Mhz": [],
    "memoryDDR4_32gb_3000Mhz": [],
    "memoryDDR4_32gb_2666Mhz": [],

    # 32gb and DDR3
    "memoryDDR3_32gb_1600Mhz": [],


}
hostIP = socket.gethostname()
IPAddr = socket.gethostbyname(hostIP)
for i in range(10):
    driver = webdriver.Chrome()
    page = i + 1
    link = 'https://www.pichau.com.br/hardware/memorias?page='
    new_link = link + str(page)
    driver.get(new_link)
    height = driver.execute_script("return document.body.scrollHeight")
    scroll = 0
    driver.fullscreen_window()
    sleep(5)
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
    if IPAddr == '192.168.2.38' or IPAddr == '192.168.2.75':  # Id verification
        product = driver.find_elements('class name', 'jss64')  # Possibles class name = jss191, jss69, jss64
        for i in product:
            if 'R$' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Installment Price
        product = driver.find_elements('class name', 'jss72')  # Possibles class name = jss199, jss77, jss72
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

# Double Data Rate
allDDR = ['DDR5', 'DDR4', 'DDR3']
key = list(DDR.values())
for i in range(len(allDDR)):
    for data in allData:
        if allDDR[i] in data['Name']:
            key = list(DDR.values())
            key[i].append(data)

# Capacity / DDR5
allCapacity = ['8GB', '16GB', '32GB']
key = list(capacityDDR5.values())
for i in range(len(allCapacity)):
    for data in DDR['memoryDDR5']:
        if allCapacity[i] in data['Name']:
            key = list(capacityDDR5.values())
            key[i].append(data)

# Capacity / DDR4
allCapacity = ['4GB', '8GB', '16GB', '32GB']
key = list(capacityDDR4.values())
for i in range(len(allCapacity)):
    for data in DDR['memoryDDR4']:
        if allCapacity[i] in data['Name']:
            key = list(capacityDDR4.values())
            key[i].append(data)

# Capacity / DDR3
key = list(capacityDDR3.values())
for i in range(len(allCapacity)):
    for data in DDR['memoryDDR3']:
        if allCapacity[i] in data['Name']:
            key = list(capacityDDR3.values())
            key[i].append(data)


# Frequency / DDR5

# FILTER == 8gb
for data in capacityDDR5['8gb']:  # 4800Mhz 16gb DDR5
    if '4800MHz' in data['Name']:
        frequencyDDR5['8gb_48000Mhz'].append(data)

# FILTER == 16gb
for data in capacityDDR5['16gb']:  # 4800Mhz 16gb DDR5
    if '4800MHz' in data['Name']:
        frequencyDDR5['16gb_4800Mhz'].append(data)

# FILTER == 32gb
for data in capacityDDR5['32gb']:
    if '5600MHz' in data['Name']:  # 5600Mhz 32gb DDR5
        frequencyDDR5['32gb_5600Mhz'].append(data)
    if '6000MHz' in data['Name']:  # 6000Mhz 32gb DDR5
        frequencyDDR5['32gb_6000Mhz'].append(data)

# # Frequency / DDR4
#
# # FILTER == 4gb
# for data in memoryDDR4_4gb:
#     if '2400MHz' in data['Name']:  # 2600Mhz 4gb DDR4
#         memoryDDR4_4gb_2400Mhz.append(data)
#     if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR4
#         memoryDDR4_4gb_1600Mhz.append(data)
#
# # FILTER == 8gb
# for data in memoryDDR4_8gb:
#     if '2666MHz' in data['Name']:  # 2666MHz 8gb DDR4
#         memoryDDR4_8gb_2666Mhz.append(data)
#     if '3000MHz' in data['Name']:  # 3000MHz 8gb DDR4
#         memoryDDR4_8gb_3000Mhz.append(data)
#     if '3200MHz' in data['Name']:  # 3200MHz 8gb DDR4
#         memoryDDR4_8gb_3200Mhz.append(data)
#
# # FILTER == 16gb
# for data in memoryDDR4_16gb:
#     if '2666MHz' in data['Name']:  # 2666MHz 16gb DDR4
#         memoryDDR4_16gb_2666Mhz.append(data)
#     if '3600MHz' in data['Name']:  # 3600MHz 16gb DDR4
#         memoryDDR4_16gb_3600Mhz.append(data)
#     if '3000MHz' in data['Name']:  # 3000MHz 16gb DDR4
#         memoryDDR4_16gb_3000Mhz.append(data)
#     if '3200MHz' in data['Name']:  # 3200MHz 16gb DDR4
#         memoryDDR4_16gb_3200Mhz.append(data)
#
# # FILTER == 32gb
# for data in memoryDDR4_32gb:
#     if '2666MHz' in data['Name']:  # 5600Mhz 32gb DDR4
#         memoryDDR4_32gb_2666Mhz.append(data)
#     if '3600MHz' in data['Name']:  # 5600Mhz 32gb DDR4
#         memoryDDR4_32gb_3600Mhz.append(data)
#     if '3000MHz' in data['Name']:  # 5600Mhz 32gb DDR4
#         memoryDDR4_32gb_3000Mhz.append(data)
#     if '3200MHz' in data['Name']:  # 5600Mhz 32gb DDR4
#         memoryDDR4_32gb_3200Mhz.append(data)
#
# # Frequency / DDR3
#
# # FILTER == 4gb
# for data in memoryDDR3_4gb:
#     if '2400MHz' in data['Name']:  # 2400MHz 4gb DDR3
#         memoryDDR3_4gb_1600Mhz.append(data)
#     if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR3
#         memoryDDR3_4gb_1333Mhz.append(data)
#
# # FILTER == 8gb
# for data in memoryDDR3_8gb:
#     if '1600MHz' in data['Name']:  # 1600MHz 8gb DDR3
#         memoryDDR3_8gb_1600Mhz.append(data)
#     if '1866MHz' in data['Name']:  # 1866MHz 8gb DDR3
#         memoryDDR3_8gb_1866Mhz.append(data)
#
# # FILTER == 16gb
# for data in memoryDDR3_16gb:
#     if '1600MHz' in data['Name']:  # 1600MHz 16gb DDR3
#         memoryDDR3_16gb_1600Mhz.append(data)
#     if '1866MHz' in data['Name']:  # 1866MHz 16gb DDR3
#         memoryDDR3_16gb_1866Mhz.append(data)
#
# # FILTER == 32gb
# for data in memoryDDR3_32gb:
#     if '1600MHz' in data['Name']:  # 1600MHz 32gb DDR3
#         memoryDDR3_32gb_1600Mhz.append(data)
