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

Durante el taller usaremos Firefox como navegador, pero mostraremos una extensión de [Chrome](https://chromewebstore.google.com/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=es) que puede ser de utilidad para realizar tareas de web scraping. 

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

:link: [Sitio web estático (tablas)](https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos)

:link: [Sitio web dinámico (tablas)](https://www.camara.cl/transparencia/asesoriasexternasgral.aspx)

:link: [Sitio web estático (paginación)](https://www.latercera.com/etiqueta/tecnologia/)

:link: [Sitio web dinámico (paginación)](https://www.emol.com/)

:link: [Condiciones de uso](https://www.amazon.com/-/es/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou) 

:link: [Licenciamiento y uso del contenido 1](https://www.biobiochile.cl/)

:link: [Licenciamiento y uso del contenido 2](https://prensa.presidencia.cl/)

:link: [robots.txt 1](https://wikipedia.org/)

:link: [robots.txt 2](https://www.oas.org/)


## Actividades

Durante el taller realizaremos algunos ejercicios para poner en práctica lo aprendido. Iremos escribiendo el código "en vivo" en la clase. Por el momento hay un enlace a Dropbox para cada archivo, para poder ir viendo el contenido a medida que vayamos escribiendo en él. Cuando el taller termine, subiremos la última versión de cada archivo a este repositorio.

### Ejercicio 1: extraer texto

:link: [Página web](https://www.minciencia.gob.cl/noticias/plan-de-data-centers-se-abre-a-consulta-ciudadana-convocada-por-el-ministerio-de-ciencia/)

:page_facing_up: [Código](https://www.dropbox.com/scl/fi/e57pl6875zrge4nbu7kgr/ejercicio-1_texto.py?rlkey=fsaps10ifemyqb5l9hohgwo1y&dl=0)


### Ejercicio 2: extraer tablas

:link: [Página web ejemplo 1](https://www.worldometers.info/world-population/population-by-country/) / [Página web ejemplo 2](https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos)

:page_facing_up: [Código](https://www.dropbox.com/scl/fi/o5wynj0vlukg5cuizyit4/ejercicio-2_tablas.py?rlkey=zei32tuyb0rr0e4g38s4vavu4&dl=0)

### Ejercicio 3: extraer enlaces y descargar archivos

:link: [Página web](https://es.wikipedia.org/wiki/Computadora)

:page_facing_up: [Código](https://www.dropbox.com/scl/fi/lnt1kc6ewzy4imzmj6xcn/ejercicio-3_enlaces-descargas.py?rlkey=imamegzdxn5egt3qqx0g5xv70&dl=0)


### Ejercicio 4: demo selenium

Al final del taller haremos una demostración de cómo extraer datos de sitios web dinámicos para que se hagan una idea de las diferencias en el flujo de trabajo respecto del _scraping_ de sitios estáticos. En esa parte no escribiremos el código en vivo, sino que probaremos código escrito con anticipación. 

:link: [Página web ejemplo 1](https://www.camara.cl/transparencia/oficinasparlamentarias.aspx) / [Página web ejemplo 2](https://www.memoriachilena.gob.cl)

:page_facing_up: [Código](https://www.dropbox.com/scl/fi/rdy354v5yhf4f7ct0erv5/ejercicio-4_demo-selenium.py?rlkey=te9248xheq6hu95tu4e0cgekf&dl=0)








