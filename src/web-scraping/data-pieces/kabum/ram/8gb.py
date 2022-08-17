import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from selenium import webdriver
from time import sleep

namesProducts = []
imgProducts = []
allData = []
installmentPriceProducts = []
linksProducts = []
pricesProducts = []

url = 'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=1&page_size=20&facet_filters=eyJDYXBhY2lkYWRlIjpbIjggR0IgKDF4IDhHQikiXX0=&sort=most_searched'
headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
driver.get(url)

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
print(site)
