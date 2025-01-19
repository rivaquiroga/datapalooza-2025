# Web Scraping con Python | Datapalooza 2025
# Taller a cargo de Riva Quiroga (https://rivaquiroga.cl)


# Ejericio 2: extraer tablas

import pandas as pd


# Una tabla en la página:

tabla_poblacion = pd.read_html("https://www.worldometers.info/world-population/population-by-country/")

print(tabla_poblacion) 

tabla_poblacion.info() # error, porque por defecto deja las tablas que extrae en una lista. Así que hay que en este caso hay que usar index 0 para sacar el primer elemento

tabla_poblacion[0].info() # ahora sí

tabla_poblacion[0].to_csv("poblacion-mundial_2025.csv", index = False)



# Varias tablas en la página


tablas_albumes = pd.read_html("https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos")

# Listo! Tenemos una lista dentro de la cual cada elemento es un dataframe

len(tablas_albumes)

tablas_albumes[4].info()
tablas_albumes[2].head()

