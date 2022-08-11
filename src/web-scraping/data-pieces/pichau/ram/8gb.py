import requests
from bs4 import BeautifulSoup

# Memória ram 8gb
precos = []
precosParcelado = []
nomes = []

header = {'user-agent': 'Mozilla/5.0'}
response = requests.get("https://www.pichau.com.br/hardware/memorias?capacidadememoria=199", headers=header)
html = BeautifulSoup(response.text, 'html.parser')

for nome in html.select('.MuiTypography-h6'):
    nomes.append(nome.text)

for preco in html.select('.jss64'):
    precos.append(preco.text)

teste = html.select('.MuiCardContent-root')
div = teste[0].contents[1]
div = html.select('.jss69')
print(div[0].text)