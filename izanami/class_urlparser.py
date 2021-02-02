import re

########################################################( URL PARSER )########################################################

class UrlParser():
    
    @classmethod
    def verify_id(self, id):
        regx_verify = r"(^[0-9]{4,20})"
        matcher = re.search(regx_verify, id)
        if matcher != None:
            print(matcher.group())
            return True
        else:
            print('======= IS A NAME ! =======')
            return False

    @classmethod
    def parse_search(self, target):
        self.target = target.replace(' ', '%20')
        return "https://www.facebook.com/search/top/?q=" + self.target

##############################################################################################################################