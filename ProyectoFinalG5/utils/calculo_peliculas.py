from functools import reduce

import utils.objetos as objetos
import paginas.letterboxd
import paginas.imdb
import paginas.rotten_tomatoes

def peliculas(pelicula):
    #se crean las variables que almacenan los objetos retornados por cada pagina
    peliculaLetterboxd = paginas.letterboxd.letterboxd(pelicula)
    peliculaImdb = paginas.imdb.imdb(pelicula)
    peliculaRottenTomatoes = paginas.rotten_tomatoes.rotten_tomatoes(pelicula)

    #funcion para convertir string a float
    def aNum(x):
        return float(x)

    #se hace un map de los score de cada pagina con la funcion anterior
    lista_scores = list(map(aNum, (peliculaLetterboxd.score, peliculaImdb.score, peliculaRottenTomatoes.score)))

    #funcion para convertir los scores a la misma escala
    def convList(x, contador):
        if(contador == len(x)-1):
            x[contador] = x[contador]/10
        else:
            if(contador == 0):
                x[contador] = x[contador]*2
                return convList(x, contador +1)
            else:
                return convList(x, contador +1)
    convList(lista_scores, 0)

    #minimo de la lista_scores con funcion reduce
    minimo = reduce(lambda x, y: x if x < y else y, lista_scores)
    #redondear minimo a un decimal
    minimo_redondeado = round(minimo, 1)

    #maximo de la lista_scores con funcion reduce
    maximo = reduce(lambda x, y: x if x > y else y, lista_scores)
    #redondear maximo a un decimal
    maximo_redondeado = round(maximo, 1)

    #calcular el promedio de los scores
    promedio_score = reduce(lambda x, y: (x+y), lista_scores)/len(lista_scores)
    #redondear el resultado
    promedio_redondeado = round(promedio_score, 1)

    #crear una lista vacia y agregarle la review de cada pagina
    lista_reviews = []
    lista_reviews.append(peliculaLetterboxd.review)
    lista_reviews.append(peliculaImdb.review)
    lista_reviews.append(peliculaRottenTomatoes.review)

    #crear el objeto de el promedio calculado y la lista de reviews
    conjunto = objetos.Conjunto(promedio_redondeado, minimo_redondeado, maximo_redondeado, lista_reviews)
    #retornar objeto
    return conjunto
