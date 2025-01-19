# Web Scraping con Python | Datapalooza 2025
# Taller a cargo de Riva Quiroga (https://rivaquiroga.cl)


# Ejericio 1: extraer texto

import requests
from bs4 import BeautifulSoup
import re

# Paso 0: identificar en la página la etiqueta de la sección que tiene la información que quiero: etiqueta html section y la clase section pt-14

# Paso 1: Hacer la solicitud (el request)

respuesta = requests.get("https://www.minciencia.gob.cl/noticias/plan-de-data-centers-se-abre-a-consulta-ciudadana-convocada-por-el-ministerio-de-ciencia/")

respuesta.status_code

# Paso 2: extraer el código fuente de esa respuesta

contenido = respuesta.text


# Paso 3: crear "la sopa"

soup = BeautifulSoup(contenido, "html.parser")

# Paso 4: extraer lo que queremos de la página

# probemos primero cómo funcionan find() y find_all()

soup.find("h1").get_text()

soup.find_all("p").get_text()

# Ahora, extraigamos el texto de la etiqueta que habíamos encontrado antes

noticia = soup.find("section", class_= "section pt-14").get_text()

# Eliminemos el exceso de salto de línea para que se vea mejor

noticia = re.sub("\n{2,}", "\n", noticia)

with open("noticia-data-centers.txt", "w") as archivo:
    archivo.write(noticia)

¡Listo!