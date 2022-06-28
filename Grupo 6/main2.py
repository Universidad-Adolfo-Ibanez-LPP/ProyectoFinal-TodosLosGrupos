from requests_html import HTMLSession
from bs4 import BeautifulSoup
from Ahumada import *
from Salcobrand import *
from Medicamento import *
from BancoUF import *


url_salcobrand = "https://salcobrand.cl/search_result?query="


uf = int(Banco().get_uf())

print("El valor actual del UF es: " + str(uf))

f_salcobrand = Salcobrand("paracetamol",url_salcobrand+"paracetamol")

nose = f_salcobrand.get_product_list()

for producto in nose:
    
    product_desc = producto.find("span",{"class" : "product-info truncate"}).text
    precio_clp = producto.find("div",{"class" : "sale-price"}).text
    precio_clp = precio_clp.replace("$","")
    precio_clp = precio_clp.replace(".","")
    precio_clp = precio_clp.replace("Oferta:","")
    precio_uf = int(precio_clp) / uf
    precio_uf = round(precio_uf,2)



    print (product_desc)
    print (precio_clp)
    print (precio_uf)
    print("")