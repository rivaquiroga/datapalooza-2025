# Datapalooza 2025: Web scraping con Python
Este es el repositorio del taller sobre "Web scraping con Python" para el evento [**Datapalooza 2025**](https://www.datapalooza.cl/), organizado por la [Facultad de Matemáticas UC](https://www.mat.uc.cl/). En este taller aprenderemos a implementar la técnica de extracción de datos conocida como web scraping sobre sitios web estáticos usando la librería Beautiful Soup. Hacia el final del taller haremos un demo sobre cómo trabajar con sitios web dinámicos usando Selenium.


## Preparación 

Para realizar las actividades planificadas necesitarás las librerías `request`, `beautifulsoup4`, `lxml` y `pandas`. Se pueden instalar desde [PyPI](https://pypi.org/) con `pip`. 

```
pip install beautifulsoup4
pip install requests
pip install pandas
pip install lxml
```

Si prefieres trabajar en Google Colab, no olvides agregar un signo de exclamación al inicio de cada línea para su instalación, es decir:

```
!pip install beautifulsoup4
!pip install requests
!pip install pandas
!pip install lxml
```
(Esto le indica a Google Colab que ese no es código de Python, sino código que tiene que ejecutarse en la Terminal.)

Durante el taller usaremos Firefox como navegador, pero mostraremos una extensión de Google Chrome que puede ser de utilidad al realizar tareas de web scraping. 

