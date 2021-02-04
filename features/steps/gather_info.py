from behave import given, when, then, step
import pytest
# CAMBIAR LA RUTA A LA DE TU PROYECTO !
import sys
sys.path.insert(1, 'C:/Users/USER/Desktop/Scripts/Python/Izanami/izanami')
from class_driver import Driver
from class_urlparser import UrlParser
from class_fbdrive import FbDrive

########################################################( Testing: get_url )#######################################################

@given('Abrimos el navegador.')
def abrirNavegador(context):
    context.web = FbDrive()
    assert context.web != 0

@when('El usuario se conecta a la URL: "{url}".')
def conectarseAUrl(context, url):
    context.web.get_url(url)

@then('Verificamos el titulo exacto: "{title}".')
def verificarTituloExacto(context, title):
    assert context.web.driver.title == title

@then('Cerramos el navegador.')
def cerrarNavegador(context):
    context.web.driver.close()

########################################################( Testing: facebook_login )################################################

@given('Entramos a la web principal de Facebook.')
def entrarWebPrincipalFacebook(context):
    abrirNavegador(context)
    conectarseAUrl(context, 'https://www.facebook.com/')
    verificarTituloExacto(context, "Facebook - Entrar o registrarse")

@when('El usuario introduce su email: "{email}" y contraseña: "{password}", luego pulsa en el boton de login.')
def logearseEnFacebook(context, email, password):
    context.web.facebook_login(email, password)

@then('Verificamos que el titulo contenga: "{text}".')
def verificarTituloContiene(context, text):
    if text not in context.web.driver.title:
        pytest.fail('%r not in %r' % (text, context.web.driver.title))

@then('Verificamos que en el HTML no exista el texto "{text}".')
def verificarQueElTextoNoExista(context, text):
    result = context.web.find_text(text)
    assert result != text

########################################################( Testing: verify_id )#####################################################

@given('Estando en el inicio de la aplicación.')
def step_impl(context):
    pass

@when('Se pasa "{valor}".')
def sePasaValor(context, valor):
    context.valor = valor

@then('Se verifica que el valor enviado es un numero.')
def verificaQueElValorEsUnNumero(context):
    context.isnumber = UrlParser.verify_id(context.valor)
    assert True == context.isnumber

########################################################( Testing: facebook_search )###############################################

@then('El programa hace una busqueda en Facebook de: "{nombre}".')
def realizarBusquedaFacebook(context, nombre):
    context.nombre = nombre
    context.web.facebook_search(context.web.driver.title, context.nombre)

#######################################################( Testing: return_results )################################################

@then('Se filtran los resultados por el nombre elegido.')
def verificarResultados(context):
    context.results = context.web.return_results(context.nombre)

@then('Se verifica que los resultados de nombres sean mayores a cero.')
def verificarQueLosResultadosSeanMayoresQueCero(context):
    assert len(context.results) > 0

########################################################( Testing: filter_results )################################################

@then('Se devuelve una lista de mas de "{numero}" links y verificando que el primer resultado sea: "{url}".')
def verificarLista(context, numero, url):
    
    errors = []
    # Contemplamos multiples posibilidades para acercanos mas al resultado esperado.
    if not context.results[0] == url:     
        errors.append("El primer resultado de la lista no es el esperado.")
       
    if not len(context.results) > int(numero):
        errors.append("La cantidad de resultados no es la esperada.")

    assert not errors, "[!] Errors occured:\n{}".format("\n".join(errors))
