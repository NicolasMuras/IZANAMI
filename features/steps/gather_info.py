from behave import *
import pytest
import sys
sys.path.insert(1, 'C:/Users/USER/Desktop/Scripts/Python/Izanami/izanami')
from class_driver import Driver
from class_urlparser import UrlParser
from class_fbdrive import FbDrive

# Nos permite conectarnos y aplicar el DRY.
def connect():
    web = FbDrive()
    web.get_url('https://www.facebook.com/')
    web.facebook_login('example@gmail.com', 'example')
    return web

# Nos conectamos y realizamos la busqueda ejemplo.
def search(nombre):
    web = connect()
    web.facebook_search(nombre)
    results = web.return_results()
    return web, results

########################################################( Testing: get_url )#######################################################

@given('Estando en el navegador.')
def step_impl(context):
    context.web = FbDrive()
    assert context.web != 0

@when('El usuario introduce el URL: "{url}".')
def step_impl(context, url):
    context.web.get_url(url)

@then('El titulo de la pagina es "{title}".')
def step_impl(context, title):
    assert context.web.driver.title == title
    context.web.driver.close()

########################################################( Testing: facebook_login )################################################

@given("En la pagina principal de Facebook.")
def step_impl(context):
    context.web = FbDrive()
    context.web.get_url('https://www.facebook.com/')
    assert context.web.driver.title == "Facebook - Entrar o registrarse"

@when('El usuario introduce su email: "{email}" y contraseña: "{password}", luego pulsa en el boton de login.')
def step_impl(context, email, password):
    context.web.facebook_login(email, password)

@then('El titulo de la pagina incluye "{text}".')
def step_impl(context, text):
    if text not in context.web.driver.title:
        context.web.driver.close()
        pytest.fail('%r not in %r' % (text, context.web.driver.title))
    else:
        context.web.driver.close()
    
########################################################( Testing: verify_id )#####################################################

@given('Estando en el inicio de la aplicación.')
def step_impl(context):
    pass

@when('Se pasa "{valor}".')
def step_impl(context, valor):
    context.valor = valor

@then('Se verifica que el valor enviado es un numero.')
def step_impl(context):
    context.isnumber = UrlParser.verify_id(context.valor)
    assert True == context.isnumber

########################################################( Testing: facebook_search )###############################################

@given('Estando en home.')
def step_impl(context):
    context.web = connect()

@when('El programa hace una busqueda de la persona: "{nombre}".')
def step_impl(context, nombre):
    context.nombre = nombre
    context.web.facebook_search(context.nombre)

@then('Se verifica que el titulo incluya el nombre pasado.')
def step_impl(context):
    assert context.web.driver.title == "{} - Resultados de búsqueda | Facebook".format((context.nombre))
    context.web.driver.close()

#######################################################( Testing: return_results )################################################

@given('En la pagina de busqueda habiendo buscado por el nombre: "{nombre}".')
def step_impl(context, nombre):
    context.web = connect()
    context.nombre = nombre
    context.web.facebook_search(context.nombre)

@when('Se filtran los resultados por el nombre elegido.')
def step_impl(context):
    context.results = context.web.return_results(context.nombre)

@then('Se verifica que la lista de nombres sea mayor a cero.')
def step_impl(context):
    assert len(context.results) > 0
    context.web.driver.close()

########################################################( Testing: filter_results )################################################

@given('En la pagina de busqueda luego de buscar por el nombre: "{nombre}".')
def step_impl(context, nombre):
    context.web = connect()
    context.nombre = nombre
    context.web.facebook_search(context.nombre)

@when('Teniendo los resultados de la busqueda.')
def step_impl(context):
    context.results = context.web.return_results(context.nombre)

@then('Se devuelve una lista de mas de "{numero}" links y verificando que el primer resultado sea: "{url}".')
def step_impl(context, numero, url):
    errors = []
    # Contemplamos multiples posibilidades para acercanos mas al resultado esperado.
    if not context.results[0] == url:         
        errors.append("El primer resultado de la lista no es el esperado.")
    if not len(context.results) > int(numero):
        errors.append("La cantidad de resultados no es la esperada.")

    assert not errors, "[!] Errors occured:\n{}".format("\n".join(errors))
    context.web.driver.close()
