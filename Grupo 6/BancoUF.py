from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests



class Banco():

    def get_url(self):
        url = 'https://www.bcentral.cl/inicio'
        return url

    def getdata(self):
        """Devuelve el html de la pagina"""
        s = HTMLSession()
        r = s.get(self.get_url())
        r.html.render(sleep=1,timeout=20)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        return soup

    def get_uf(self):
        """Devuelve el valor actual del UF"""
        soup = self.getdata()
        uf=soup.find('p' ,class_='basic-text fs-2 f-opensans-bold text-center c-blue-nb-2').text
        valor=uf.replace("$","")
        valor=valor.replace(".","")
        valor=valor.split(",")[0]
        return(valor)    