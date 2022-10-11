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
