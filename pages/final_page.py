import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Final_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    product_name = '//div[contains(@class, "location-fulfillment-item__title")]'



    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.product_name))
        )


    def final(self):
        self.get_current_url()
        product_element = self.get_product_name()
        self.assert_product(product_element, "Segway - Ninebot F2 Pro Electric Scooter w/34 miles Max Operating Range & 20 mph Max Speed - Black")
        self.assert_url("https://www.bestbuy.com/checkout/r/fulfillment")
        time.sleep(3)
        self.get_screenshot()
