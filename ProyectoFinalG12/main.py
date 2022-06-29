from DataManager import *
from Ahumada import *
import csv

from Farmazon import Farma
from Remedios import medicamentos
from Simi import Simi
from UFprice import getUFprice
from Funciones import *

# Si el codigo es muy lento, insertar menos principios activos a la vez 

def main():

    remedios = read_txt("principios_activos.txt")  # lee el txt con los activos
    Ahumada(remedios)  # llama al scraper
    Simi(remedios)  # llama al scraper
    Farma(remedios)  # llama al scraper
    getUFprice() # llama al scraper

    with open('Medicamentos.csv', 'w') as Medicamentos_csv:
        writer = csv.writer(Medicamentos_csv)
        for x in medicamentos:
            writer.writerow([x.activo, x.farmacia, x.descripcion, x.precioClp, x.precioUf])

    Csv('Medicamentos.csv')


    for Principio_Activo in remedios:

        #  Funciones estadisticas

        Promedio_Activo(Principio_Activo)

        Promedio_Activo_Farmacia(Principio_Activo, "Ahumada")
        Promedio_Activo_Farmacia(Principio_Activo, "Drsimi")
        Promedio_Activo_Farmacia(Principio_Activo, "Farmazon")

        Minimo_Farmacia(Principio_Activo, "Ahumada")
        Minimo_Farmacia(Principio_Activo, "Drsimi")
        Minimo_Farmacia(Principio_Activo, "Farmazon")

        Maximo_Farmacia(Principio_Activo, "Ahumada")
        Maximo_Farmacia(Principio_Activo, "Drsimi")
        Maximo_Farmacia(Principio_Activo, "Farmazon")

        Minimo_Activo(Principio_Activo)

        Maximo_Activo(Principio_Activo)

        Diferencia_Farmacia(Principio_Activo,"Ahumada")
        Diferencia_Farmacia(Principio_Activo, "Drsimi")
        Diferencia_Farmacia(Principio_Activo, "Farmazon")

        Diferencia_Activo(Principio_Activo)

        Mediana_Activo(Principio_Activo)

        Desviacion_Activo(Principio_Activo)

if __name__ == "__main__":
    main()
