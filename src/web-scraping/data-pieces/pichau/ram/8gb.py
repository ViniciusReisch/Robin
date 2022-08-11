import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Memória ram 8gb
namesProducts = []
header = {'user-agent': 'Mozilla/5.0'}
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199", headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

for nome in soup.select('.MuiTypography-h6'):
    namesProducts.append(nome.text)

navegador = webdriver.Chrome()
navegador.get('https://www.pichau.com.br/hardware/memorias?capacidadememoria=199')
produto = navegador.find_elements('class name', 'jss69')
priceProducts = []
sleep(5)
for i in produto:
    if i.text == "":
        continue
    priceProducts.append(i.text)
    sleep(1)

# Reunindo dados em json
allData = []
for i in range(len(priceProducts)):
    dataDic = {namesProducts[i]: priceProducts[i]}
    allData.append(dataDic)

print(allData)
