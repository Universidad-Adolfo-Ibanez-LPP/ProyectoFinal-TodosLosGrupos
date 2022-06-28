from requests_html import HTMLSession
from bs4 import BeautifulSoup
from Medicamento import *
from BancoUF import *
import csv


class Escritor():

    def __init__(self,busqueda,uf,paginas):
        self.busqueda = busqueda
        self.uf = uf
        self.paginas = paginas



    def to_csv_ahumada(self):
        
        # paginas_ahumada = []

        # query = 'https://www.farmaciasahumada.cl/catalogsearch/result/index/?p='+str(1)+'&q=' + busqueda

        # while True:
        #     f_ahumada = Ahumada(busqueda,query) #crea un objeto de la clase Ahumada
        #     next_page = f_ahumada.getnextpage() #obtiene el url de la siguiente pagina
        #     if  next_page == False: #si no hay siguiente pagina, termina el ciclo
        #         break
        #     else:
        #         query = next_page #si hay siguiente pagina, cambia el query
        #     paginas_ahumada.append(f_ahumada) #agrega el objeto a la lista de paginas de ahumada


        lista_de_medicamentos_ahumada = []
        for pagina in self.paginas: #recorre la lista de paginas de ahumada
            f_ahumada_product_list = (pagina.get_product_list()) #obtiene la lista de productos de la pagina
            for producto in f_ahumada_product_list: #recorre la lista de productos de la pagina
                product_desc = producto.find("a",{"class" : "product-item-link"}).text #obtiene la descripcion del producto
                precio_clp = producto.find("span",{"class" : "price"}).text #obtiene el precio del producto
                precio_clp = precio_clp.replace("$","")
                precio_clp = int(precio_clp.replace(".",""))
                precio_uf = round(precio_clp / self.uf,2) #calcula el precio en uf
                medicamento_a = Medicamento(self.busqueda,"Ahumada", product_desc,precio_clp,precio_uf)
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



