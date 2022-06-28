from requests_html import HTMLSession
from bs4 import BeautifulSoup
from Medicamento import *
from BancoUF import *
import csv


class Ahumada():

    def __init__(self, busqueda,url):
        self.busqueda = busqueda
        self.url = url



    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = self.url
        return url
       
    

    def getdata(self):
        """Devuelve el html de la pagina"""
        s = HTMLSession()
        r = s.get(self.get_url())
        r.html.render(sleep=4,timeout=90)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        return soup


    def getnextpage(self):
        """Devuelve el url de la siguiente pagina"""

        soup = self.getdata()
        # soup = self.getdata() 
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
        soup = self.getdata()
        product_list = soup.findAll("li",{"class" : "item product product-item"})

        n = len(product_list)
        for i in range(0, n - 12 ):
            product_list.pop()
        return product_list


