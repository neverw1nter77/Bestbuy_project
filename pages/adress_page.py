import time
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from faker import Faker


class Address_page(Base):
    # Constructor to initialize driver and Faker instance for generating random data
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()

    #  Locators for different elements on the page
    first_name = '//input[@id="firstName"]'
    last_name = '//input[@id="lastName"]'
    address = '//input[@id="street"]'
    city = '//input[@id="city"]'
    state = '//select[@id="state"]'
    zipcode = '//input[@id="zipcode"]'
    apply_button = '//button[@class="c-button c-button-secondary c-button-md new-address-form__button"]'
    update_address_button = '//button[@class="c-button c-button-outline c-button-lg "]'


    # Getters:
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.state)))

    def get_zipcode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zipcode)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_update_address_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.update_address_button)))



    # Actions:
    def input_first_name(self):
        random_first_name = self.fake.first_name()
        self.get_first_name().send_keys(random_first_name)
        print(f"First name entered: {random_first_name}")
        time.sleep(1)

    def input_last_name(self):
        random_last_name = self.fake.last_name()
        self.get_last_name().send_keys(random_last_name)
        print(f"Last name entered: {random_last_name}")
        time.sleep(1)

    def input_city(self):
        self.get_city().send_keys("Middletown")
        print("City entered: Middletown")
        time.sleep(1)

    def select_state(self):
        select_element = self.get_state()
        select = Select(select_element)
        select.select_by_visible_text("RI")
        print("State selected: RI")
        time.sleep(1)

    def input_zipcode(self):
        self.get_zipcode().send_keys("02842")
        print("Zipcode entered: 02842")
        time.sleep(1)

    def input_address(self):
        self.get_address().send_keys("A Admiralty Dr W")
        print("Address entered: A Admiralty Dr W")
        time.sleep(1)
        self.get_address().send_keys(Keys.ENTER)
        print("Enter key pressed")

    def click_apply(self):
        self.get_apply_button().click()
        print("Apply button clicked")
        time.sleep(1)

    def click_update_address_button(self):
        self.get_update_address_button().click()
        print("Apply button clicked")
        time.sleep(1)

    # Methods:
    def personal_data(self):
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_city()
        self.select_state()
        self.input_zipcode()
        self.input_address()
        self.click_apply()
        self.click_update_address_button()
