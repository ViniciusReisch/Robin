from scraping import *
import tweepy

# api = tweepy.Client(
#     consumer_key='UyVtE6kqxNba68SGXkBBvcTsp',
#     consumer_secret='IGLke5dnLhTGAz6qexISGRKEFcsHywJZmGm1coRw7Ev70z9ne0',
#     access_token='1570009243717099534-P507lUYxogGfSwmWnlKFxn6kpv6vhx',
#     access_token_secret='bupgNZCzjWwDhAEKokc7tcYFxc7pEBE86qNyButTDijzs'
# )
# tweet = api.create_tweet(text='test bot')
products = []

allData = [Crawl_Terabyte(), Crawl_Kabum()]
for i in allData:
    for k in i:
        products.append(k)

for i in products:
    if i['Discount'] > 40:
        text = f'{i["Name"]} está com {i["Discount"]}% de desconto na {i["Store"]} Store' \
               f'\n\n De R${i["Old Price"]} ' \
               f'\n Por: R${i["Price"]}' \
               f'\n Você economiza: R${float(i["Old Price"]) - float(i["Price"])} ({i["Discount"]}%)' \
               f'\n\n Você pode comprar em: {i["Link"]}' \
               f'\n Siga a Robin nas suas redes socias para receber mais promoções de hardware: https://linkr.bio/robinsite'
        print(text)