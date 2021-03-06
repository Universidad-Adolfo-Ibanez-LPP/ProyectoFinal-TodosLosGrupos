from requests_html import HTMLSession
from bs4 import BeautifulSoup

class Farmacia:

    def __init__(self, busqueda,url):
        self.busqueda = busqueda
        self.url = url


    def get_busqueda(self):
        return self.busqueda

    def get_url(self):
        url = self.url
        return url
       
    def _getdata(self):
        """Devuelve el html de la pagina, el _ indica que esd una funcion privada"""
        try:
            s = HTMLSession()
            r = s.get(self.get_url())
            r.html.render(sleep=5,timeout=120)
            soup = BeautifulSoup(r.html.html, 'html.parser')
        except:
            print("Scrapping al farmacia falló, corra el programa nuevamente")
            exit()
        return soup
