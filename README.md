<h1>
  <a href="https://www.google.com/"> <img src="img/robin-logo.png" width="40%"> </a>
</h1>

<h1> Description ⚙ </h1>

<p> Robin é um website que visa ajudar as pessoas na hora de escolher as peças para montar seu computador, o Robin reúne dados de diversos sites de venda de produtos de informática, retornando os valores mais acessíveis. </p>

<h1> Tools Used 🛠 </h1>

- Selenium <a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="25" alt="Selenium"/></a>
- MySQL <a href="https://selenium.dev"><img src="https://kinsta.com/wp-content/uploads/2019/04/mysql-logo-1.svg" width="43" alt="MySQL"/></a>
- Python <a href="https://selenium.dev"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png" width="23" alt="MySQL"/></a>

<h1> Web-Scraping </h1>

<p> A maneira que achamos para pegar todos os dados de peças de computador foi por meio do Web-Scraping que é uma forma de mineração que permite a extração de dados de sites da web convertendo-os em informação estruturada para posterior análise, o framework ultilizado para obter esses dados foi o Selenium em Python </p>
<p> Cada site possui uma estrutura especifica para seus dados: </p>

<h2> Pichau </h2>

<p> A Pichau com certeza foi o site que eu mais tive dificuldade, a estrutura do site altera a cada computador diferente que o mesmo é aberto, então uma forma que eu achei para obter os dados em diferentes computadores que eu executasse o código ele ainda sim funcionasse, foi usando a lib Socket para salvar uma estrutura especifica para cada IP, nesse README estarei usando a estrutura gerada no meu computador pessoal. </p>

```python
import socket
    hostIP = socket.gethostname()           # IP Local
    IP = socket.gethostbyname(hostIP)       # Specif IP
```

<p> Outro problema que eu tive foi o pequeno efeito de fade-in que é aplicado apartir da terceira linha de produtos do site, sendo assim as imagens dos itens só passam a aparecer no source HMTL do site depois que você da scoll pra baixo. </p>

<img src="img/robin.gif" width="50%">

<p> Para resolver esse problema eu ultizei um comandos do Selenium para pegar a altura total do site, e para fazer ele dar um scroll down automatico de acordo com o tamanho do site. </p>

```python
from selenium import webdriver
    height = driver.execute_script("return document.body.scrollHeight") 
    while scroll < height:
         driver.execute_script(f"window.scrollTo(0, {scroll});")
         scroll += 200
```
<p> Problemas resolvidos agora vem a hora de pegar cada especificação de peça, como o preço, o nome e etc... </p>
<p> Tendo isso em mente na Pichau optei por essa lista de especificações, exemplo: </p>

| Especificações | Dados |
| --- | --- |
| Preço parcelado | R$ 771,29 |
| Preço | R$678,74 |
| Nome | MEMORIA TEAM GROUP T-FORCE DELTA RGB, 8GB(1X8GB), DDR4, 3200MHZ, C16, BRANCO, TF4D48G3200HC16C01 |
| Link | https://www.pichau.com.br/memoria-team-group-t-force-delta-rgb-8gb-1x8gb-ddr4-3200mhz-c16-branco-tf4d48g3200hc16c01 |
| Link da imagem | https://media.pichau.com.br/media/catalog/product/cache/2f958555330323e505eba7ce930bdf27/t/f/tf4d48g3200hc16c011.jpg |
| Horário de Scraping | 09/07/2022 23:22:34 |

<h3> Texto de nome de produto </h3>
<p> No site da Pichau os títulos dos produtos são separados em tags ``h2`` sendo assim é só puxar todas h2 do site usando ``find_elements('tag name', 'h2')`` </p>
<table>
  <tr>
    <td>Bloco de informação </td>
     <td>Código de web-scraping</td>
  </tr>
  <tr>
    <td valign="top"><img src="img/Captura de tela 2022-09-10 224901.jpg" width="100%"></td>
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

 </table>
 
<br>
<h2>
UNDER DEVELOPMENT
</h2>
<br>
📜Project developed in the <a href="https://www.entra21.com.br/">Entra21</a> Python Class
