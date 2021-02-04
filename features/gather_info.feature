Feature: Gather information from Facebook Profiles.

    Scenario: Entrar a la pagina principal de Facebook.
      Given Abrimos el navegador.
      When El usuario se conecta a la URL: "https://www.facebook.com/".
      Then Verificamos el titulo exacto: "Facebook - Entrar o registrarse".
      And Cerramos el navegador.

    Scenario: Logearse en Facebook.
      Given Entramos a la web principal de Facebook.
      When El usuario introduce su email: "example.mail@gmail.com" y contraseña: "example.pass", luego pulsa en el boton de login.
      Then Verificamos que el titulo contenga: "Facebook".
      And Verificamos que en el HTML no exista el texto "La contraseña que has introducido es incorrecta. ¿Has olvidado la contraseña?".
      And Cerramos el navegador.
    
    Scenario: El usuario decide el elegir el target mediante un numero id.
      Given Estando en el inicio de la aplicación.
      When Se pasa "132465846321".
      Then Se verifica que el valor enviado es un numero.

    Scenario: Buscar perfil en cuadro de busqueda.
      Given Entramos a la web principal de Facebook.
      When El usuario introduce su email: "example.mail@gmail.com" y contraseña: "example.pass", luego pulsa en el boton de login.
      Then Verificamos que el titulo contenga: "Facebook".
      And Verificamos que en el HTML no exista el texto "La contraseña que has introducido es incorrecta. ¿Has olvidado la contraseña?".
      And El programa hace una busqueda en Facebook de: "mario cardenas".
      And Verificamos que el titulo contenga: "mario cardenas".
      Then Cerramos el navegador.

    Scenario: Devolver resultados de busqueda.
      Given Entramos a la web principal de Facebook.
      When El usuario introduce su email: "example.mail@gmail.com" y contraseña: "example.pass", luego pulsa en el boton de login.
      Then Verificamos que el titulo contenga: "Facebook".
      And Verificamos que en el HTML no exista el texto "La contraseña que has introducido es incorrecta. ¿Has olvidado la contraseña?".
      And El programa hace una busqueda en Facebook de: "mario cardenas".
      And Verificamos que el titulo contenga: "mario cardenas".
      And Se filtran los resultados por el nombre elegido.
      And Se verifica que los resultados de nombres sean mayores a cero.
      Then Cerramos el navegador.

    Scenario: Filtrar resultados de la busqueda y devolver una lista correcta de perfiles.
      Given Entramos a la web principal de Facebook.
      When El usuario introduce su email: "example.mail@gmail.com" y contraseña: "example.pass", luego pulsa en el boton de login.
      Then Verificamos que el titulo contenga: "Facebook".
      And Verificamos que en el HTML no exista el texto "La contraseña que has introducido es incorrecta. ¿Has olvidado la contraseña?".
      And El programa hace una busqueda en Facebook de: "mario cardenas".
      And Verificamos que el titulo contenga: "mario cardenas".
      And Se filtran los resultados por el nombre elegido.
      And Se verifica que los resultados de nombres sean mayores a cero.
      And Se devuelve una lista de mas de "5" links y verificando que el primer resultado sea: "https://www.facebook.com/mariocardenasojeda".
      Then Cerramos el navegador.
