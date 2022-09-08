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

<br>
<h2>
UNDER DEVELOPMENT
</h2>
<br>
📜Project developed in the <a href="https://www.entra21.com.br/">Entra21</a> Python Class
