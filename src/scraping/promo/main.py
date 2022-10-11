from itens import Crawl_Kabum, Crawl_Terabyte

def crawl_products():
    products = []
    allData = [Crawl_Terabyte(), Crawl_Kabum()]
    for i in allData:
        for k in i:
            products.append(k)
    return products
    
a = crawl_products()