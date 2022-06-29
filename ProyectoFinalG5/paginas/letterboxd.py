from bs4 import BeautifulSoup
import requests
from termcolor import colored
import utils.objetos as objetos

def letterboxd(pelicula):

    #trycatch en caso de que no exista la pelicula
    try:
        #url de la pagina web con la pelicula ingresada 
        url_busqueda = "https://letterboxd.com/search/films/" + pelicula
        #tomar el html de la pagina
        busqueda = requests.get(url_busqueda)
        #parsear html
        soup = BeautifulSoup(busqueda.text, 'html.parser')

        #se rescata el link de la pelicula
        link_busqueda = soup.find("span", class_="film-title-wrapper").find('a', href=True)
        link_pelicula = 'https://letterboxd.com' + link_busqueda['href']
        #tomar el html de la pagina
        pelicula = requests.get(link_pelicula)
        #parsear html
        soup = BeautifulSoup(pelicula.text, 'html.parser')

        #se realiza webscraping para sacar los parametros necesarios
        titulo = soup.find("h1", class_="headline-1 js-widont prettify").text
        anio = soup.find("small", class_="number").text
        director = soup.find("span", class_="prettify").text
        #recorrer las secciones "a" que contiene tab-cast y guardarlas en un array
        cast = [line.contents[0] for line in soup.find('div', attrs={'id':'tab-cast'}).find_all('a')]
        duracion = soup.find("p", class_="text-link text-footer").text.split(' ')[0].strip()

        #recorrer las secciones "meta" para encontrar el score
        for tag in soup.find_all("meta"):
            if tag.get("name", None) == "twitter:data2":
                score = tag.get("content", None)
        score = score.split(" ")[0]

        #para encontrar los reviews ocultos como spoilers
        #si no se encuentra ninguno printear "No hay review"
        if soup.find("div", class_="hidden-spoilers expanded-text"):
            review = soup.find("div", class_="hidden-spoilers expanded-text").find("p")
            if review is None:
                review = "No hay review"
            else:
                review = review.text   
        else:
            review = soup.find("div", class_="body-text -prose collapsible-text").find("p")
            if review is None:
                review = "No hay review"
            else:
                review = review.text   

        #se guarda el link de los generos
        link_generos = link_pelicula + "genres/"
        #tomar el html de la pagina
        genero = requests.get(link_generos)
        #parsear html
        soup = BeautifulSoup(genero.text, 'html.parser')
        #recorrer las secciones "a" que contiene text-sluglist capitalize y guardarlas en un array 
        generos = [line.contents[0] for line in soup.find('div', class_="text-sluglist capitalize").find_all('a')]

        #creacion de objeto de Letterboxd con los parametros establecidos
        obj_pelicula = objetos.Pelicula(titulo, anio, director, generos, cast, duracion, score, review)
        #se retorna el objeto
        return obj_pelicula

    except:
        print(colored("No se ha encontrado la pelicula. Verifique que este bien escrito el titulo.", "red"))
        exit()