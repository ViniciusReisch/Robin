<h1>
  <a href="https://www.google.com/"> <img src="img/robin-logo.png" width="40%"> </a>
</h1>

<h1> Descrição ⚙ </h1>

<p> Robin é um website que visa ajudar as pessoas na hora de escolher as peças para montar seu computador, o Robin reúne dados de diversos sites de venda de produtos de informática, retornando os valores mais acessíveis. </p>

<h1> Ferramentas Utilizadas 🛠 </h1>

- Selenium <a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="25" alt="Selenium"/></a>
- MySQL <a href="https://selenium.dev"><img src="https://kinsta.com/wp-content/uploads/2019/04/mysql-logo-1.svg" width="43" alt="MySQL"/></a>
- Python <a href="https://selenium.dev"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png" width="23" alt="MySQL"/></a>

<h1> Web-Scraping </h1>

<p> A maneira que achamos para pegar todos os dados de peças de computador foi por meio do <strong>Web-Scraping</strong>, que é uma forma de mineração no qual nos permite a extração de dados de sites da web convertendo-os em informação estruturada para posterior análise, o framework ultilizado para obter esses dados foi o <strong>Selenium</strong> em <strong>Python</strong> </p>
<p> Cada site possui uma estrutura especifica para seus dados: </p>

<h2> Pichau </h2>

<p> A <strong>Pichau</strong> com certeza foi o site que mais tivemos dificuldade, a estrutura do site altera a cada computador diferente que o mesmo é aberto, então uma forma que achamos para obter os dados em diferentes computadores que executássemos o código e ele ainda funcionasse, foi usando a <strong>lib Socket</strong> para salvar uma estrutura específica para cada IP. </p>

```python
import socket
    hostIP = socket.gethostname()           # IP Local
    IP = socket.gethostbyname(hostIP)       # Specif IP
```

<p> Outro problema que nós tivemos, foi o pequeno efeito de <strong>fade-in</strong> que é aplicado apartir da terceira linha de produtos do site, sendo assim as imagens dos ítens só passam a aparecer no <strong>source HMTL</strong> do site depois que você da scoll pra baixo. </p>

<img src="img/robin.gif" width="50%">

<p> Para resolver esse problema, nós ultilizamos um comando do <strong>Selenium</strong> para pegar a altura total do site, e para fazer ele dar um scroll down automático de acordo com o tamanho do site. </p>

```python
from selenium import webdriver
    height = driver.execute_script("return document.body.scrollHeight") 
    while scroll < height:
         driver.execute_script(f"window.scrollTo(0, {scroll});")
         scroll += 200
```
<p> Problemas resolvidos, agora vem a hora de pegar cada especificação de peça, como o preço, o nome, etc... </p>
<p> Tendo isso em mente, optamos na Pichau essa lista de especificações:</p>

| Especificações | Dados |
| --- | --- |
| Preço parcelado | R$ 771,29 |
| Preço | R$678,74 |
| Nome | MEMORIA TEAM GROUP T-FORCE DELTA RGB, 8GB(1X8GB), DDR4, 3200MHZ, C16, BRANCO, TF4D48G3200HC16C01 |
| Link | https://www.pichau.com.br/memoria-team-group-t-force-delta-rgb-8gb-1x8gb-ddr4-3200mhz-c16-branco-tf4d48g3200hc16c01 |
| Link da imagem | https://media.pichau.com.br/media/catalog/product/cache/2f958555330323e505eba7ce930bdf27/t/f/tf4d48g3200hc16c011.jpg |
| Horário de Scraping | 09/07/2022 23:22:34 |

<h3> Como realizar o <strong>scraping</strong> na Pichau </h3>

<table>
  <tr>
    <td>Bloco de informação </td>
     <td>Código de web-scraping</td>
     <td>Explicação</td>
  </tr>
  <tr>
    <td valign="top"><img src="img/Captura de tela 2022-09-10 224901.jpg" width="200%"></td>
    <td valign="top">
    
```python
# Crawling Products == Name
product = driver.find_elements('tag name', 'h2')
for i in product:
    if i.text == "":
        continue
    namesProducts.append(i.text)
``` 

</td>
<td valign="top">

No site da Pichau os títulos dos produtos são separados em tags ``h2``, sendo assim temos que puxar todas as tags h2 do site usando
``find_elements('tag name', 'h2')``

</td>
  <tr>
    <td valign="top"><img src="img/Captura de tela 2022-09-10 224901.jpg" width="200%"></td>
    <td valign="top">
    
```python
# Crawling Products == Image
while scroll < height:
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    product = driver.find_elements('tag name', 'img')
    for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
    scroll += 200
imgProducts = list(dict.fromkeys(imgProducts))
``` 

</td>
<td valign="top">

  As imagens dos produtos são separados em tags ``img`` devido ao problema do <strong>fade-in</strong> explicado acima. Temos que usar um comando  ``driver.execute_script(f"window.scrollTo(0, {scroll});")`` dentro de um laço ``` while ``` para que o código fique dando scrap e descendo, depois temos separar as imagens dos produtos usando: 
```python
for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
``` 

</td>
<td valign="top">

No site da Pichau os títulos dos produtos são separados em tags ``h2``, sendo assim temos que puxar todas as tags h2 do site usando
``find_elements('tag name', 'h2')``

</td>
  <tr>
    <td valign="top"><img src="img/Captura de tela 2022-09-10 224901.jpg" width="200%"></td>
    <td valign="top">
    
```python
# Crawling Products == Image
while scroll < height:
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    product = driver.find_elements('tag name', 'img')
    for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
    scroll += 200
imgProducts = list(dict.fromkeys(imgProducts))
``` 

</td>
<td valign="top">

  As imagens dos produtos são separados em tags ``img`` devido ao problema do <strong>fade-in</strong> explicado acima. Temos que usar um comando  ``driver.execute_script(f"window.scrollTo(0, {scroll});")`` dentro de um laço ``` while ``` para que o código fique dando scrap e descendo, depois temos separar as imagens dos produtos usando: 
```python
for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
``` 

</td>
<td valign="top">

No site da Pichau os títulos dos produtos são separados em tags ``h2``, sendo assim temos que puxar todas as tags h2 do site usando
``find_elements('tag name', 'h2')``

</td>
  <tr>
    <td valign="top"><img src="img/Captura de tela 2022-09-10 224901.jpg" width="200%"></td>
    <td valign="top">
    
```python
# Crawling Products == Image
while scroll < height:
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    product = driver.find_elements('tag name', 'img')
    for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
    scroll += 200
imgProducts = list(dict.fromkeys(imgProducts))
``` 

</td>
<td valign="top">

  As imagens dos produtos são separados em tags ``img`` devido ao problema do <strong>fade-in</strong> explicado acima. Temos que usar um comando  ``driver.execute_script(f"window.scrollTo(0, {scroll});")`` dentro de um laço ``` while ``` para que o código fique dando scrap e descendo, depois temos separar as imagens dos produtos usando: 
```python
for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
``` 

</td>
 </table>
 
<br>
<h2>
UNDER DEVELOPMENT
</h2>
<br>
📜Project developed in the <a href="https://www.entra21.com.br/">Entra21</a> Python Class
