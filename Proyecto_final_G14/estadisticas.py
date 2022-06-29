from Archivo import *
import csv
import functools
import statistics

def calcular_precio_min_pesos_principio_activo(medicamentos, principios_activos):

    # ORDENAR MEDICAMENTOS POR PRINCIPIO ACTIVO
    listado = list(map(
        lambda pa: (
            pa, list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos))
        ),
        principios_activos
    ))

    # PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))

    # CALCULAR PRECIO MÍNIMO 
    listado = list(
        map(
            # VALOR MÍNIMO EN PESOS
            lambda e: functools.reduce(lambda a, b: a if int(float(a[2])) < int(float(b[2])) else b, e[1]),
            listado
        )
    )

    def _imprimir(fila):
        #Imprime el resultado 
        print(
            'Principio: {}; Farmacia: {}; Precio (pesos): ${}' \
                .format(
                    fila[0], fila[1], '{:,}'.format(int(fila[2])).replace(',', '.'), fila[4][:20]
                )
        )

    print('Estadística 1: precio mínimo (en pesos) por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_precio_max_pesos_principio_activo(medicamentos, principios_activos):

    # ORDENAR MEDICAMENTOS POR PRINCIPIO ACTIVO
    listado = list(map(
        lambda pa: (
            pa, list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos))
        ),
        principios_activos
    ))

    # PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))

    listado = list(
        map(
            # VALOR MÁXIMO BASADO EN PESOS
            lambda e: functools.reduce(lambda a, b: a if int(float(a[2])) > int(float(b[2])) else b, e[1]),
            listado
        )
    )

    def _imprimir(fila):
        # Imprime el resultado 
        print(
            'Principio: {}; Farmacia: {}; Precio (pesos): ${}' \
                .format(
                    fila[0], fila[1], '{:,}'.format(float(fila[2])).replace(',', '.'), fila[4][:20]
                )
        )

    print('\nEstadística 4: precio máximo (en pesos) por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_precio_min_uf_principio_activo(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (
            pa, list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos))
        ),
        principios_activos
    ))

    # PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))

    listado = list(
        map(
            # VALOR MÍNIMO BASADO EN UF
            lambda e: functools.reduce(lambda a, b: a if float(a[3]) < float(b[3]) else b, e[1]),
            listado
        )
    )

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        '''Imprime el resultado de la estadística'''
        print(
            'Principio: {}; Farmacia: {}; Precio (pesos): {}UF' \
                .format(
                    fila[0], fila[1], '{:,}'.format(float(fila[3])), fila[4][:20]
                )
        )

    print('\nEstadística 2: precio mínimo (en UF) por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_precio_max_uf_principio_activo(medicamentos, principios_activos):
 
    listado = list(map(
        lambda pa: (
            pa, list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos))
        ),
        principios_activos
    ))

    # FILTRO PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))
    listado = list(

        map(
            # VALOR MÁXIMO BASADO EN UF
            lambda e: functools.reduce(lambda a, b: a if float(a[3]) > float(b[3]) else b, e[1]),
            listado
        )
    )

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Farmacia: {}; Precio (pesos): {}UF' \
                .format(
                    fila[0], fila[1], '{:,}'.format(float(fila[3])), fila[4][:20]
                )
        )

    print('\nEstadística 3: precio máximo (en UF) por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_promedio_precio_pesos_principio_activo(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (pa, list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos)) ),
        principios_activos
    ))
    
    # FILTRO PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))

    listado = list(map(
        lambda tupla: (
            tupla[0],
            # PROMEDIO
            int( functools.reduce(lambda a, b: int(float(a[2])) if type(a) is list else a + int(float(b[2])), tupla[1]) / len(tupla[1]) )
        ),
        listado
    ))

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Precio Promedio (pesos): ${}' \
                .format( fila[0], '{:,}'.format(fila[1]).replace(',', '.') )
        )

    print('\nEstadística 5: precio promedio (en pesos) por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_total_resultados_principio_activo_farmacia(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (
            # PRINCIPIO ACTIVO
            pa,
            # TOTAL AHUMADA
            len(list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Ahumada', medicamentos))),
            # TOTAL SALCOBRAND
            len(list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Salcobrand', medicamentos)))
        ),
        principios_activos
    ))

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Totales: Salcobrand: {}, Ahumada: {}' \
                .format( fila[0], fila[1], fila[2])
        )

    print('\nEstadística 6: total de resultados por principio activo y farmacia\n')
    [_imprimir(e) for e in listado]

def calcular_promedio_precio_uf_farmacia(medicamentos):

    # AGRUPAR MEDICAMENTOS POR FARMACIAS
    listado = [
        # SALCOBRAND
        list(filter(lambda m: m[1] == 'Salcobrand', medicamentos)),
        # AHUMADA
        list(filter(lambda m: m[1] == 'Ahumada', medicamentos)),
    ]

    # CALCULAR PROMEDIO DE PRECIO EN UF REDONDEADO A 2 DECIMALES
    # AHUMADA
    listado[0] = round(functools.reduce(lambda a, b: float(a[3]) if type(a) is list else a + float(b[3]), listado[0]) / len(listado[0]), 2)
    # SALCOBRAND
    listado[1] = round(functools.reduce(lambda a, b: float(a[3]) if type(a) is list else a + float(b[3]), listado[1]) / len(listado[1]), 2)

    print('\nEstadística 7: promedio de precios por farmacia\n')
    print(
        'Ahumada: {}UF; Salcobrand: {}UF'.format(listado[0], listado[1])
    )

def calcular_precio_uf_max_farmacia(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (
            # PRINCIPIO ACTIVO
            pa,
            # AHUMADA
            list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Ahumada', medicamentos)),
            # SALCOBRAND
            list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Salcobrand', medicamentos))
        ),
        principios_activos
    ))

    # CALCULAR PRECIOS MÍNIMOS
    listado = list(map(
        lambda tupla: (
            tupla[0],
            # AHUMADA
            0 if len(tupla[1]) == 0 else functools.reduce(lambda a, b: a if float(a[3]) > float(b[3]) else b, tupla[1])[3],
            # SALCOBRAND
            0 if len(tupla[2]) == 0 else functools.reduce(lambda a, b: a if float(a[3]) > float(b[3]) else b, tupla[2])[3]
        ),
        listado
    ))

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Precios: Salcobrand: {}UF, Ahumada: {}UF' \
                .format( fila[0], fila[1], fila[2])
        )

    print('\nEstadística 8: precio máximo por principio activo y farmacia\n')
    [_imprimir(e) for e in listado]

def calcular_moda_principio_activo_precio_pesos(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (
            # PRINCIPIO ACTIVO
            pa,
            # PRECIOS
            list(map(
                lambda m: int(float(m[2])),
                list(filter(lambda fila, pa=pa: fila[0] == pa, medicamentos))
            ))
        ),
        principios_activos
    ))
    
    # PRINCIPIOS ACTIVOS SIN DATOS CONSULTADOS
    listado = list(filter(lambda e: len(e[1]) > 0, listado))
    
    # CALCULAR MODA
    listado = list(map(
        lambda m: (m[0], statistics.mode(m[1])),
        listado
    ))

    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Precio: ${}' \
                .format( fila[0], '{:,}'.format(fila[1]).replace(',', '.') )
        )

    print('\nEstadística 9: precio mas frecuente por principio activo\n')
    [_imprimir(e) for e in listado]

def calcular_desviacion_estandar_principio_activo_farmacia(medicamentos, principios_activos):

    listado = list(map(
        lambda pa: (
            # PRINCIPIO ACTIVO
            pa,
            # AHUMADA
            list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Ahumada', medicamentos)),
            # SALCOBRAND
            list(filter(lambda fila, pa=pa: fila[0] == pa and fila[1] == 'Salcobrand', medicamentos))
        ),
        principios_activos
    ))

    # CALCULAR DESVIACIÓN ESTÁNDAR
    listado = list(map(
        lambda tupla: (
            # PRINCIPIO ACTIVO
            tupla[0],
            # AHUMADA
            round( statistics.pstdev( list(map(lambda e: int(float(e[2])), tupla[1])) ), 2 ) if len(tupla[1]) > 0 else 0,
            # SALCOBRAND
            round( statistics.pstdev( list(map(lambda e: int(float(e[2])), tupla[2])) ), 2 ) if len(tupla[2]) > 0 else 0
        ),
        listado
    ))
    # IMPRIMIR RESULTADOS
    def _imprimir(fila):
        print(
            'Principio: {}; Ahumada: ${}; Salcobrand: ${}' \
                .format(
                    fila[0],
                    '{:,}'.format(fila[1]).replace(',', '.'),
                    '{:,}'.format(fila[2]).replace(',', '.'),
                )
        )

    print('\nEstadística 10: desviación estándar para los precios en pesos por principio activo y farmacia\n')
    [_imprimir(e) for e in listado]

def main():
    archivo_medicamentos = 'medicamentos.csv'
    principios_activos = 'principios_activos.txt'
    # LEO ARCHIVO MEDICAMENTOS
    with open(archivo_medicamentos, 'r') as archivo:
        medicamentos = list(csv.reader(archivo, delimiter=',', quotechar='"'))

        # LEE PRINCIPIOS ACTIVOS
        pa_archivo = Archivo()
        pa_archivo.set_nombre(principios_activos)
        principios_activos = pa_archivo.leer('l')

        # ESTADISTICA 1/10:
        calcular_precio_min_pesos_principio_activo(medicamentos, principios_activos)

        # ESTADISTICA 2/10:
        calcular_precio_min_uf_principio_activo(medicamentos, principios_activos)

        # ESTADISTICA 3/10:
        calcular_precio_max_uf_principio_activo(medicamentos, principios_activos)

        # ESTADISTICA 4/10:
        calcular_precio_max_pesos_principio_activo(medicamentos, principios_activos)

        # ESTADISTICA 5/10:
        calcular_promedio_precio_pesos_principio_activo(medicamentos, principios_activos)

        # ESTADISTICA 6/10:
        calcular_total_resultados_principio_activo_farmacia(medicamentos, principios_activos)

        # ESTADISTICA 7/10:
        calcular_promedio_precio_uf_farmacia(medicamentos)
        
        # ESTADISTICA 8/10:
        calcular_precio_uf_max_farmacia(medicamentos, principios_activos)
        
        # ESTADISTICA 9/10:
        calcular_moda_principio_activo_precio_pesos(medicamentos, principios_activos)
        
        # ESTADISTICA 10/10:
        calcular_desviacion_estandar_principio_activo_farmacia(medicamentos, principios_activos)
    
if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminado por el usuario...")
        exit(0)