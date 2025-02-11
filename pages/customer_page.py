import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Customer_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    guest_button = '//button[@class="c-button c-button-secondary c-button-lg cia-guest-content__continue guest"]'


    # Getters

    def get_guest_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.guest_button)))



    # Actions

    def click_guest_button(self):
        self.get_guest_button().click()
        print("Guest_button clicked")
        time.sleep(1)


    # Methods
    def guest(self):
        self.get_current_url()
        self.click_guest_button()