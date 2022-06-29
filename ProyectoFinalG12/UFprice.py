import requests
from datetime import datetime
from bs4 import BeautifulSoup
import csv

condicional = True


def getUFprice(): #scraper UF
    global condicional
    URL = "https://www.bcentral.cl/inicio"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    valorUf = soup.find_all("p", class_="basic-text fs-2 f-opensans-bold text-center c-blue-nb-2")

    now = datetime.now()
    mesesES = (
    "Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
    "Diciembre")

    fechaActual = (str(now.day) + " de " + str(mesesES[int(now.month) - 1]) + " de " + str(
        now.year))  # Fecha a usar en csv

    valorUfActual = valorUf[0].text.replace("$", "").replace(".", "").replace(",", ".")
    # valor uf a usar en csv

    if (condicional == True):
        with open('parametros.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow([fechaActual, valorUfActual])
            condicional = False

    return float(valorUfActual)