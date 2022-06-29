from bs4 import BeautifulSoup
import requests
import pandas as pd
#instale estas librerias si no las tiene y para correrlo desde la terminal ocupe python (ubicación del archivo en el directorio)/main.py ó, si no funciona en el terminal, y de forma mucho más sencilla para nosotros, descargue el archivo zip, súbalo a replit y córralo allí

class WebScraperAhumada(object): #scrapear desde ahumada

    def __init__(self,principios_activos): #definimos los atributos del objeto 
      self.principios_activos = principios_activos #parametro
      self.max_page = self.find_max_page()        
      self.lista_anticonceptivos = lista_anticonceptivos       
      self.precios_anticonceptivos = precios_anticonceptivos

    def run(self):
      #falta sacar este loop
      for url in self.generate_pages_to_scrape():
          anticonceptivos_pagina = self.scrape_page(url)
          self.lista_anticonceptivos += anticonceptivos_pagina #vamos agregando resultados

    def create_url(self):
        return "https://www.farmaciasahumada.cl/catalogsearch/result/?q=anticonceptivos"

    def create_paginated_url(self, page_number): #creamos la pag siguiente de resultados

        if page_number == 1:
          return self.create_url()
        else:
          return "https://www.farmaciasahumada.cl/catalogsearch/result/index/?p="+str(page_number)+"&q=anticonceptivos"

    def find_max_page(self): #retorna el num. de pags. de los resultados
 
      r = requests.get(self.create_url())
      soup = BeautifulSoup(r.content, "lxml")
      pagination_soup = soup.findAll("strong", {"class": "page"})
      pagination = (pagination_soup)[0]
      page_text = pagination("span",class_=False)[0].text
      return int(page_text.replace('Page 1 of ', ''))

    def generate_pages_to_scrape(self): #buscar todas las paginas por el num. max.

      return [self.create_paginated_url(page_number) for page_number in range(1, self.max_page + 1)]

    def get_links():
       return [x.find('a').get('href') for x in (s.find_all('div',class_="product details product-item-details"))]

    def scrape_page(self, url):

      r = requests.get(url)
      soup = BeautifulSoup(r.content, "lxml")
      data = soup.findAll("li", {"class": "item product product-item"})
  
      lista_anticonceptivos = list()
      precios_anticonceptivos = list()

      for item in data: #uso de paradigma procedural
        nombre = item.find_all("p", {"class": "product-brand-name truncate"})[0].text
        lista_anticonceptivos.append(nombre)
        precio =  item.find_all("span", {"class": "price"})[0].text
        precios_anticonceptivos.append(precio)
      return lista_anticonceptivos,precios_anticonceptivos


class WebScraperDrSimi(object): #scrapear datos desde dr. simi

    def __init__(self,principios_activos): #definimos los atributos del objeto
      self.principios_activos = principios_activos #input
      self.max_page = self.find_max_page() #numero de pag. de la pagina
      self.lista_anticonceptivos = lista_anticonceptivos   
      self.precios_anticonceptivos = precios_anticonceptivos

    def run(self):
        #falta sacar este loop
        for url in self.generate_pages_to_scrape():
            anticonceptivos_pagina = self.scrape_page(url)
            self.lista_anticonceptivos += anticonceptivos_pagina 

    def create_url(self): #creamos la url base de resultados
        return "https://www.drsimi.cl/medicamento/salud-femenina/anticonceptivos.html"

    def create_paginated_url(self, page_number): #creamos la pag siguiente de resultados
        if page_number == 1:
          return self.create_url()
        else:
          return "https://www.drsimi.cl/medicamento/salud-femenina/anticonceptivos.html?p="+str(page_number)

    def find_max_page(self): #retorna el num. de pags. de los resultados
 
      r = requests.get(self.create_url())
      soup = BeautifulSoup(r.content, "lxml")
      pagination_soup = soup.findAll("strong", {"class": "page"}
      pagination = pagination_soup[0]
      page_text = pagination("span")[0].text
      return int(page_text.replace('Page 1 of ', ''))

    def generate_pages_to_scrape(self): #buscar todas las paginas por el num. max.

      return [self.create_paginated_url(page_number) for page_number in range(1, self.max_page + 1)]

    def get_links():
      
     return [x.find('a').get('href') for x in (s.find_all('div',class_="product-item-link"))]
    
    def scrape_page(self, url):

      r = requests.get(url)
      soup = BeautifulSoup(r.content, "lxml")
      data = soup.findAll("div", {"class": "product-item-info type1"})
  
      lista_anticonceptivos = list()
      precios_anticonceptivos = list()

      for item in data: #uso de paradigma procedural
        nombre = item.find_all("a", class_= "product-item-link")[0].text
        lista_anticonceptivos.append(nombre)
        precio =  item.find_all("span", {"class": "price"})[0].text
        precios_anticonceptivos.append(precio)
      return lista_anticonceptivos,precios_anticonceptivos
