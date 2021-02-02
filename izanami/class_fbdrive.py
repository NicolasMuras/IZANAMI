from class_driver import Driver
from class_urlparser import UrlParser
from selenium import webdriver
import os
from time import sleep

########################################################( FB DRIVER )########################################################

class FbDrive(Driver):

    def __init__(self):
        self.driver = webdriver.Opera(executable_path=(str(os.getcwd())+"\\Izanami\\operadriver.exe"))

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
            self.driver.close()
            print('[!] Cannot connect to the main page, try again.')
        
        Driver.wait_request(self, 'Facebook')
    
    def facebook_search(self, target):

        try:
            url = UrlParser.parse_search(target)
            self.driver.get(url)
            target = target + " - Resultados de búsqueda | Facebook"
            Driver.wait_request(self, target)

        except Exception:
            self.driver.close()
            print('[!] Cannot search, try again.')

##############################################################################################################################