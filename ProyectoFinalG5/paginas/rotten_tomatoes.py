from bs4 import BeautifulSoup
import requests
from termcolor import colored
import utils.objetos as objetos

def rotten_tomatoes(pelicula):

    #trycatch en caso de que no exista la pelicula
    try:
        #url de la pagina web con la pelicula ingresada
        url_busqueda = "https://www.rottentomatoes.com/search?search=" + pelicula
        #tomar el html de la pagina
        busqueda = requests.get(url_busqueda)
        #parsear html
        soup_busqueda = BeautifulSoup(busqueda.text, "html.parser")

        #se rescata el link de la pelicula
        link_busqueda = soup_busqueda.find("search-page-result", slot="movie").find('a', href=True)
        link_pelicula = link_busqueda["href"]
        #tomar el html de la pagina
        pelicula = requests.get(link_pelicula)
        #parsear html
        soup_pelicula = BeautifulSoup(pelicula.text, "html.parser")

        #se realiza webscraping para sacar los parametros necesarios
        titulo = soup_pelicula.find("h1", class_="scoreboard__title").text
        score = soup_pelicula.find("score-board", class_="scoreboard")['audiencescore']
        genero = (soup_pelicula.find("div", class_="meta-value genre").text).split()
        
        #se crea una lista vacia para despues recorrer cast y cada "reparto" añadirlo a esta lista
        cast = soup_pelicula.find_all("span", class_="characters subtle smaller")
        cast2 = []
        for reparto in cast:
            cast2.append(reparto.attrs['title'])

        publicacion = soup_pelicula.find_all("time")[0].text

        #almacenamiento de todas las secciones "time" en un arreglo
        duracion = soup_pelicula.find_all("time")
        #si este tiene mas de 2 elementos duracion sera igual al tercer elemento, de caso contrario sera igual al segundo elemento
        if len(duracion) > 2:
            duracion = (duracion[2].text).strip()
        else:
            duracion = (duracion[1].text).strip()

        director = soup_pelicula.find_all("div", class_="meta-value")[3].text
        review = soup_pelicula.find("div", class_="mop-audience-reviews__review--comment clamp clamp-4 js-clamp")
        #si no se encuentra ninguno printear "No hay review"
        if review is None:
            review = "No hay review"
        else:
            review = review.text

        #creacion de objeto de Rotten Tomatoes con los parametros establecidos
        obj_pelicula = objetos.Pelicula(titulo, publicacion, director, genero, cast2, duracion, score, review)
        #se retorna el objeto
        return obj_pelicula

    except:
        print(colored("No se ha encontrado la pelicula. Verifique que este bien escrito el titulo.", "red"))
        exit()