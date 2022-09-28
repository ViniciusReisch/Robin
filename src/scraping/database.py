import mysql.connector
# import main
#
# allProducts = main.get_All()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RobinDB"
)
cursor = conexao.cursor()

product = {'Store': 'Kabum', 'Name': 'Memória Gamer Husky Gaming, 8GB, 2666MHz, DDR4, CL19, Preto - HGMF001', 'Price': ['R$ 159,99', 159.99], 'Installment price': [0,0], 'Link': 'https://www.kabum.com.br/produto/114222/memoria-gamer-husky-gaming-8gb-2666mhz-ddr4-cl19-preto-hgmf001', 'Image': 'https://images.kabum.com.br/produtos/fotos/114222/memoria-husky-8gb-2666mhz-ddr4-cl19-preto-hmr-d4826_1597862504_m.jpg', 'Time': '2022-09-28 14:16:56', 'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'RAM Memory', 'Model': '2666MHz 8GB DDR4', 'Format': '', 'Interface': '', 'Capacity': '8GB', 'DDR': 'DDR4', 'Frequency': '2666MHz', 'Platform': '', 'Color': ''}
cursor.execute(f'INSERT INTO AllData (store, name, price, changeablePrice, installmentPrice, '
                   f'changeableInstallmentPrice, Link, Image, Time, Logo, Type, Model, Format, Interface, Capacity, DDR, '
                   f'Frequency, Platform, Color) VALUES ("{product["Store"]}", "{product["Name"]}", '
                   f'"{product["Price"][0]}", "{product["Price"][1]}", "{product["Installment price"]}", '
                   f'"{product["Installment price"][1]}", "{product["Link"]}", "{product["Image"]}", "{product["Time"]}", '
                   f'"{product["Logo"]}", "{product["Type"]}", "{product["Model"]}", "{product["Format"]}", '
                   f'"{product["Interface"]}", "{product["Capacity"]}", "{product["DDR"]}", "{product["Frequency"]}", '
                   f'"{product["Platform"]}", "{product["Color"]}")')
conexao.commit()
cursor.close()
conexao.close()
