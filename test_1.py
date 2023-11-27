from seleniumbase import BaseCase
import time
import pytest
from helper import products, CATEGORY_BUTTON, APPLY_BUTTON, SAVE_BUTTON, FORMAT_CATEGORY, FORMAT_CLASS
import configparser
import json

BaseCase.main(__name__, __file__)

config = configparser.ConfigParser()

config.read('config.ini')

panda_email = config.get('Panda_Cred', 'email')
panda_pass = config.get('Panda_Cred', 'password')

class MyTestClass(BaseCase):
    @pytest.mark.run(order=1)
    def test_demo_site(self):
        self.open("https://foodpanda.portal.restaurant/login")
        self.maximize_window()
        print('open panda portal')
        self.type("//input[@id='login-email-field']", panda_email)
        self.type("//input[@id='login-password-field']", panda_pass)
        self.click("//button[@id='button_login']")
        print('login complete')
        time.sleep(10)
        self.open('https://foodpanda.portal.restaurant/store-management/product-search?vendor=FP_PK;efp3')
        time.sleep(5)
        failedProducts = []
        for product in products:
            self.type("//input[contains(@placeholder,'Search for Products')]", product['barcodes'])
            try:
                self.wait_for_element(".MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-undefined.MuiGrid-grid-xs-12.ehh1dcx1.css-1vm7xg0", timeout=100)
                self.type("input[placeholder='SKU:']", product['sku'])
                self.type("input[placeholder='Max Qty']", product['max_sale_qty'])
                self.type("input[placeholder='Price']", product['price'])
                print(product['title'], 'belong to category ', product['category'])
                # click category
                self.click(CATEGORY_BUTTON)
                time.sleep(3)
                # click bevarages
                self.click(FORMAT_CATEGORY.format(product['category']))
                # select class soft drink
                self.click(FORMAT_CLASS.format(product['class']))
                # click apply
                self.click(APPLY_BUTTON)
                # click save
                time.sleep(3)
                self.click(SAVE_BUTTON)
            except Exception as E:
                print("Failed while uploading {0}".format(product['title']))
                failedProducts.append(product)
        with open('products_failed_to_upload.json','w') as json_file:
            json.dump(failedProducts, json_file, indent=4)
        self.click("//p[@class='MuiTypography-root MuiTypography-body1 css-1r42u07']")
        time.sleep(10)
        self.click("//button[normalize-space()='Add to My Products']")
        time.sleep(1)
        self.click("//button[normalize-space()='Add']")
        time.sleep(20)
        self.open('https://foodpanda.portal.restaurant/store-management')
        time.sleep(5)
        self.scroll_to_bottom()
        time.sleep(30)
