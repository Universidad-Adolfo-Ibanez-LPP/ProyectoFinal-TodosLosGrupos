from webscrapers import *

if __name__ == '__main__':
    print("Bienvenido al buscador de anticonceptivos UAI")
    with open('principios_activos.txt', "r") as f:
        principios_activos = f.read().split()
    scraper1 = WebScraperAhumada(principios_activos)
    print("Farmacias Ahumada tiene los siguientes anticonceptivos que contienen los principios activos que busca, con su respectivo precio")
    scraper1.run() 
    scraper2 = WebScraperDrSimi(principios_activos)
    print("Farmacias Dr. Simi tiene los siguientes anticonceptivos que contienen los principios activos que busca, con su respectivo precio")
    scraper2.run() 