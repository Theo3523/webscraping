import requests
from bs4 import BeautifulSoup


url_1 = 'https://www.19kala.com/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3' \
        '%D9%88%D9%86%DA%AF-samsung '
try:
    result = requests.get(url_1)
    result.raise_for_status()
    doc1 = BeautifulSoup(result.text, 'html.parser')
except Exception as e:
    print(e)
get_mobiles = doc1.find('div', class_="col-sm-9").find('div', class_=["row", "main-products" ,"product-grid"])
get_mobiles=get_mobiles.find_all('div',class_="product-list-item xs-100 sm-100 md-100 lg-100 xl-100")
mobiles=[]
for i in get_mobiles:
    mobiles.append(i.find('a')['href'])


for i in mobiles:
    url = i
    try:
        result = requests.get(url)
        result.raise_for_status()
        doc = BeautifulSoup(result.text, 'html.parser')

        product_name=doc.find('div',class_='right col-md-4').find('h1').text
        product_price=doc.find('ul',class_='list-unstyled price').find('li',class_='price-new').text
        print(product_name)
        print(product_price)
    except:
        print(product_name,'Not available in stock')
