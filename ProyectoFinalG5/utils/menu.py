import paginas.letterboxd as letterboxd
import paginas.imdb as imdb
import utils.calculo_peliculas as calculo_peliculas
import csv
import archivo.lectura_csv as lectura_csv


def menu():
    #guardar pelicula que el usuario entrega
    busqueda = input("Ingrese la pelicula a buscar: ")

    #crear objetos de pelicula buscada
    pelicula = letterboxd.letterboxd(busqueda)
    generos = imdb.imdb(busqueda).genero
    conjunto = calculo_peliculas.peliculas(busqueda)

    #imprime todos los parametros de la pelicula consultada
    #estadisticos son promedio de puntaje, minimo de puntaje, maximo de puntaje, minimo y maximo de duracion del historial, 
    #minimo y maximo de aÃ±o del historial, y promedio de puntaje del historial
    print("------------------")
    print("Resultado de la busqueda: ")
    print("")
    print("Titulo:", pelicula.titulo)
    print("")
    print("Lanzamiento:", pelicula.anio)
    print("")
    print("Director:", pelicula.director)
    print("")
    print("Elenco:")
    print('\n' .join(pelicula.cast))
    print("")
    print("Duracion:", pelicula.duracion)
    print("")
    print("Generos:")
    print('\n' .join(generos))
    print("")
    print("Puntaje promedio entre las paginas:", str(conjunto.promedio) + "/10")
    print("")
    print("Minimo puntaje entre las paginas:", str(conjunto.minimo)+ "/10")
    print("")
    print("Maximo puntaje entre las paginas:", str(conjunto.maximo)+ "/10")
    print("")
    print("Review Letterboxd:", conjunto.reviews[0])
    print("")
    print("Review IMDB:", conjunto.reviews[1])
    print("")
    print("Review Rotten Tomatoes:", conjunto.reviews[2])
    print("------------------")

    #guardar datos de la pelicula (titulo, anio, director, duracion, promedio) en un archivo csv
    with open('historial.csv', 'a', newline='',encoding='utf8') as f_object:
        duracion = pelicula.duracion.split('\xa0')[0]
        writer_object = csv.writer(f_object)
        writer_object.writerow([pelicula.titulo, pelicula.anio, pelicula.director, duracion, conjunto.promedio])
    
    #obtner datos de la lectura de archivo csv
    datos = lectura_csv.leer()

    #imprimir estadisticos del historial
    print("Datos del historial:")
    print("Duracion de la pelicula mas corta:", str(datos.min_largo)+" min")
    print("Duracion de la pelicula mas larga:", str(datos.max_largo)+" min")
    print("Lanzamiento de la pelicula mas antigua:", datos.min_anio)
    print("Lanzamiento de la pelicula mas reciente:", datos.max_anio)
    print("Promedio de puntajes:", str(datos.promedio)+ "/10")
    print("------------------")
