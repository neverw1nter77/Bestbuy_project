import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators for the elements on the Cart page

    remove_button = '(//button[@class="c-button-link cart-item__remove"])[1]'
    checkout_button = '//button[@class="btn btn-lg btn-block btn-primary"]'



    # Getters:

    def get_remove_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))




    # Actions:

    def click_remove_button(self):
        self.get_remove_button().click()
        print("Remove button clicked")
        time.sleep(2)

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Checkout_button clicked")
        time.sleep(2)


    # Methods
    def cart(self):
        self.get_current_url()
        self.click_remove_button()
        self.click_checkout_button()

