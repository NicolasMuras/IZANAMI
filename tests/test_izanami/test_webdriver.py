import pytest
from time import sleep
########################################################( IMPORT FILES )###########################################################

import sys
sys.path.insert(1, 'C:/Users/USER/Desktop/Scripts/Python/Izanami/izanami')
from class_driver import Driver
from class_urlparser import UrlParser
from class_fbdrive import FbDrive

# Nos permite conectarnos y evitar el DRY.
def connect():
    web = FbDrive()
    web.get_url('https://www.facebook.com/')
    web.facebook_login('examplemail@gmail.com', 'example_pass')
    return web

# Nos conectamos y realizamos la busqueda ejemplo.
def search():
    web = connect()
    web.facebook_search('mario cardenas')
    results = web.return_results()
    return web, results

########################################################( Testing: get_url )#######################################################
# Scenario: Entrar a la pagina principal de Facebook.
# Given: Estando en el navegador.
# When: El usuario introduce el URL: 'https://www.facebook.com/'.
# Then: El titulo de la pagina es "Facebook - Entrar o registrarse".

def test_get_url():

    web = FbDrive()
    web.get_url('https://www.facebook.com/')
    assert web.driver.title == "Facebook - Entrar o registrarse"
    web.driver.close()

########################################################( Testing: facebook_login )################################################
# Scenario: Logearse en Facebook.
# Given: En la pagina principal de Facebook.
# When: El usuario introduce su email y contraseña, luego pulsa en el boton de login.
# Then: El titulo de la pagina es "Facebook".

def test_facebook_login():

    web = connect()
    assert web.driver.title == "Facebook"
    web.driver.close()

########################################################( Testing: verify_id )#####################################################
# Scenario: Verificar que el valor enviado sea un numero.
# Given: Habiendo logeado y estando en home.
# When: Despues de logearse exitosamente.
# Then: Se verifica que el valor 'id' == 'True'.

def test_verify_id():

    isnumber = UrlParser.verify_id('1231483215642')
    assert True == isnumber

########################################################( Testing: facebook_search )###############################################
# Scenario: Buscar perfil en cuadro de busqueda.
# Given: Estando en home. Si la verificación de 'id' nos arroja un resultado falso.
# When: El usuario hace clic en el cuadro de busqueda y coloca el nombre del objetivo.
# Then: Se verifica que el valor 'id' == 'True'.

def test_facebook_search():
    # solo debe ejecutar la busqueda no debe seleccionar un resultado en la busqueda

    web, results = search()
    assert web.driver.title == "mario cardenas - Resultados de búsqueda | Facebook"
    web.driver.close()

#######################################################( Testing: return_results )################################################
# Scenario: Devolver resultados de busqueda.
# Given: Luego de realizada la busqueda.
# When: El usuario hace clic en el perfil que prefiera.
# Then: Se redirige al perfil del usuario elegido.

def test_return_results():
    web, results = search()
    assert len(results) > 0
    web.driver.close()
########################################################( Testing: filter_results )################################################
# Scenario: Filtrar resultados de la busqueda y devolver una lista correcta de perfiles.
# Given: Estando en el url de busqueda.
# When:  Una vez devueltos los resultados.
# Then: Filtrar y devolver una lista de links de perfiles.

def test_filter_results():
    web, results = search()
    errors = []

    # Contemplamos multiples posibilidades para acercanos mas al resultado esperado.
    if not results[0] == 'https://www.facebook.com/mariocardenasojeda':         
        errors.append("El primer resultado de la lista no es el esperado.")
    if not len(results) > 5:
        errors.append("La cantidad de resultados no es la esperada.")

    assert not errors, "[!] Errors occured:\n{}".format("\n".join(errors))

    web.driver.close()
