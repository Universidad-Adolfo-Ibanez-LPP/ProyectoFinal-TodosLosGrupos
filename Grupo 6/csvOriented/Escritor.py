from requests_html import HTMLSession
from bs4 import BeautifulSoup

from destinos.BancoUF import *

from csvOriented.Medicamento import *
import csv


class Escritor():

    def __init__(self,busqueda,uf,paginas):
        self.busqueda = busqueda
        self.uf = uf
        self.paginas = paginas



    def to_csv_ahumada(self):
        
        try:
            
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
        except Exception as e:
            print("Error al escribir en el csv de Ahumada! corra el archivo nuevamente!!")
            exit()


    def to_csv_salcobrand(self):
        try:

            lista_de_medicamentos_salcobrand=[]
            for pagina in self.paginas:
                f_salcobrand_product_list = (pagina.get_product_list())
                for producto in f_salcobrand_product_list:
            
                    product_desc = producto.find("span",{"class" : "product-info truncate"}).text
                    precio_clp = producto.find("div",{"class" : "sale-price"}).text
                    precio_clp = precio_clp.replace("$","")
                    precio_clp = precio_clp.replace(".","")
                    precio_clp = precio_clp.replace("Oferta:","")
                    precio_uf = int(precio_clp) / self.uf
                    precio_uf = round(precio_uf,2)
                    medicamento_b= Medicamento(self.busqueda,"Salcobrand", product_desc,precio_clp,precio_uf)
                    lista_de_medicamentos_salcobrand.append(medicamento_b)
                    with open('out.csv', 'a', newline='',encoding='utf8') as f_object:  
                        # Pass the CSV  file object to the writer() function
                        writer_object = csv.writer(f_object)
                        # Result - a writer object
                        # Pass the data in the list as an argument into the writerow() function
                        writer_object.writerow(medicamento_b.a_lista())  
                        # Close the file object
                        f_object.close()
        except Exception as e:
            print("Error al escribir en el csv de Salcobrand! corra el archivo nuevamente!!")
            exit()
    
    def to_csv_red(self):

        try:
            lista_de_medicamentos_salcobrand=[]
            for pagina in self.paginas:
                f_red_product_list = (pagina.get_product_list())
                for producto in f_red_product_list:
        
                    product_desc = producto.find("div",{"class" : "nombre"}).text
                    precio_clp = producto.find("div",{"class" : "normal"}).text
                    precio_clp = precio_clp.replace("$","")
                    precio_clp = precio_clp.replace(".","")
                    precio_clp = precio_clp.replace("Normal:","")
                    precio_clp = precio_clp.replace("\n","")
                    if (precio_clp == ""):
                        #El ultimo item se entrega vacio, por eso se ignora
                        break
                    precio_uf = int(precio_clp) / self.uf
                    precio_uf = round(precio_uf,2)

                    medicamento_b= Medicamento(self.busqueda,"RedFarma", product_desc,precio_clp.strip(),precio_uf)
                    lista_de_medicamentos_salcobrand.append(medicamento_b)
                    with open('out.csv', 'a', newline='',encoding='utf8') as f_object:  
                        # Pass the CSV  file object to the writer() function
                        writer_object = csv.writer(f_object)
                        # Result - a writer object
                        # Pass the data in the list as an argument into the writerow() function
                        writer_object.writerow(medicamento_b.a_lista())  
                        # Close the file object
                        f_object.close()
        except Exception as e:
            print("Error al escribir en el csv de RedFarma! corra el archivo nuevamente!!")
            exit()