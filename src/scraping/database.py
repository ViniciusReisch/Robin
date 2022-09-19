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
    cursor.execute(f"INSERT into Store {product['Store']}")
    cursor.execute(f"INSERT into Name {product['Name']}")
    cursor.execute(f"INSERT into Price {product['Price'][0]}")
    cursor.execute(f"INSERT into changeablePrice {product['changeablePrice'][1]}")
    cursor.execute(f"INSERT into installmentPrice {product['installmentPrice'][0]}")
    cursor.execute(f"INSERT into changeableInstallmentPrice {product['changeableInstallmentPrice'][1]}")
    cursor.execute(f"INSERT into Link {product['Link']}")
    cursor.execute(f"INSERT into Image {product['Image']}")
    cursor.execute(f"INSERT into Time {product['Time']}")
    cursor.execute(f"INSERT into Logo {product['Logo']}")
    cursor.execute(f"INSERT into Type {product['Type']}")
    cursor.execute(f"INSERT into Model {product['Model']}")
    cursor.execute(f"INSERT into Format {product['Format']}")
    cursor.execute(f"INSERT into Interface {product['Interface']}")
    cursor.execute(f"INSERT into Capacity {product['Capacity']}")
    cursor.execute(f"INSERT into DDR {product['DDR']}")
    cursor.execute(f"INSERT into Frequency {product['Frequency']}")
    cursor.execute(f"INSERT into Platform {product['Platform']}")
    cursor.execute(f"INSERT into Color {product['Color']}")
    cursor.execute(f"INSERT into Color {product['Color']}")

conexao.close()
cursor.close()


