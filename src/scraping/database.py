import mysql.connector
import main

allProducts = main.get_All()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RobinDatabase"
)
cursor = conexao.cursor()

for product in allProducts:
    cursor.execute(f'INSERT INTO alldata (store, name, price, changeablePrice, installmentPrice, '
                   f'changeableInstallmentPrice, Link, Image, Time, Logo, Type, Model, Format, Interface, Capacity, DDR,'
                   f'Frequency, Platform, Color,  Discount, OldPrice) VALUES ("{product["Store"]}", "{product["Name"]}", '
                   f'"{product["Price"][0]}", "{product["Price"][1]}", "{product["Installment price"]}", '
                   f'"{product["Installment price"][1]}", "{product["Link"]}", "{product["Image"]}", "{product["Time"]}", '
                   f'"{product["Logo"]}", "{product["Type"]}", "{product["Model"]}", "{product["Format"]}", '
                   f'"{product["Interface"]}", "{product["Capacity"]}", "{product["DDR"]}", "{product["Frequency"]}", '
                   f'"{product["Platform"]}", "{product["Color"]}", "{product["Discount"]}", "{product["Old Prices"]}")')
conexao.commit()
cursor.close()
conexao.close()
