# Datapalooza 2025: Web scraping con Python
Este es el repositorio se encuentran los materiales del taller "Web scraping con Python" realizado en el marco del evento [**Datapalooza 2025**](https://www.datapalooza.cl/), organizado por la [Facultad de Matemáticas UC](https://www.mat.uc.cl/). En este taller aprenderemos a implementar la técnica de extracción de datos conocida como _web scraping_ sobre sitios web estáticos usando la librería Beautiful Soup. Hacia el final del taller haremos un demo sobre cómo trabajar con sitios web dinámicos usando Selenium.

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

Durante el taller usaremos Firefox como navegador, pero mostraremos una extensión de Google Chrome que puede ser de utilidad para realizar tareas de web scraping. 

## Atajos de teclado útiles

Los siguientes atajos de teclado serán útiles al explorar las páginas web que _escrapearemos_.

| Acción | Windows / Linux | Mac |
|---|---|---|
| Ver el código fuente de una página | ctrl +  u | command + u|
| Abrir el panel de desarrollo | F12<br/>ctrl + shift + i | F12<br/>option + command +i |
| Abrir el panel de desarrollo con la opción de selección activada | ctrl + shift + c | option/ctrl + command + c |

Existe una extensión de Google Chrome que se llama [SelectorGadget](https://chromewebstore.google.com/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=es) que puede resultar de utilidad. 

## Sitios web de ejemplo

A lo largo de la sesión revisaremos algunos sitios web a modo de ejemplo o para discutir algunas ideas. Dejaremos acá los enlaces para que sea más fácil revisarlos. 

:link: [Sitio web estático](https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos)

:link: [Sitio web dinámico](https://www.camara.cl/transparencia/asesoriasexternasgral.aspx)

:link: [Condiciones de uso](https://www.amazon.com/-/es/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou) 

:link: [Licenciamiento y uso del contenido 1](https://www.biobiochile.cl/)

:link: [Licenciamiento y uso del contenido 2](https://prensa.presidencia.cl/)

:link: [robots.txt 1](https://wikipedia.org/)

:link: [robots.txt 2](https://www.oas.org/)









