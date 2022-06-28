
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import parser


class Salcobrand():

    def __init__(self, farmacia, busqueda):
        self.farmacia = farmacia
        self.busqueda = busqueda


    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = "https://salcobrand.cl/search_result?query=" + self.busqueda
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
        
        soup = super(Salcobrand, self).getdata()
        page = soup.find("ul",{"class" : "items pages-items"})
        # print(page)
        if page.find("li",{"class":"item pages-item-next"}):
            print("hola")
            url = page.find("li",{"class":"item pages-item-next"}).find("a").attrs['href']
            return url
        else:
            return


    # print("chao")
    # print("chao")
    # print("chao")
    # print("chao")
