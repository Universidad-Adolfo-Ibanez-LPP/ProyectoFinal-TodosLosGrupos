from requests_html import HTMLSession
from bs4 import BeautifulSoup
from sympy import print_maple_code
from Ahumada import *
from Escritor import Escritor
from Salcobrand import *
from Medicamento import *
from BancoUF import *
from Escritor import *
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


paginas_cruz = []


for busqueda in abuscar:
#####
    paginas_ahumada = []
    paginas_salcobrand = []

    query = 'https://www.farmaciasahumada.cl/catalogsearch/result/index/?p='+str(1)+'&q=' + busqueda

    while True:
        f_ahumada = Ahumada(busqueda,query) #crea un objeto de la clase Ahumada
        next_page = f_ahumada.getnextpage() #obtiene el url de la siguiente pagina
        if  next_page == False: #si no hay siguiente pagina, termina el ciclo
            break
        else:
            query = next_page #si hay siguiente pagina, cambia el query
        paginas_ahumada.append(f_ahumada) #agrega el objeto a la lista de paginas de ahumada

    escritor_ahumada = Escritor(busqueda = busqueda,uf=uf,paginas = paginas_ahumada)
    escritor_ahumada.to_csv_ahumada()
    print("TERMINE AHUMADA")

    url_salcobrand = "https://salcobrand.cl/search_result?query=" + busqueda
    f_salcobrand= Salcobrand(busqueda=busqueda, url=url_salcobrand)
    paginas_salcobrand.append(f_salcobrand)

    escritor_salcobrand= Escritor(busqueda=busqueda,uf=uf,paginas=paginas_salcobrand)
    escritor_salcobrand.to_csv_salcobrand()
    print("TERMINE SALCOBRAND")
# ######
#     print("TERMINE AHUMADA")



print("TERMINE")