import mysql.connector
import main

allProducts = main.get_All()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RobinDatabase"
)

if conexao.is_connected():
    print('deu certo')
    cursor = conexao.cursor()


