

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import parser


class Ahumada():

    def __init__(self, busqueda):
        self.busqueda = busqueda

    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = 'https://www.farmaciasahumada.cl/catalogsearch/result/index/?p=1&q=' + self.busqueda
        return url
       
    

    def getdata(self):
        """Devuelve el html de la pagina"""
        s = HTMLSession()
        r = s.get(self.get_url())
        r.html.render(sleep=1,timeout=20)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        return soup


    def getnextpage(self):
        """Devuelve el url de la siguiente pagina"""

        soup = super(Ahumada, self).getdata()
        # soup = self.getdata() 
        page = soup.find("ul",{"class" : "items pages-items"})
        # print(page)
        if page.find("li",{"class":"item pages-item-next"}):
            print("hola")
            url = page.find("li",{"class":"item pages-item-next"}).find("a").attrs['href']
            return url
        else:
            return

    def get_product_list(self):
        """Devuelve una lista de productos"""
        soup = self.getdata()
        product_list = soup.findAll("li",{"class" : "item product product-item"})

        n = len(product_list)
        for i in range(0, n - 12 ):
            product_list.pop()
        return product_list



