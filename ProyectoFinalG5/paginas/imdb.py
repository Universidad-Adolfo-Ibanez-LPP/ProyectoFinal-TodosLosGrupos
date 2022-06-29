from bs4 import BeautifulSoup
import requests
from termcolor import colored
import utils.objetos as objetos


def imdb(pelicula):

    #trycatch en caso de que no exista la pelicula
    try:
        #url de la pagina web con la pelicula ingresada 
        url_busqueda = "https://www.imdb.com/find?q=" + pelicula
        #tomar el html de la pagina
        busqueda = requests.get(url_busqueda)
        #parsear html
        soup = BeautifulSoup(busqueda.text, 'html.parser')

        #se rescata el link de la pelicula
        link_busqueda = soup.find("div", class_="findSection").find('a', href=True)
        link_pelicula = 'https://www.imdb.com/' + link_busqueda['href']
        #tomar el html de la pagina
        pelicula = requests.get(link_pelicula)
        #parsear html
        soup = BeautifulSoup(pelicula.text, 'html.parser')

        #se realiza webscraping para sacar los parametros necesarios
        titulo = soup.find("title").text 
        anio = soup.find("span", class_="sc-8c396aa2-2 itZqyK").text
        director = soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
        duracion = soup.find_all("li", class_="ipc-inline-list__item")
        duracion = duracion[5].text
        score = soup.find("span", class_="sc-7ab21ed2-1 jGRxWM").text
        cast = soup.find('div', class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid").find_all('a', class_="sc-18baf029-1 gJhRzH")
        
        #se crea una lista vacia para despues recorrer cast y cada "reparto" añadirlo a esta lista
        cast2 = []
        for reparto in cast:
            cast2.append(reparto.text)
        
        genero = soup.find_all("li", class_="ipc-inline-list__item ipc-chip__text")
        #se repite lo anterior con genero
        genero2 = []
        for reparto in genero:
            genero2.append(reparto.text)

        #se guarda el link de las reviews
        link_review = soup.find("div", class_="sc-66a20916-0 lQXVY", attrs={"data-testid":"reviews-header"}).find("a", href=True)
        link_reviews = 'https://www.imdb.com/' + link_review['href']
        #tomar el html de la pagina
        reviews = requests.get(link_reviews)
        #parsear html
        soup = BeautifulSoup(reviews.text, 'html.parser')

        #si no se encuentra ninguno printear "No hay review"
        review = soup.find("div", class_="text show-more__control")
        if review is None:
            review = "No hay review"
        else:
            review = review.text    
            
        #creacion de objeto de IMDB con los parametros establecidos
        obj_pelicula = objetos.Pelicula(titulo, anio, director, genero2, cast2, duracion, score, review)
        #se retorna el objeto
        return obj_pelicula

    except:
        print(colored("No se ha encontrado la pelicula. Verifique que este bien escrito el titulo.", "red"))
        exit
