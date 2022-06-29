import csv
import utils.objetos as objetos
from functools import reduce

#función que lee el archivo csv y guarda las filas en un array
def leer():
    rows = []
    with open("historial.csv", "r", encoding="utf8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    #se crea el objeto de Datos
    datos = objetos.Datos

    #funcion que obtiene los minutos de las peliculas en el historial
    def minutos(lista):
        largo = []
        for fila in lista:
            largo.append(fila[3])
        largo = list(map(int, largo))
        if(len(largo)>1):
            #minimo y maximo de minutos entre todas las peliculas del historial
            datos.min_largo = min(largo)
            datos.max_largo = max(largo)

    #funcion que obtiene los años de las peliculas en el historial
    def anio(lista):
        anios = []
        for fila in lista:
            anios.append(fila[1])
        anios = list(map(int, anios))
        if(len(anios)>1):
            #minimo y maximo entre los años todas las peliculas del historial
            datos.min_anio = min(anios)
            datos.max_anio = max(anios)

    #funcion que obtiene los puntajes de las peliculas en el historial
    def promedio(lista):
        scores = []
        for fila in lista:
            scores.append(fila[4])
        scores = list(map(float, scores))
        if(len(scores)>1):
            #promedio de puntaje entre todas las peliculas del historial
            promedio_score = reduce(lambda x, y: (x+y), scores)/len(scores)
            #redondear el resultado
            promedio_redondeado = round(promedio_score, 1)
            datos.promedio = promedio_redondeado

    minutos(rows)
    anio(rows)
    promedio(rows)

    return datos
