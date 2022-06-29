from lxml import html
from requests import get
from UF import UF

# OBTENER HTML
def obtener_html(url):
    # Obtiene el HTML de la página
    response = get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"ERROR: ${response.status_code}")
        return None

def obtener_indicador_uf(html_str):
    #Obtiene la fecha y el valor UF al momento de ser consultada
    dom = html.fromstring(html_str)
    col1 = dom.cssselect('#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate .fin-indicators-col1')[0]
    fecha = col1.cssselect('p.basic-text')[0].text_content()
    valor = col1.cssselect('p.basic-text')[2].text_content() \
        .replace('$', '') \
        .replace('.', '') \
        .replace(',', '.')
    return {'fecha': fecha, 'valor': valor}

def guardar_archivo(fecha, valor, nombre_archivo):
    #Guarda texto en un archivo
    uf = UF(fecha, valor)
    uf.set_nombreArchivoGuardado(nombre_archivo)
    uf.guardar()

def main():
    archivo_salida = 'parámetros.csv'
    url = 'http://www.bcentral.cl/inicio'

    print(f"Consultando {url}", end='')
    html = obtener_html(url)
    print('ok')

    if html != None:
        print('Obteniendo indicador: UF', end='')
        indicador = obtener_indicador_uf(html)
        print('ok')

        print(f"Guardando resultados en '{archivo_salida}'", end='')
        guardar_archivo(indicador['fecha'], indicador['valor'], archivo_salida)
        print('ok')

if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminado por el usuario")
        exit(0)