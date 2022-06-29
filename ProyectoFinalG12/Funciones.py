import statistics

from Remedios import medicamentos
from functools import reduce


def Promedio_Activo(Activo):# promedio precio por activo entre todas las farmacias

    lista = list(filter(lambda x: x.activo == Activo, medicamentos))
    print(f"El precio promedio en CLP del activo {Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, lista,0)/len(lista),"\n")
    print(f"El precio promedio en UF del activo {Activo} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, lista,0)/len(lista),"\n")

def Promedio_Activo_Farmacia(Activo,Farmacia):# promedio precio por activo entre farmacia seleccionada

    lista = list(filter(lambda x: x.activo == Activo and x.farmacia == Farmacia, medicamentos))
    print(f"El precio promedio en CLP del activo {Activo} y de la farmacia {Farmacia} es: ")
    print(reduce(lambda suma, p: suma + p.precioClp, lista,0)/len(lista),"\n")
    print(f"El precio promedio en UF del activo {Activo} y de la farmacia {Farmacia} es: ")
    print(reduce(lambda suma, p: suma + p.precioUf, lista,0)/len(lista),"\n")


def Minimo_Farmacia(Activo, Farmacia):  # precio minimo en la farmacia seleccionada
    lista = list(filter(lambda x: x.activo == Activo and x.farmacia == Farmacia, medicamentos))
    Minimo_Farmacia = min(lista, key=lambda value: value.precioClp)
    print(" -- Minimo Farmacia -- ")
    print("Principio Activo: ", Minimo_Farmacia.activo, "\nFarmacia: ", Minimo_Farmacia.farmacia, "\nDescripcion: ", Minimo_Farmacia.descripcion,"\nPrecio min CLP: " ,Minimo_Farmacia.precioClp, "\nPrecio min UF: " ,Minimo_Farmacia.precioUf, "\n")

def Maximo_Farmacia(Activo, Farmacia):  # precio maximo en la farmacia seleccionada
    lista = list(filter(lambda x: x.activo == Activo and x.farmacia == Farmacia, medicamentos))
    Maximo_Farmacia = max(lista, key=lambda value: value.precioClp)
    print(" -- Maximo Farmacia -- ")
    print("Principio Activo: ", Maximo_Farmacia.activo, "\nFarmacia: ", Maximo_Farmacia.farmacia, "\nDescripcion: ",Maximo_Farmacia.descripcion,"\nPrecio min CLP: " ,Maximo_Farmacia.precioClp, "\nPrecio min UF: " ,Maximo_Farmacia.precioUf,"\n")

def Minimo_Activo(Activo):  # precio minimo entre todas las farmacias
    lista = list(filter(lambda x: x.activo == Activo, medicamentos))
    Minimo = min(lista, key=lambda value: value.precioClp)
    print(" -- Minimo Activo -- ")
    print("Principio Activo: ", Minimo.activo, "\nFarmacia: ", Minimo.farmacia, "\nDescripcion: ",Minimo.descripcion,"\nPrecio min CLP: " ,Minimo.precioClp, "\nPrecio min UF: " ,Minimo.precioUf,"\n")

def Maximo_Activo(Activo):  # precio maximo entre todas las farmacias
    lista = list(filter(lambda x: x.activo == Activo, medicamentos))
    Maximo = max(lista, key=lambda value: value.precioClp)
    print(" -- Minimo Activo -- ")
    print("Principio Activo: ", Maximo.activo, "\nFarmacia: ", Maximo.farmacia, "\nDescripcion: ",Maximo.descripcion,"\nPrecio min CLP: " ,Maximo.precioClp, "\nPrecio min UF: " ,Maximo.precioUf,"\n")

def Diferencia_Farmacia(Activo,Farmacia):   # diferencia entre precios de un activo en farmacia seleccionada
    lista = list(filter(lambda x: x.activo == Activo and x.farmacia == Farmacia, medicamentos))
    print(f"La diferencia entre el valor maximo y minimo del activo en Clp {Activo} en la farmacia {Farmacia} es:", (max(lista, key=lambda value: value.precioClp)).precioClp - (min(lista, key=lambda value: value.precioClp)).precioUf)
    print(f"La diferencia entre el valor maximo y minimo del activo en UF {Activo} en la farmacia {Farmacia} es:", (max(lista, key=lambda value: value.precioClp)).precioClp - (min(lista, key=lambda value: value.precioClp)).precioUf)

def Diferencia_Activo(Activo):  # diferencia entre precios de un activo entre todas las farmacias
    lista = list(filter(lambda x: x.activo == Activo, medicamentos))
    print(f"\nLa diferencia entre el valor maximo y minimo en Clp del activo {Activo} es:", (max(lista, key=lambda value: value.precioClp)).precioClp - (min(lista, key=lambda value: value.precioClp)).precioClp)
    print(f"La diferencia entre el valor maximo y minimo Uf del activo {Activo} es:",(max(lista, key=lambda value: value.precioClp)).precioUf - (min(lista, key=lambda value: value.precioClp)).precioUf,"\n")

def Mediana_Activo(Activo): #mediana entre todas las farmacias
    activos_filtrados = list(filter(lambda x: x.activo == Activo, medicamentos))
    activos_filtrados_precio = list(map(lambda p: p.precioClp,activos_filtrados))
    datos_mediana = statistics.median(activos_filtrados_precio)
    print(f"La mediana del activo {Activo} es: {datos_mediana}")


def Desviacion_Activo(Activo): #desviacion estandar entre todas las farmacias
    activos_filtrados = list(filter(lambda x: x.activo == Activo, medicamentos))
    activos_filtrados_precio = list(map(lambda p: p.precioClp,activos_filtrados))
    Desv_Farmacia = statistics.pstdev(activos_filtrados_precio)
    print(f"La desviacion estandar del activo {Activo} es: {Desv_Farmacia}" )
