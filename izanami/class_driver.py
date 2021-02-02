from selenium import webdriver
from selenium.webdriver.common.keys import Keys

########################################################( WEB DRIVER )########################################################

class Driver():

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)
    
    def return_results(self):
        
        try:
            results = self.driver.find_elements_by_partial_link_text('Mario')
            results = self.filter_results(results)
            return results

        except Exception:
            self.driver.close()
            print('[!] Cannot return results, try again.')
    
    def filter_results(self, results):
        profile_links = []
        for result in results:
            try:
                profile_links.append(result.get_attribute('href'))
            except Exception:
                pass

        return profile_links


    # Wait until the web title changes.
    def wait_request(self, expected):
        while(self.driver.title != expected):
            pass
    
##############################################################################################################################

