from requests_html import HTMLSession
from bs4 import BeautifulSoup
from sympy import print_maple_code
from Ahumada import *
from Salcobrand import *
from Medicamento import *
from BancoUF import *
import csv

url_ahumada = "https://www.farmaciasahumada.cl/catalogsearch/result/index/?p=1&q="
url_salcobrand = "https://salcobrand.cl/search_result?query="

with open('principios_activos.txt',encoding='utf8') as f:
    lines = f.readlines()
    

with open('out.csv', 'a', newline='',encoding='utf8') as f_object:  
            # Pass the CSV  file object to the writer() function
    writer_object = csv.writer(f_object)
    writer_object.writerow(["busqueda","farmacia","descripcion","precio_clp","precio_uf"])

abuscar = []
for line in lines:
    line = line.replace("\n","")
    line = line.replace(" ","+")
    abuscar.append(line)

print(abuscar)

uf = int(Banco().get_uf())

print("El valor actual del UF es: " + str(uf))


paginas_ahumada = []
paginas_salcobrand = []
paginas_cruz = []


for busqueda in abuscar:

    query = 'https://www.farmaciasahumada.cl/catalogsearch/result/index/?p='+str(1)+'&q=' + busqueda

    while True:
        f_ahumada = Ahumada(busqueda,query) #crea un objeto de la clase Ahumada
        next_page = f_ahumada.getnextpage() #obtiene el url de la siguiente pagina
        if  next_page == False: #si no hay siguiente pagina, termina el ciclo
            break
        else:
            query = next_page #si hay siguiente pagina, cambia el query
        paginas_ahumada.append(f_ahumada) #agrega el objeto a la lista de paginas de ahumada


    lista_de_medicamentos_ahumada = []
    for pagina in paginas_ahumada: #recorre la lista de paginas de ahumada
        f_ahumada_product_list = (pagina.get_product_list()) #obtiene la lista de productos de la pagina
        for producto in f_ahumada_product_list: #recorre la lista de productos de la pagina
            product_desc = producto.find("a",{"class" : "product-item-link"}).text #obtiene la descripcion del producto
            precio_clp = producto.find("span",{"class" : "price"}).text #obtiene el precio del producto
            precio_clp = precio_clp.replace("$","")
            precio_clp = int(precio_clp.replace(".",""))
            precio_uf = round(precio_clp / uf,2) #calcula el precio en uf
            medicamento_a = Medicamento(busqueda,"Ahumada", product_desc,precio_clp,precio_uf)
            lista_de_medicamentos_ahumada.append(medicamento_a) #agrega el medicamento a la lista de medicamentos
            # print(Medicamento("Ahumada", product_desc,precio_clp,precio_uf)) #imprime el medicamento en formato csv
            with open('out.csv', 'a', newline='',encoding='utf8') as f_object:  
                # Pass the CSV  file object to the writer() function
                writer_object = csv.writer(f_object)
                # Result - a writer object
                # Pass the data in the list as an argument into the writerow() function
                writer_object.writerow(medicamento_a.a_lista())  
                # Close the file object
                f_object.close()
    print("TERMINE AHUMADA")
    
    url_salcobrand = "https://salcobrand.cl/search_result?query=" + busqueda


    #posible for con next page

    f_salcobrand = Salcobrand("paracetamol",url_salcobrand+"paracetamol")
    nose = f_salcobrand.get_product_list()
    lista_de_medicamentos_salcobrand=[]
    for producto in nose:
    
      product_desc = producto.find("span",{"class" : "product-info truncate"}).text
      precio_clp = producto.find("div",{"class" : "sale-price"}).text
      precio_clp = precio_clp.replace("$","")
      precio_clp = precio_clp.replace(".","")
      precio_clp = precio_clp.replace("Oferta:","")
      precio_uf = int(precio_clp) / uf
      precio_uf = round(precio_uf,2)
      medicamento_b= Medicamento(busqueda,"Salcobrand", product_desc,precio_clp,precio_uf)
      lista_de_medicamentos_salcobrand.append(medicamento_b)
      with open('out.csv', 'a', newline='',encoding='utf8') as f_object:  
             # Pass the CSV  file object to the writer() function
             writer_object = csv.writer(f_object)
             # Result - a writer object
             # Pass the data in the list as an argument into the writerow() function
             writer_object.writerow(medicamento_b.a_lista())  
             # Close the file object
             f_object.close()

print("TERMINE")