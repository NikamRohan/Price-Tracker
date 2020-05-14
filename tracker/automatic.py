from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time

class AmazonBot(object):
  
    def __init__(self):
        self.amazon_url = "https://www.amazon.in/"

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        firefox_options=self.options)



    def get_product_price_name_src(self, url):
       
        self.driver.get(url)

        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
             try:
                price=self.driver.find_element_by_id("priceblock_ourprice").text
             except:
                price=None

        if price is None:
            price = "Not available"

        else:
            non_decimal = re.compile(r'[^\d.]+')
            price = non_decimal.sub('', price)

        name=self.get_product_name(url)

        return name,price

    def get_product_name(self, url):
        try:
            product_name = self.driver.find_element_by_id("productTitle").text
        except:
            pass

        if product_name is None:
            product_name = "Not available"

            
        return product_name

    def get_price_only(self,url):
        self.driver.get(url)

        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
             try:
                price=self.driver.find_element_by_id("priceblock_ourprice").text
             except:
                price=None

        if price is None:
            price = "Not available"

        else:
            non_decimal = re.compile(r'[^\d.]+')
            price = non_decimal.sub('', price)

        
        
        return price   



