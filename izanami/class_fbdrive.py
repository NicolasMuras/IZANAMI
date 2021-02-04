from class_driver import Driver
from class_urlparser import UrlParser
from selenium import webdriver
from selenium.webdriver.opera.options import Options
import os
from time import sleep

########################################################( FB DRIVER )########################################################

class FbDrive(Driver):

    def __init__(self):
        options = Options()
        options.add_argument("--log-level=3")  
        self.driver = webdriver.Opera(options=options, executable_path=(str(os.getcwd())+"\\Izanami\\operadriver.exe"))

        self.objeto = Driver.__init__(self, self.driver)

    def facebook_login(self, usr, pwd):
        
        try:
            print('[*] Trying connection... (METHOD = ID)')
            self.driver.find_element_by_id('email').send_keys(usr)
            sleep(0.4)
            self.driver.find_element_by_id('pass').send_keys(pwd)
            sleep(0.6)
            self.driver.find_element_by_name('login').click()
        except Exception:
            print('[!] Cannot connect to the main page, try again.')
        
        Driver.wait_request(self, self.driver.title)
    
    def facebook_search(self, original, target):

        try:
            url = UrlParser.parse_search(target)
            self.driver.get(url)
            target = target + " - Resultados de búsqueda | Facebook"
            Driver.wait_request(self, original, target)

        except Exception:
            print('[!] Cannot search, try again.')

##############################################################################################################################
