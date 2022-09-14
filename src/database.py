import mysql.connector
from scraping import main

allProducts, Cabinet, Font, SSD, HardDisk, MotherBoard, GPU, CPU, RAM = main.AllProducts.get_All()



#
# banco = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="webscraping"
# )
#
# cursor = banco.cursor()
#
# # All memory's
# cursor.execute("CREATE TABLE memoryRam(Name VARCHAR(255), Price VARCHAR(255), changeablePrice FLOAT(10), "
#                "installmentPrince VARCHAR(255), changebleInstallmentePrice VARCHAR(255), link VARCHAR(255), "
#                "image VARCHAR(255), time VARCHAR(255), logo VARCHAR(255)) ")