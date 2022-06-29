from UF import UF
from data_manager import Archivo as A
from farmacias import Simi as S
from farmacias import Ahumada as Ahu
from farmacias import Farmex as F
from datetime import date
import pandas as pd
from estadisticas import Estadistico
import sys

#Variables:

path = r'C:\Users\drago\PycharmProjects\Scrapping' #Ruta donde se irán guardando los csv.
banco = UF.BancoCentral("https://portalbiblioteca.bcentral.cl/web/banco-central/inicio") #Se crea el objeto de banco.
uf_price = banco.find_Uf() #Se obtiene el valor de la UF.
manager = A.Archivo() #Se crea el manager de archivos.

dr_simi = S.simi('Dr. Simi', 'https://www.drsimi.cl/?gclid=CjwKCAjwzeqVBhAoEiwAOrEmzUsmFhzyBClMLg782m40-Xhn626Pz7fjO2XgsAirx8K7R0YTLuS4ihoChhwQAvD_BwE')
ahumada = Ahu.ahumada('Ahumada', 'https://www.farmaciasahumada.cl/?gclid=CjwKCAjwzeqVBhAoEiwAOrEmzY0TN6rgym8yI99I887uc7Y2WgA0rK9L3XJOt380V7JOsT3hgR1qtBoC1egQAvD_BwE')
farmex = F.farmex('Farmex', 'https://farmex.cl/')

#Captura de valor de UF hacia csv.
parametros = pd.DataFrame({'Fecha captura': date.today(), 'Valor UF':uf_price}, index = [0]) #Dataframe que contiene la fecha cuando se saca el valor de la UF, y el valor como tal.
manager.toCSV(parametros, 'no farmacia', path, 0) #Se pasa el dataframe a .csv y se exporta.

#Leemos el archivo de principios activos. Se guarda en una lista.
principios_activos = manager.ReadCVS(path, sys.argv[1])

#'principios_activos.txt'

scrapping_number = 0
for i in principios_activos:

    find = i
    print(find)
    scrapping_number += 1
    #Farmacia Dr. Simi.

    lista_nombre_simi, lista_info_simi, lista_precio_simi, lista_farmacia_simi = dr_simi.GetData(find) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.

    lista_precio_uf_simi = dr_simi.precio_to_UF(lista_precio_simi, uf_price) #Se crea la lista de precios UF de cada producto.

    df_simi = manager.toDF(lista_nombre_simi, lista_info_simi, lista_precio_simi, lista_precio_uf_simi, lista_farmacia_simi) #Se crea el data frame con los datos.
    #manager.toCSV(df_simi, 'Dr. Simi', path) #Se crea un archivo csv con los datos extraidos.

    medicamentos_simi =  dr_simi.GetObjectList(lista_nombre_simi, lista_info_simi, lista_precio_simi, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

    ####################

    #Farmacia Ahumada

    lista_nombre_ahumada, lista_info_ahumada, lista_precio_ahumada, lista_farmacia_ahumada = ahumada.GetData(find) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.
    lista_precio_uf_ahumada = ahumada.precio_to_UF(lista_precio_ahumada, uf_price) #Se crea la lista de precios UF de cada producto.
    df_ahumada = manager.toDF(lista_nombre_ahumada, lista_info_ahumada, lista_precio_ahumada, lista_precio_uf_ahumada, lista_farmacia_ahumada) #Se crea el data frame con los datos.
    #manager.toCSV(df_ahumada, 'Ahumada', path) #Se crea un archivo csv con los datos extraidos.
    medicamentos_ahumada = ahumada.GetObjectList(lista_nombre_ahumada, lista_info_ahumada, lista_precio_ahumada, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

    ###################

    #Farmacia Farmex

    lista_nombre_farmex, lista_info_farmex, lista_precio_farmex, lista_farmacia_farmex, lista_precio_uf_farmex = farmex.getData(farmex.Get_LastPage(find), find) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.
    df_farmex = manager.toDF(lista_nombre_farmex, lista_info_farmex, lista_precio_farmex, lista_precio_uf_farmex, lista_farmacia_farmex) #Se crea el data frame con los datos.
    #manager.toCSV(df_farmex, 'Farmex', path) #Se crea un archivo csv con los datos extraidos.
    medicamentos_farmex = farmex.GetObjectList(lista_nombre_farmex, lista_info_farmex, lista_precio_farmex, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

    ###################

    #csv final.
    df_final = manager.joinDF(df_simi, df_farmex, df_ahumada) #Se juntan los dataframes de las farmacias en uno solo.
    manager.toCSV(df_final, 'Final', path, scrapping_number) #Se crea un archivo csv con los datos finales.

    #Estadisticas (NO FUNCIONAN POR ERROR DE ULTIMO MOMENTO)

    # DR.SIMI
    # -------------------------------------------------------------------------
    simi_med_min = Estadistico.minPrice(medicamentos_simi, lista_precio_simi)
    print('\nMedicamento con el precio mínimo (DR SIMI):')
    print('Nombre:', simi_med_min.nombre, '\nFarmacia: Dr.Simi', '\nDescripción:', simi_med_min.info.strip(),
          '\nPrecio:', simi_med_min.precio, '\nPrecio UF:', simi_med_min.precioUF)

    #simi_med_max = Estadistico.maxPrice(medicamentos_simi, lista_precio_simi)
    #print('\nMedicamento con el precio máximo (DR SIMI):')
    #print('Nombre:', simi_med_max.nombre, '\nFarmacia: Dr.Simi', '\nDescripción:', simi_med_max.info.strip(), '\nPrecio:', simi_med_max.precio, '\nPrecio UF:', simi_med_max.precioUF)

    print('\nPrecio promedio (DR SIMI):')
    simi_mean_price = Estadistico.Mean(lista_precio_simi)
    simi_mean_price_UF = Estadistico.Mean(lista_precio_uf_simi)
    #print('Nombre:', simi_med_max.nombre, '\nFarmacia: Dr.Simi', '\nPrecio promedio:', simi_mean_price, '\nPrecio Promedio UF:', simi_mean_price_UF)

    print("\nQuartiles (precio) (DR SIMI):")
    print("Q1:", Estadistico.cuartiles(lista_precio_simi, 1))
    print("Q2:", Estadistico.cuartiles(lista_precio_simi, 2))
    print("Q3:", Estadistico.cuartiles(lista_precio_simi, 3))

    n = Estadistico.list_length(lista_precio_simi)
    print("\nDesviación Estándar (precio) (DR SIMI):", Estadistico.desvia_estantar(lista_precio_simi, simi_mean_price, n))
    print("\nVarianza:", Estadistico.varianza(lista_precio_simi, simi_mean_price, n))
    print('\nProductos totales encontrados:', len(lista_nombre_simi))

    # -------------------------------------------------------------------------

    # AHUMADA
    # -------------------------------------------------------------------------
    ahu_med_min = Estadistico.minPrice(medicamentos_ahumada, lista_precio_ahumada)
    print('\nMedicamento con el precio mínimo (AHUMADA):')
    print('Nombre:', ahu_med_min.nombre, '\nFarmacia: Ahumada', '\nDescripción:', ahu_med_min.info.strip(), '\nPrecio:',
          ahu_med_min.precio, '\nPrecio UF:', ahu_med_min.precioUF)

    ahu_med_max = Estadistico.maxPrice(medicamentos_ahumada, lista_precio_ahumada)
    print('\nMedicamento con el precio máximo (AHUMADA):')
    print('Nombre:', ahu_med_max.nombre, '\nFarmacia: Ahumada', '\nDescripción:', ahu_med_max.info.strip(), '\nPrecio:',
          ahu_med_max.precio, '\nPrecio UF:', ahu_med_max.precioUF)

    print('\nPrecio promedio (AHUMADA):')
    ahu_mean_price = Estadistico.Mean(lista_precio_ahumada)
    ahu_mean_price_UF = Estadistico.Mean(lista_precio_uf_ahumada)
    print('Nombre:', ahu_med_max.nombre, '\nFarmacia: Ahumada', '\nPrecio promedio:', ahu_mean_price,
          '\nPrecio Promedio UF:', ahu_mean_price_UF)

    print("\nQuartiles (precio) (AHUMADA):")
    print("Q1:", Estadistico.cuartiles(lista_precio_ahumada, 1))
    print("Q2:", Estadistico.cuartiles(lista_precio_ahumada, 2))
    print("Q3:", Estadistico.cuartiles(lista_precio_ahumada, 3))

    n = Estadistico.list_length(lista_precio_ahumada)
    print("\nDesviación Estándar (precio) (AHUMADA):", Estadistico.desvia_estantar(lista_precio_ahumada, ahu_mean_price, n))
    print("\nVarianza:", Estadistico.varianza(lista_precio_ahumada, ahu_mean_price, n))
    print('\nProductos totales encontrados:', len(lista_nombre_ahumada))

    # FARMEX
    # -------------------------------------------------------------------------
    far_med_min = Estadistico.minPrice(medicamentos_farmex, lista_precio_farmex)
    print('\nMedicamento con el precio mínimo (FARMEX):')
    print('Nombre:', far_med_min.nombre, '\nFarmacia: Farmex', '\nDescripción:', far_med_min.info.strip(), '\nPrecio:',
          far_med_min.precio, '\nPrecio UF:', far_med_min.precioUF)

    far_med_max = Estadistico.maxPrice(medicamentos_farmex, lista_precio_farmex)
    print('\nMedicamento con el precio máximo: (FARMEX)')
    print('Nombre:', far_med_max.nombre, '\nFarmacia: Farmex', '\nDescripción:', far_med_max.info.strip(), '\nPrecio:',
          far_med_max.precio, '\nPrecio UF:', far_med_max.precioUF)

    print('\nPrecio promedio (FARMEX):')
    far_mean_price = Estadistico.Mean(lista_precio_farmex)
    far_mean_price_UF = Estadistico.Mean(lista_precio_uf_farmex)
    print('Nombre:', far_med_max.nombre, '\nFarmacia: Farmex', '\nPrecio promedio:', far_mean_price,
          '\nPrecio Promedio UF:', far_mean_price_UF)

    print("\nQuartiles (precio) (FARMEX):")
    print("Q1:", Estadistico.cuartiles(lista_precio_farmex, 1))
    print("Q2:", Estadistico.cuartiles(lista_precio_farmex, 2))
    print("Q3:", Estadistico.cuartiles(lista_precio_farmex, 3))

    n = Estadistico.list_length(lista_precio_ahumada)
    print("\nDesviación Estándar (precio):", Estadistico.desvia_estantar(lista_precio_farmex, far_mean_price, n))
    print("\nVarianza:", Estadistico.varianza(lista_precio_farmex, far_mean_price, n))
    print('\nProductos totales encontrados:', len(lista_nombre_farmex))

    # PRECIOS POR PRINCIPIO ACTIVO
    print('\nPrecios por principio activo: Dr.Simi')
    #print('Nombre:', simi_med_max.nombre, '\nPrecio mínimo:', simi_med_min.precio, '\nPrecio máximo:', simi_med_max.precio, '\nPrecio promedio:', simi_mean_price, '\nPrecio Promedio UF:', simi_mean_price_UF)

    print('\nPrecios por principio activo: Ahumada')
    print('Nombre:', ahu_med_max.nombre, '\nPrecio mínimo:', ahu_med_min.precio, '\nPrecio máximo:', ahu_med_max.precio,
          '\nPrecio promedio:', ahu_mean_price, '\nPrecio Promedio UF:', ahu_mean_price_UF)

    print('\nPrecios por principio activo: Farmex')
    print('Nombre:', far_med_max.nombre, '\nPrecio mínimo:', far_med_min.precio, '\nPrecio máximo:', far_med_max.precio,
          '\nPrecio promedio:', far_mean_price, '\nPrecio Promedio UF:', far_mean_price_UF)

    # Frecuencia por rango
    Estadistico.frecuenciaRangoPrecio(df_final)
