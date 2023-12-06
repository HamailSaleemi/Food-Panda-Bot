from seleniumbase import BaseCase
import time
import pytest
from helper import products, CATEGORY_BUTTON, APPLY_BUTTON, SAVE_BUTTON, FORMAT_CATEGORY, FORMAT_CLASS
import json
from base_class import BaseFunctionalityClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestClass(BaseFunctionalityClass):


    @pytest.mark.run(order=1)
    def test_demo_site(self):
        self.login()


    @pytest.mark.run(after='test_demo_site')
    def test_create_product(self):
        self.open('https://foodpanda.portal.restaurant/store-management/')
        time.sleep(5)
        failedProducts = []
        first_run = True
        for product in products:
            self.type("//input[contains(@placeholder,'Search for Products')]", product['barcodes'])

            self.wait_for_element(".MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-undefined.e1m2815e2.css-z6ujo4", timeout=100)

            time.sleep(2)
            hidden_element_selector = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10 css-irq8bb'])[1]"
            # time.sleep(2)
            # self.execute_script("arguments[0].style.display = 'block';", self.find_element(hidden_element_selector))
            # time.sleep(2)
            self.click(hidden_element_selector)
            # time.sleep(2)
            try:
                if first_run:
                    self.click("(//*[name()='path'])[36]")
                else:
                    self.click("(//*[name()='path'])[37]")
            except Exception:
                if first_run:
                    self.click("(//*[name()='path'])[37]")
                else:
                    self.click("(//*[name()='path'])[36]")

            # time.sleep(2)
            self.type("input[placeholder='Max Qty']", product['max_sale_qty'])
            # time.sleep(2)
            self.click("//*[name()='path' and contains(@d,'M17 3H5c-1')]")
            # time.sleep(2)

            hidden_element_selector = "(//div[@class='MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-undefined MuiGrid-grid-xs-12 css-s1ez65'])[1]"
            # time.sleep(0)
            # self.execute_script("arguments[0].style.display = 'block';", self.find_element(hidden_element_selector))
            # time.sleep(0)
            self.click(hidden_element_selector)
            # time.sleep(1)
            try:
                if first_run:
                    self.click("(//*[name()='path'])[38]")
                else:
                    self.click("(//*[name()='path'])[39]")
            except Exception:
                if first_run:
                    self.click("(//*[name()='path'])[39]")
                else:
                    self.click("(//*[name()='path'])[38]")
            first_run = False
            # time.sleep(1)
            self.type("input[placeholder='Price']", product['price'])
            # time.sleep(1)
            self.click ("//*[name()='path' and contains(@d,'M17 3H5c-1')]")
            # time.sleep(0)

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
