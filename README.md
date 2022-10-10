<h1>
  <a href="https://www.google.com/"> <img src="img/robin-logo.png" width="40%"> </a>
</h1>

<h1> Description ⚙ </h1>

<p> Robin is a site that aims to help people how to choose the parts to assemble their computer Robin collects computer data sales sites, returning the most affordable values. </p>

<h1> Used Tools 🛠 </h1>

- Selenium <a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="25" alt="Selenium"/></a>
- MySQL <a href="https://selenium.dev"><img src="https://kinsta.com/wp-content/uploads/2019/04/mysql-logo-1.svg" width="43" alt="MySQL"/></a>
- Python <a href="https://selenium.dev"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png" width="23" alt="MySQL"/></a>

<h1> Web-Scraping </h1>

<p> The way we found to obtain all the data from the parts of the computer was through Web-Scraping, which is a form of mining that allows us to extract data from websites, converting them into structured information for later analysis, the framework used to obtain these data was Selenium in Python. </p>
<p> Each site has a specific structure for its data: </p>

<h2> Pichau </h2>

<p> Pichau was certainly the site that we had the most difficulty with, the structure of the site changes with each different computer that it is opened, so a way we found to get the data on different computers that we ran the code and it still worked, was using the Socket lib to save a specific structure for each IP. </p>

```python
import socket
    hostIP = socket.gethostname()           # IP Local
    IP = socket.gethostbyname(hostIP)       # Specif IP
```

<p> Another issue we had was the small fade-in effect that is applied from the third product line on the site, so the item images only start to appear in the site's HTML source after you scroll down. </p>

<img src="img/robin.gif" width="50%">

<p> To solve this problem, we use a Selenium command to get the full height of the site and make it automatically scroll down according to the size of the site. </p>

```python
from selenium import webdriver
    height = driver.execute_script("return document.body.scrollHeight") 
    while scroll < height:
         driver.execute_script(f"window.scrollTo(0, {scroll});")
         scroll += 200
```
<p> Problems solved, now it's time to get the specification of each part like price, name, etc... </p>
<p> With that in mind, we chose this list of specifications in Pichau:</p>

| Especificações | Dados |
| --- | --- |
| Preço parcelado | R$ 771,29 |
| Preço | R$678,74 |
| Nome | MEMORIA TEAM GROUP T-FORCE DELTA RGB, 8GB(1X8GB), DDR4, 3200MHZ, C16, BRANCO, TF4D48G3200HC16C01 |
| Link | https://www.pichau.com.br/memoria-team-group-t-force-delta-rgb-8gb-1x8gb-ddr4-3200mhz-c16-branco-tf4d48g3200hc16c01 |
| Link da imagem | https://media.pichau.com.br/media/catalog/product/cache/2f958555330323e505eba7ce930bdf27/t/f/tf4d48g3200hc16c011.jpg |
| Horário de Scraping | 09/07/2022 23:22:34 |

<h3> How to perform the scraping on Pichau: </h3>

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

On Pichau's website, product titles are separated into ``h2`` tags, so we have to pull all h2 tags from the website using
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

Product images are separated into ``img`` tags due to the fade-in issue explained above. We have to use a command ``driver.execute_script(f"window.scrollTo(0, {scroll});")`` inside a loop ``` while ``` so that the code is scraping and scrolling down the page, so we have to separate the images from the products using:
```python
for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
``` 

</td>
<td valign="top">

On Pichau's site, the product titles are separated into ``h2`` tags, so we have to pull all the h2 tags from the site using
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

Product images are separated into ``img`` tags due to the fade-in issue explained above. We have to use a command ``driver.execute_script(f"window.scrollTo(0, {scroll});")`` inside a loop``` while ``` so that the code is scraping and scrolling down the page, so we have to separate the images from the products using: 
```python
for e in product:
        if 'product' in e.get_attribute('src'):
            imgProducts.append(e.get_attribute('src'))
``` 

</td>
<td valign="top">

On Pichau's site, the product titles are separated into ``h2`` tags, so we have to pull all the h2 tags from the site using
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

 Product images are separated into ``img`` tags due to the fade-in issue explained above. We have to use a command``driver.execute_script(f"window.scrollTo(0, {scroll});")`` inside a loop ``` while ``` so that the code is scraping and scrolling down the page, so we have to separate the images from the products using: 
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
📜Project developed in the <a href="https://www.entra21.com.br/">Entra21</a> Matutine Python Class
