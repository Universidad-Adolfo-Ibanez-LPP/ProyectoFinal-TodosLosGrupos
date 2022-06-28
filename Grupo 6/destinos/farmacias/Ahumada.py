from requests_html import HTMLSession
from bs4 import BeautifulSoup
from csvOriented.Medicamento import *
from destinos.BancoUF import *
from destinos.farmacias.Farmacia import *
import csv


class Ahumada(Farmacia):

    def __init__(self, busqueda,url):
        self.busqueda = busqueda
        self.url = url



    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = self.url
        return url
       
    

    # def _getdata(self):
    """funcion heredada de clase farmacia"""

    def getnextpage(self):
        """Devuelve el url de la siguiente pagina"""

        soup = self._getdata()
        # soup = self._getdata() 
        # page = soup.find("ul",{"class" : "items pages-items"})
        # print(page)
        # print(page)
        try:
            url = soup.find_all("a",class_="action next")[0]["href"]
            return url
        except:
            return False

    def get_product_list(self):
        """Devuelve una lista de productos"""
        soup = self._getdata()
        product_list = soup.findAll("li",{"class" : "item product product-item"})

        n = len(product_list)
        for i in range(0, n - 12 ):
            product_list.pop()
        return product_list


