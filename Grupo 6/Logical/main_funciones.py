import csv
from Redactor import *
from Estadistico import *


titles = ['principio_activo','farmacia','descripcion','precioCLP','precioUF']
dic_datos=csv_to_dic(titles)


caro=mas_caro_en_farmacia(dic_datos) 
menor_a_mil=menor_que_mil(dic_datos)

mas_barato_buscados=[]
mas_barato_buscados=mas_barato_por_busqueda(mas_barato_buscados,dic_datos,0)
promedio_cada_farmacia=promedio_remedio_farmacia(dic_datos)

titlesespfarmacia=["farmacia","precio_promedio"]
promedio_cada_farmacia=attach_price_to_drugstore(promedio_cada_farmacia)

desv_estandar=desv_estandar_remedio_farmacia(dic_datos)
desv_estandar=attach_price_to_drugstore(desv_estandar)


dic_to_csv(titles,caro,"Remedio_mas_caro_por_farmacia")
dic_to_csv(titles,menor_a_mil,"Cuestan_menos_de_1000CLP")
dic_to_csv(titles,mas_barato_buscados,"Mas_barato_por_busqueda")
dic_to_csv(titlesespfarmacia,promedio_cada_farmacia,"Precio_promedio_total_farmacia")  
dic_to_csv(titlesespfarmacia,desv_estandar,"Desviacion_estandar_de_farmacias")  
print("Hecho")  
