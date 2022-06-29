import csv

def csv_to_dic(titles):
  with open('out.csv', newline='') as f:
      reader = csv.reader(f)
      data = list(reader)
  
  data.pop(0)
  dic_datos=[]
  
  for row in data:
    iterator=zip(titles, row)
    a_dictionary = dict(iterator)
    dic_datos.append(a_dictionary)
  
  return dic_datos


def dic_to_csv(titles,data,csvname):
 with open (csvname+'.csv', 'w') as csvfile:
   writer = csv.DictWriter(csvfile, fieldnames = titles)
   writer.writeheader()
   writer.writerows(data)

def attach_price_to_drugstore(list):
  farmacias=["Ahumada", "Salcobrand", "Redfarma"]
  lista=[]
  for i in range(len(farmacias)):
  
    diccionari={"farmacia": farmacias[i], "precio_promedio":list[i]}
    lista.append(diccionari)
  return lista
  