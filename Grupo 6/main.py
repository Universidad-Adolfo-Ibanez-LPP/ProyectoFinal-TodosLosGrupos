from requests_html import HTMLSession
from bs4 import BeautifulSoup
import ahumada
import salcobrand

url_ahumada = "https://www.farmaciasahumada.cl/catalogsearch/result/index/?p=1&q="
url_salcobrand = "https://salcobrand.cl/search_result?query="

f_ahumada = ahumada.Ahumada("paracetamol")
lista = []


# print("url =" ,f_ahumada.get_url())

# chorizo  = f_ahumada.getnextpage()

# print(chorizo)


# f_salcobrand = salcobrand.Salcobrand("paracetamol")

# print(f_ahumada.getdata())

f_ahumada_product_list = (f_ahumada.get_product_list())



for producto in f_ahumada_product_list:
    product_desc = producto.find("a",{"class" : "product-item-link"}).text
    precio_clp = producto.find("span",{"class" : "price"}).text
    print(product_desc)
    print(precio_clp)