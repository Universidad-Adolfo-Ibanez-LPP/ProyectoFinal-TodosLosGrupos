from requests_html import HTMLSession
from bs4 import BeautifulSoup
from csvOriented.Medicamento import *
from destinos.BancoUF import *
from destinos.farmacias.Farmacia import *
import csv


class RedFarma(Farmacia):

    def __init__(self, busqueda,url):
        self.busqueda = busqueda
        self.url = url



    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = self.url
        return url

    def is_valid_page(self):
        """Devuelve si esta page es valida"""

        soup = self._getdata()

        return soup.find("div",class_="borde")


    def get_product_list(self):
        """Devuelve una lista de productos"""
        soup = self._getdata()
        product_list = soup.findAll("div",{"class" : "producto"})

        n = len(product_list)
        for i in range(0, n - 8 ):
            product_list.pop()
        return product_list
