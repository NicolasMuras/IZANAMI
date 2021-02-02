<h1>Izanami</h1>

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/code_climate_start.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementacion del proyecto</a></li>
  <li><a href="#resultados">Resultados</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduccion al proyecto</h2>

La idea del proyecto es hacer un refactoring a un script que hice hace unos años, implementando la metodología del Test-Driven Development.
El objetivo principal de esta herramienta es conectarse a una cuenta de facebook y substraer datos de un perfil objetivo.
Para esto utilizo Selenium en conjunto con BeautifulSoup.

<h2><a id="user-content-implementación-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>Python</strong>: El lenguaje utilizado para la elaboracion del codigo.</li>
<li><strong>Selenium</strong>: Es un framework que nos permitira simular la navegación mediante un web driver.</li>
<li><strong>BeautifulSoup</strong>: Libreria utilizada para analizar documentos HTML.</li>
</ul>

<h2> DIA 1 </h2>

Empece por definir esta vez una clase y encarar por otro camino, el paradigma de la programación orientada a objetos.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/class_driver_0.bmp?raw=true)

Empece a implementar los test, siguiendo la metodología TDD, aquí algunos ejemplos:

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/ejemplos_escritos_por_mi.bmp?raw=true)

<h2> DIA 2 </h2>

Continue separando en metodos, esta vez contemple la posibilidad de crear una clase FbDriver y hacer que herede de Driver, de esta forma las responsabilidades de cada una estan bien divididas, ademas tenemos la clase UrlParser, esta se encarga de realizar algunas busquedas especificas (expresiones regulares) en cadenas de texto.

![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/herencia_python.bmp?raw=true)

Le hago refactoring a los tests para aplicar el DRY, uno para conectarnos y otro que te conecta y busca, por ahora son 6 tests a las funciones principales, todos pasaron.
El inconveniente que seguro veran, sera que el tiempo de ejecución de los tests es alto, esto es normal debido a que el programa en si utiliza Selenium, basicamente,
estoy haciendole test unitarios a un test funcional.
![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/test_refactoring_0.bmp?raw=true)
![alt text](https://github.com/NicolasMuras/script_izanami/blob/main/images/success_testing.bmp?raw=true)
#Selenium #Automation #Hacking #Scripting #bs4
