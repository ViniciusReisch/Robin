from promo import itens

def crawl_products():
    products = []
    allData = [itens.Crawl_Terabyte(), itens.Crawl_Kabum()]
    for i in allData:
        for k in i:
            products.append(k)
    return products


a = crawl_products()