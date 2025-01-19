# Web Scraping con Python | Datapalooza 2025
# Taller a cargo de Riva Quiroga (https://rivaquiroga.cl)


# Ejericio 4: un demo de cómo funciona selenium
# antes: pip install pyselenium


from selenium import webdriver 
from selenium.webdriver.support.select import Select # para el ejemplo 1


# EJEMPLO 1: seleccionar un menú

# Iniciamos el driver

driver = webdriver.Firefox() 
# si prefieres usar Chrome, entonces usa  driver = webdriver.Chrome() 

# Navegamos a la página que nos interesa

driver.get("https://www.camara.cl/transparencia/oficinasparlamentarias.aspx")

# Identificamos el elemento de la página con el que queremos interactua

menu_anio = driver.find_element("id", "ContentPlaceHolder1_ContentPlaceHolder1_ddlAno")

# Selenium tiene distintos métodos para interactuar desde nuestra sesión de Python con la página. Por ejemplo, podemos hacer clic:

menu_anio.click()

# En este caso nos interesa seleccionar el menú
Select(menu_anio).select_by_visible_text("2023") 

# también puedo seleccionar por value o por index
Select(menu_anio).select_by_index(0)

# Cuando la página muestra los datos que queremos, extreamos el código fuente tal como está en ese momento

codigo_fuente = driver.page_source

# Ya no necesitamos el driver, así que lo cerramos

driver.quit()

# Luego, podemos seguir trabajando tal como cuando hacemos web scraping en sitios estáticos: usando Beautiful Soup. También podemos seguir con Selenium, que tiene funciones y métodos similares para extraer los datos de los elementos de la página. 


# EJEMPLO 2: llenar un formulario de búsqueda y hacer clic en un botón

# Iniciamos el driver
driver = webdriver.Firefox()

# Navegamos a la página que nos interesa
driver.get("https://www.memoriachilena.gob.cl")

# Identificamos los elementos con los que nos interesa interactuar

barra_busqueda = driver.find_element("id", "keywords")
boton_busqueda = driver.find_element("id", "boton_busqueda")

# Realizamos acciones con ellos: enviamos datos para hacer una búsqueda y hacemos click en buscar

barra_busqueda.send_keys("tipografía en Chile")

barra_busqueda.clear() # si queremos limpiar la búsqueda
boton_busqueda.click()

# Extraemos el código fuente:

codigo_fuente = driver.page_source

# Nue no se nos olvide cerrar el navegador:

driver.quit()

# Ya tenemos el código fuente guardado en una variable.






