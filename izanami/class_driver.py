from selenium import webdriver
from selenium.webdriver.common.keys import Keys

########################################################( WEB DRIVER )########################################################

class Driver():

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)
    
    def return_results(self, name):
        try:
            search = (name).split()[0]
            results = self.driver.find_elements_by_partial_link_text(search.capitalize())
            results = self.filter_results(results)

            return results

        except Exception:
            print('[!] Cannot return results, try again.')
    
    def filter_results(self, results):
        profile_links = []
        for result in results:
            try:
                profile_links.append(result.get_attribute('href'))
            except Exception:
                pass

        return profile_links

    def find_text(self, text):
        try:
            result = self.driver.find_element_by_xpath("//*[ text() = 'La contraseña que has introducido es incorrecta. ' ]")
            return result.text
        except Exception:
            return "[!] Elemento no localizado."  

    # Wait until the web title changes.
    def wait_request(self, original_title = 0, expected_title = 0):
        num = str(self.driver.title[1])
        title_new = ("({}) {}".format(num, expected_title))
        
        if expected_title == 0:
            while(self.driver.title == original_title):
                pass
        else:
            while(True):
                if self.driver.title == expected_title or self.driver.title == title_new:
                    break
        
##############################################################################################################################
