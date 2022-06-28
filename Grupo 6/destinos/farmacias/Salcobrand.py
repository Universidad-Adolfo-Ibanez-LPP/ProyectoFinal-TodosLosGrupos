
from requests_html import HTMLSession
from bs4 import BeautifulSoup

from destinos.farmacias.Farmacia import *



class Salcobrand(Farmacia):

    def __init__(self, busqueda,url):
        self.busqueda = busqueda
        self.url = url


    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = "https://salcobrand.cl/search_result?query=" + self.busqueda
        return url
       
    

    # def _getdata(self):
    """funcion heredada de clase farmacia"""

    


    # def getnextpage(self):
    #     """Devuelve el url de la siguiente pagina"""
        
    #     soup = super(Salcobrand, self).getdata()
    #     page = soup.find("ul",{"class" : "items pages-items"})
    #     # print(page)
    #     if page.find("li",{"class":"item pages-item-next"}):
    #         print("hola")
    #         url = page.find("li",{"class":"item pages-item-next"}).find("a").attrs['href']
    #         return url
    #     else:
    #         return

    def get_product_list(self):
        """Devuelve una lista de productos"""
        soup = self._getdata()
        product_list = soup.findAll("li",{"class" : "ais-Hits-item"})

        # n = len(product_list)
        # for i in range(0, n - 12 ):
        #     product_list.pop()
        return product_list


    # print("chao")
    # print("chao")
    # print("chao")
    # print("chao")
