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

for product in allProducts:
    cursor.execute(f"INSERT INTO Alldata (store, name, price, changeablePrice, installmentPrice, "
                   f"changeableInstallmentPrice, Link, Image, Time, Logo, Type, Model, Format, Interface, Capacity, "
                   f"DDR, Frequency, Platform, Color) VALUES ({product['Store']}, {product['Name']},"
                   f"{product['Price'][0]}, {product['Price'][1]}, {product['Installment price'][0]}, "
                   f"{product['Installment price'][1]}, {product['Link']}, {product['Image']}, "
                   f"{product['Time']}, {product['Logo']}, {product['Type']}, {product['Model']}, "
                   f"{product['Format']}, {product['Interface']}, {product['Capacity']}, "
                   f"{product['DDR']}, {product['Frequency']}, {product['Platform']}, {product['Color']})")

conexao.close()
cursor.close()


