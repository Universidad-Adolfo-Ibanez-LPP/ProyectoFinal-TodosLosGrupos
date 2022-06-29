import pandas as pd

def read_txt(archivo): # lee txt

    with open(archivo, "r", encoding="utf8") as activos:
        lines = activos.read().split('\n')

    return lines

def Csv(Nombre): # pasa a data frame para escribir el csv

    df = pd.read_csv(Nombre, encoding = 'latin')
    df.columns=['Principio Activo', 'Farmacia', 'Descripción', 'Precio en Pesos Chilenos', 'Precio en UF']
    df= df[df['Precio en Pesos Chilenos'] != 0.0]
    df.to_csv('Medicamentos.csv', index=False)

