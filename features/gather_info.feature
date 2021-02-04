Feature: Gather information from Facebook Profiles.

  Scenario: Entrar a la pagina principal de Facebook.
    Given Estando en el navegador.
    When El usuario introduce el URL: "https://www.facebook.com/".
    Then El titulo de la pagina es "Facebook - Entrar o registrarse".

    Scenario: Logearse en Facebook.
      Given En la pagina principal de Facebook.
      When El usuario introduce su email: "example@gmail.com" y contraseña: "example", luego pulsa en el boton de login.
      Then El titulo de la pagina incluye "Facebook".
    
    Scenario: El usuario decide el elegir el target mediante un numero id.
      Given Estando en el inicio de la aplicación.
      When Se pasa "132465846321".
      Then Se verifica que el valor enviado es un numero.

    Scenario: Buscar perfil en cuadro de busqueda.
      Given Estando en home.
      When El programa hace una busqueda de la persona: "mario cardenas".
      Then Se verifica que el titulo incluya el nombre pasado.

    Scenario: Devolver resultados de busqueda.
      Given En la pagina de busqueda habiendo buscado por el nombre: "mario cardenas".
      When Se filtran los resultados por el nombre elegido.
      Then Se verifica que la lista de nombres sea mayor a cero.

    Scenario: Filtrar resultados de la busqueda y devolver una lista correcta de perfiles.
      Given En la pagina de busqueda luego de buscar por el nombre: "mario cardenas".
      When Teniendo los resultados de la busqueda.
      Then Se devuelve una lista de mas de "5" links y verificando que el primer resultado sea: "https://www.facebook.com/mariocardenasojeda".
