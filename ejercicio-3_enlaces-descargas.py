# Web Scraping con Python | Datapalooza 2025
# Taller a cargo de Riva Quiroga (https://rivaquiroga.cl)


# Ejericio 3: extraer enlaces y descargar archivos
# Vamos a descargar todas las imágenes que están disponibles en esta página: https://es.wikipedia.org/wiki/Computadora

import requests
from bs4 import BeautifulSoup
import time
import os

# Primero, probemos cómo descargar una imagen

enlace = "https://upload.wikimedia.org/wikipedia/commons/9/96/Componentes_de_un_PC.png"

nombre_archivo = os.path.basename(enlace)

ruta_destino = f"{nombre_archivo}"

respuesta = requests.get(enlace)

with open(ruta_destino, "wb") as archivo:
    archivo.write(respuesta.content)


# Ahora, buscamos todos los enlaces que nos interesan

respuesta = requests.get("https://es.wikipedia.org/wiki/Computadora")

contenido = respuesta.text

soup = BeautifulSoup(contenido, "html.parser")

imagenes = soup.find_all("figure")

# Probamos cómo llegar a la url de cada imagen:
imagenes[0].find("img").get("src")


# Ahora, usamos un loop para extraer todos los enlaces:

enlaces_imagenes = []

for imagen in imagenes:
    ruta = imagen.find("img").get("src")
    enlaces_imagenes.append(f"https:{ruta}")


# Ahora que tenemos los enlaces, podemos iterar sobre ellos usando el código que escribimos antes para descargar una imagen

for enlace in enlaces_imagenes:
    nombre_archivo = os.path.basename(enlace)
    ruta_destino = f"{nombre_archivo}"
    respuesta = requests.get(enlace)
    with open(ruta_destino, "wb") as archivo:
        archivo.write(respuesta.content)
    print(f"Imagen guardada como {nombre_archivo}")
    time.sleep(5)


# En este tipo de casos, lo ideal es implementar try + except para asegurarnos de que si algún enlace falla no se nos rompa el código
