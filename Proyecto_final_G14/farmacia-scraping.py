import json
from Archivo import *
from lxml import html, etree
from requests import get
from Resultado import Resultado
#from selenium.common.exceptions import *
from sys import argv
from urllib.parse import quote
from UF import UF

def obtener_html(url):
    # Obtiene el HTML de la página a la que se quiere hacer scraping
    response = get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"ERROR: ${response.status_code}")
        return None

def salcobrand_obtener_session(partner_id):
    #Obtiene un id de tipo string necesario para realizar búsquedas en el sitio de salcobrand
    url = f"https://tracking.retailrocket.net/1.0/event/initialize/{partner_id}"
    response = get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"ERROR: ${response.status_code}")
        return None

def salcobrand_obtener_partner_id(html):
    #Obtiene el partner id de salcobrand end retailrocket.net
    partner_id = html.split('rrPartnerId = "')[1].split('";')[0]
    return partner_id

def salcobrand_limpiar_descripcion(html_str):
    #Extrae el texto del html de la descripción
    if len(html_str) <= 10:
        return ''
    else:
        lineas = html.fromstring(html_str).text_content().split("\n")
        lineas = [linea.strip().replace(":&nbsp", '') for linea in lineas]
        return ' '.join(lineas)

def salcobrand_consultar_principio(principio, nombre_archivo_resultados, valor_uf):
    #Realiza el proceso de scraping para salcobrand
    print(f"Salcobrand: Iniciando búsqueda de principio activo {principio}")
    url = f"https://salcobrand.cl/search_result?query={quote(principio)}"
    response = get(url)
    if response.status_code == 200:
        partnert_id = salcobrand_obtener_partner_id(response.text)
        session_salcobrand = salcobrand_obtener_session(partnert_id)
        api_url = f"https://api.retailrocket.net/api/2.0/recommendation/Search/602bba6097a5281b4cc438c9/?&phrase={quote(principio)}&session={session_salcobrand['sessionId']}&pvid=137&isDebug=false&format=json"

        print('Salcobrand: Realizando búsqueda')
        response2 = get(api_url)
        if response2.status_code == 200:
            medicamentos = json.loads(response2.text)

            print(f"Procesando resultados:")
            for i in range(0, len(medicamentos)):
                medicamento = medicamentos[i]
                print(f"- {medicamento['Name']} ", end='')
                
                descripcion = salcobrand_limpiar_descripcion(medicamento['Description'])
                descripcion = medicamento['Name'] + ' ' + descripcion
                precio_uf = round( float(medicamento['Price']) / valor_uf, 2)
                resultado = Resultado()
                resultado.set_nombreArchivoGuardado(nombre_archivo_resultados)
                resultado.set_descripcion(descripcion)
                resultado.set_farmacia('Salcobrand')
                resultado.set_principioActivo(principio)
                resultado.set_precioFinal(medicamento['Price'])
                resultado.set_precioUF(precio_uf)
                resultado.guardar()
                
                print('ok')
        else:
            print(f" Error al consultar medicamentos: {response2.status_code}")
            return None
    else:
        print(f"ERROR: ${response.status_code}")
        return None

def ahumada_obtener_paginacion(dom):
    #Obtiene los datos de paginación
    for script in dom.cssselect('script'):
        script_html = etree.tostring(script).decode('utf-8')
        if 'product_list.page_count' in script_html:
            # LIMPIEZA DE DATA
            data = script_html.strip() \
                .replace("    ", '') \
                .replace("&lt;!--\ntry {\n", '') \
                .replace("smileTracker.addPageVar('product_list.", '') \
                .replace("', '", ',') \
                .replace("')", '') \
                .replace("} catch (err) {\n;\n}\n//--&gt;\n", '') \
                .split("\n")[1:4]
            #  CONVERTIR A UN DICCIONARIO
            data_dict = {}
            for dato in data:
                clave, valor = dato.split(',')
                data_dict[clave] = int(valor)
            
            # DEVOLVER LA DATA COMO UN DICCIONARIO
            return data_dict
    return None

def ahumada_obtener_descripcion(url):
    #Obtiene la descripción de un medicamento
    response = get(url)
    if response.status_code == 200:
        dom = html.fromstring(response.text)
        try:
            # OBTENER INFORMACION
            informacion = dom.cssselect('div.product.attribute.description > div.value')[0].text_content() \
                .strip() \
                .replace("\n", ' ')

        except IndexError:
            informacion = ''

        # OBTENER FICHA TÉCNICA
        ficha_filas = dom.cssselect('table#product-attribute-specs-table tbody tr')
        ficha = ''
        # ACCESANDO A CELDAS DE LA TABLA
        for fila in ficha_filas:
            th = fila.cssselect('th')[0].text_content().strip()
            td = fila.cssselect('td')[0].text_content().strip()
            ficha = f"{ficha}; {th}: {td}"

        # DEVOLVER LA DESCRIPCIÓN
        return f"{informacion}; {ficha}"
    else:
        print(f"ERROR: ${response.status_code}")
        return ''

def ahumada_procesar_productos(dom, principio, nombre_archivo_resultados, valor_uf):
    #Procesa los productos de una página
    productos = dom.cssselect('ol.products > li')
    for producto in productos:
        # NOMBRE DEL PRODUCTO
        titulo = producto.cssselect('a.product-item-link')[0].text_content().strip()
        print(f"- {titulo}...", end='')
        # URL PARA CONSULTAR DETALLES
        url = producto.cssselect('a.product')[0].get('href')
        # PRECIO EN PESOS SIN DECIMALES
        precio = producto.cssselect('span.price')[0].text_content() \
            .replace('$', '') \
            .replace('.', '')
        precio = int(precio)
        # CALCULAR EL VALOR UF CON 2 DECIMALES
        precio_uf = round(float(precio) / valor_uf, 2)
        # OBTENER DESCRIPCIÓN
        descripcion = ahumada_obtener_descripcion(url)
        descripcion = f"{titulo}; {descripcion}"

        # GUARDARDO
        resultado = Resultado()
        resultado.set_nombreArchivoGuardado(nombre_archivo_resultados)
        resultado.set_descripcion(titulo + '' + descripcion)
        resultado.set_farmacia('Ahumada')
        resultado.set_principioActivo(principio)
        resultado.set_precioFinal(precio)
        resultado.set_precioUF(precio_uf)
        resultado.guardar()

        print('ok')

def ahumada_consultar_principio(principio, nombre_archivo_resultados, valor_uf):
    #Busca los principios activos en la farmacia ahumada
    print(f"Ahumada: iniciando búsqueda de principio activo {principio}")
    pagina = 1
    url = "https://www.farmaciasahumada.cl/catalogsearch/result/?p={}&q=${}"

    #CONVERTIR CARÁCTERES COMO TILDES Y ESPACIOS AL FORMATO DE LA URL
    response = get(url.format(pagina, quote(principio)))
    if response.status_code == 200:
        dom = html.fromstring(response.text)
        # EXTRAER LA PAGINACIÓN MANUALMENTE DESDE UNO DE LOS SCRIPTS QUE SE CARGAN EN LA PÁGINA
        print('Ahumada: obteniendo datos de paginación', end='')
        paginacion = ahumada_obtener_paginacion(dom)
        print('ok')

        print(f"Ahumada: consultando pagina {pagina}")
        print('Ahumada: cargando listado de productos:')
        ahumada_procesar_productos(dom, principio, nombre_archivo_resultados, valor_uf)
        
        # CONSULTAR RESTO DE PAGINAS
        if paginacion != None and paginacion['page_count'] > 1:
            for i in range(2, paginacion['page_count']):
                # ARMAR URL NUEVAMENTE
                response = get(url.format(i, quote(principio)))
                if response.status_code == 200:
                    dom = html.fromstring(response.text)
                    # CONSULTANDO PAGINA i
                    print(f"Ahumada: consultando pagina {i}")
                    print('Ahumada: cargando listado de productos:')
                    ahumada_procesar_productos(dom, principio, nombre_archivo_resultados, valor_uf)
                else:
                    print(f"ERROR: ${response.status_code}")
                    return None
    else:
        print(f"ERROR: ${response.status_code}")
        return None

def main():
    if len(argv) < 2:
        print('Especificar parámetros!')
        print('-a: Ejecuta python3 farmacia-scraping.py -a para hacer un scraping de farmacias ahumada')
        print('-s: Ejecuta python3 farmacia-scraping.py -s para hacer un scraping de farmacias salcobrand')
        # SE LE INDICA AL SISTEMA QUE OCURRIÓ UN ERROR
        exit(1)

    archivo_resultados = 'medicamentos.csv'
    archivo_registro_uf = 'parámetros.csv'
    principios_activos_archivo = 'principios_activos.txt'
    
    print('Leyendo registro de UF', end='')
    uf = UF()
    uf.set_nombreArchivoGuardado(archivo_registro_uf)
    uf.leer()
    valor_uf = uf.get_valor()
    print('ok')
    
    print('Leyendo principios activos', end='')
    principios_activos = Archivo()
    principios_activos.set_nombre(principios_activos_archivo)
    try:
        principios_activos_listado = principios_activos.leer('l')
    # EN CASO DE NO ENCONTRAR EL ARCHIVO DE PRINCIPIOS ACTIVOS
    except ArchivoNoEncontradoException as e:
        print(e)
        exit(1)
    print('ok')

    # REALIZAR LAS BÚSQUEDAS
    for principio in principios_activos_listado:
        # LEER PARAMETRO DESDE CONSOLA

        # S: EJECUTA SCRAPER PARA SALCOBRAND
        if '-s' == argv[1]:
            salcobrand_consultar_principio(principio, archivo_resultados, valor_uf)

        # A: EJECUTA SCRAPER PARA AHUMADA
        if '-a' == argv[1]:
            ahumada_consultar_principio(principio, archivo_resultados, valor_uf)

if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminado por el usuario")
        exit(0)
