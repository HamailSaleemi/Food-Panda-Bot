from seleniumbase import BaseCase
import time
import configparser

BaseCase.main(__name__, __file__)

config = configparser.ConfigParser()

config.read('config.ini')

panda_email = config.get('Panda_Cred', 'email')
panda_pass = config.get('Panda_Cred', 'password')

class BaseFunctionalityClass(BaseCase):

    def login(self):
        self.open("https://foodpanda.portal.restaurant/login")
        self.maximize_window()
        print('open panda portal')
        self.type("//input[@id='login-email-field']", panda_email)
        self.type("//input[@id='login-password-field']", panda_pass)
        self.click("//button[@id='button_login']")
        print('login complete')
        time.sleep(10)
