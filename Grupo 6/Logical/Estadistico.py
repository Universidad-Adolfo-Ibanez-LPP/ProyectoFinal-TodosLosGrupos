from operator import itemgetter
from functools import reduce
import statistics

def mas_caro_en_farmacia(dict):
  maxPricedItems=[]
  
  maxPricedItems.append(max((list(filter(lambda x: x["farmacia"]=="Ahumada", dict))),key=lambda x: int(x['precioCLP'])))
  maxPricedItems.append(max((list(filter(lambda x: x["farmacia"]=="Salcobrand", dict))),key=lambda x: int(x['precioCLP'])))
  maxPricedItems.append(max((list(filter(lambda x: x["farmacia"]=="RedFarma", dict))),key=lambda x: int(x['precioCLP'])))
  
  return maxPricedItems


def menor_que_mil(dic):

 return list(filter(lambda x: (int(x['precioCLP'])) < 1000, dic))


def mas_barato_por_busqueda(lista,dic,i):
  
  busquedas=list(set(list(map(itemgetter('principio_activo'),dic))))
  
  if len(busquedas)==i:
    return lista
    
  dict1=min((list(filter(lambda x: x["principio_activo"]==busquedas[i], dic))),key=lambda x: int(x['precioCLP']))
  lista.insert(i,dict1)
  
  return mas_barato_por_busqueda(lista,dic,i+1)

def promedio_remedio_farmacia(dic):
  promedio=[]
  pricelist1=list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="Ahumada", dic))))
  pricelist2=list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="Salcobrand", dic))))
  pricelist3=list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="RedFarma", dic))))
  
  promedio.append((reduce((lambda x,y: x+y), list(map(int,pricelist1))))/len(pricelist1))
  promedio.append((reduce((lambda x,y: x+y), list(map(int,pricelist2))))/len(pricelist2))
  promedio.append((reduce((lambda x,y: x+y), list(map(int,pricelist3))))/len(pricelist3))

  return promedio



def desv_estandar_remedio_farmacia(dic):
  desv_estandar=[]

  pricelist1=(list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="Ahumada", dic)))))
  pricelist2=(list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="Salcobrand", dic)))))
  pricelist3=(list(map((itemgetter('precioCLP')),list(filter(lambda x: x["farmacia"]=="RedFarma", dic)))))

  
  
  desv_estandar.append(statistics.pstdev(map(int,pricelist1)))
  desv_estandar.append(statistics.pstdev(map(int,pricelist2)))
  desv_estandar.append(statistics.pstdev(map(int,pricelist3)))


  return desv_estandar

def mas_caro_por_busqueda(lista,dic,i):
  
  busquedas=list(set(list(map(itemgetter('principio_activo'),dic))))
  
  if len(busquedas)==i:
    return lista
    
  dict1=max((list(filter(lambda x: x["principio_activo"]==busquedas[i], dic))),key=lambda x: int(x['precioCLP']))
  lista.insert(i,dict1)
  
  return mas_caro_por_busqueda(lista,dic,i+1)

def mayor_que_uno(dic):

 return list(filter(lambda x: (float(x['precioUF'])) > 1, dic))

