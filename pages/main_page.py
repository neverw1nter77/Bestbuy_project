import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):
    # Constructor: Initializes the driver
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators: Define the XPath for various elements on the main page

    main_button = '//button[@class="c-button-unstyled hamburger-menu-button"]'
    menu_scroll = '//ul[@class="hamburger-menu-flyout-list"]'
    electric_transportation_button = "//button[starts-with(@data-id, \"node-\") and contains(text(), \"Electric Transportation\")]"
    scooter_button = '//*[contains(text(), "Electric Scooters")]'
    scooter_adult_button = '//*[contains(text(), "Adult Electric Scooters")]'

    # Getters: Methods to retrieve the web elements based on the defined locators

    def get_main_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_button)))

    def get_menu_scroll(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_scroll)))

    def get_electric_transportation(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.electric_transportation_button)))

    def get_scooter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scooter_button)))

    def get_scooter_adult_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scooter_adult_button)))


    # Actions: Methods to interact with the elements

    def click_main_button(self):
        self.get_main_button().click()
        print("Main button clicked")
        time.sleep(1)

    def scroll_menu(self):
        self.driver.execute_script("arguments[0].scrollTop += 500;", self.get_menu_scroll())
        print("Scroll menu")
        time.sleep(1)
    def click_electric_transportation(self):
        self.get_electric_transportation().click()
        print("Button Electric Transportation clicked")
        time.sleep(1)


    def click_scooter_button(self):
        self.get_scooter_button().click()
        print("Button Electric Scooters clicked")
        time.sleep(1)

    def click_scooter_adult_button(self):
        self.get_scooter_adult_button().click()
        print("Button Adult Electric Scooters clicked")
        time.sleep(1)

    # Methods: Perform a series of actions to navigate through the menu
    def menu(self):
        self.get_current_url()
        self.click_main_button()
        self.scroll_menu()
        self.click_electric_transportation()
        self.click_scooter_button()
        self.click_scooter_adult_button()