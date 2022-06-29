import math
import pandas as pd

# estadistico 1 maximo
def Max_(arr, max_=None):
    arr_aux = arr.copy()
    if (max_ is None):  # Caso inicial en donde la no hay un valor maximo.
        max_ = arr_aux.pop()  # Va ir cortando la lista desde el primer elemto.
    current = arr_aux.pop()
    if (current > max_):  # En caso del que el valor cortado de la lista sea mayor el max_ se cambia
        max_ = current
    if (arr_aux):  # Si la lista no esta vacia se vuelve a iterar de forma recursiva.
        return Max_(arr_aux, max_)
    return max_

def medicamentoMin(array, i, min_price):
    if (array[i].precio == min_price):
        return array[i]
    return medicamentoMin(array, i + 1, min_price)

def minPrice(array, lista_precio_uf):
    min_price = (Min_(lista_precio_uf))
    return medicamentoMin(array, 0, min_price)

def medicamentoMax(array, i, max_price):
    if (array[i].precio == max_price):
        return array[i]
    return medicamentoMax(array, i + 1, max_price)

def maxPrice(array, lista_precio_uf):
    max_price = (Max_(lista_precio_uf))
    return medicamentoMax(array, 0, max_price)

# estadistico 2 minimo
def Min_(arr, min_=None):
    arr_aux = arr.copy()
    if (min_ is None):  # Caso inicial en donde la no hay un valor minimo.
        min_ = arr_aux.pop()

    current = arr_aux.pop()

    if (current < min_):  # En caso del que el valor cortado de la lista sea menor el min_ se cambia
        min_ = current
    if (arr_aux):  # Si la lista no esta vacia se vuelve a iterar de forma recursiva.
        return Min_(arr_aux, min_)
    return min_

# Estadistico 3 suma elemtos de la lista
def Sum_(numList):
    if (len(numList) == 1):  # Caso en que la lista este tenga 1 elemento.
        return numList[0]  # Retorna el elemento que esta primero en la lista
    else:
        return numList[0] + Sum_(numList[1:])  # la lista se va ir va a tomar el segundo elemento

# estadistico 4 cantidad
def list_length(L):
    if L:  # Caso en que la lista este no vacia.
        return 1 + list_length(L[1:])  # se va a ir contando la lista.
    else:  # Caso en que la lista este vacia vale.
        return 0

# estadistico 5 mean
def Mean(lista):
    return Sum_(lista) / list_length(lista)

# estadistico 6 VARIANZA
def varianza(numList, u, n):
    if len(numList) == 1:
        return ((numList[0] - u) ** 2) / (n - 1)
    else:
        return ((numList[0] - u) ** 2) / (n - 1) + varianza(numList[1:], u, (n))

# estadistico 7 deviacion estandar
def desvia_estantar(numList, u, n):
    return math.sqrt(varianza(numList, u, n))

# Estadistico 8
def cuartiles(lista, Q):
    lista_sort = sorted(lista, key=lambda x: int(x))
    N = list_length(lista)
    if (list_length(lista) % 2 != 0):
        pos = round(Q * (N + 1) / 4)
        return lista_sort[pos]
    else:
        pos = round(Q * (N) / 4)
        return lista_sort[pos]

# Estadictico 9
def frecuenciaRangoPrecio(df):
    print((pd.cut(df[['Precio']].values.flatten(), bins=[0,1000,2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 50000, 100000, 1000000]).value_counts()).add_prefix('count'))