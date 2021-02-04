<h1>Izanami</h1>

Antes del refactoring:

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/code_climate_start.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementación del proyecto</a></li>
  <li><a href="#resultados">Resultados</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introducción al proyecto</h2>

La idea del proyecto es hacer un refactoring a un script que hice hace unos años, implementando la metodología del Test-Driven Development.
El objetivo principal de esta herramienta es conectarse a una cuenta de facebook y substraer datos de un perfil objetivo.
Para esto utilizo Selenium en conjunto con BeautifulSoup.

<h2><a id="user-content-implementación-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>Python 3+</strong>: El lenguaje utilizado para la elaboración del código.</li>
<li><strong>Selenium</strong>: Es un framework que nos permitirá simular la navegación mediante un web driver.</li>
<li><strong>BeautifulSoup</strong>: Librería utilizada para analizar documentos HTML.</li>
<li><strong>Pytest</strong>: Librería de testing utilizada.</li>
<li><strong>Behave</strong>: Nos permite utilizar pruebas escritas en lenguaje natural.</li>
</ul>

<h2> DIA 1 </h2>

Empecé por definir esta vez una clase y encarar por otro camino, el paradigma de la programación orientada a objetos.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/class_driver_0.bmp?raw=true)

Implemente los test siguiendo la metodología TDD, aquí algunos ejemplos:

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/ejemplos_escritos_por_mi.bmp?raw=true)

<h2> DIA 2 </h2>

Continúe separando en métodos, esta vez contemple la posibilidad de crear una clase FbDriver y hacer que herede de Driver, de esta forma las responsabilidades de cada una están bien divididas, además tenemos la clase UrlParser, esta se encarga de realizar algunas búsquedas especificas (expresiones regulares) en cadenas de texto.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/herencia_python.bmp?raw=true)

Le hago refactoring a los tests para aplicar el DRY, uno para conectarnos y otro que te conecta y busca, por ahora son 6 tests a las funciones principales, todos pasaron.
El inconveniente que seguro verán es que el tiempo de ejecución de los tests es alto, esto es normal debido a que el programa en si utiliza Selenium.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/test_refactoring_0.bmp?raw=true)

<h2> DIA 3 </h2>

Hoy me levante con ganas de aplicar otra metodología, mi idea es que este proyecto sea completo y documentado, que cualquier stakeholder pueda entender y verificar como funciona el código, para esto implemente el conocido Behavior-Driver Development (BDD) con Behave, ahora usted puede comprobar con diversos parametros que el programa funciona como debe. 

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/gherkin_0.bmp?raw=true)

Mas alla de esto, hay que recalcar que este proyecto es en Selenium y aunque parezca que simplemente es un test UI, no lo es, mas adelante entrara en acción BeautifulSoup, con el que podremos hacer el conocido "web scraping" y todo cobrara mas sentido.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/behavior_testing_0.bmp?raw=true)

#Selenium #Automation #Hacking #Scripting #bs4
