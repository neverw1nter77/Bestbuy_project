import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators:

    filters_scroll = '//div[@class="sticky-container lv"]'
    features_input_1 = '//input[@id="features_facet-Foldable-Design-0"]'
    features_input_2 = '//input[@id="features_facet-App-Compatible-1"]'
    price_range_1 = '//input[@placeholder="min."]'
    price_range_2 = '//input[@placeholder="max."]'
    button_enter_price = '//button[@class="c-button-link range-submit"]'
    max_speed_button = '//input[@id="maxspeedrange_facet-15-20-MPH-0"]'
    brand = '//input[@id="brand_facet-Segway-0"]'
    add_to_cart_button = '(//button[contains(@class, "add-to-cart-button") and contains(@data-button-state, "ADD_TO_CART")])[1]'
    helmet_button = '//button[@data-sku-id="6559372"]'
    go_to_cart_button = '//a[@class="c-button c-button-secondary c-button-md c-button-block "]'





    # Getters:

    def get_filters_scroll(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters_scroll)))

    def get_features_input_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.features_input_1)))

    def get_features_input_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.features_input_2)))

    def get_input_price_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_1)))

    def get_input_price_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_2)))

    def get_button_enter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter_price)))

    def get_max_speed_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_speed_button)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))


    def get_scooter_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_helmet_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.helmet_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))



    # Actions:

    def scroll_menu_1(self):
        self.driver.execute_script("arguments[0].scrollTop += 1000;", self.get_filters_scroll())
        print("Scroll filters")
        time.sleep(1)

    def click_features_input_1(self):
        self.get_features_input_1().click()
        print("Feature Foldable design clicked")
        time.sleep(2)

    def scroll_menu_2(self):
        self.driver.execute_script("arguments[0].scrollTop += 0;", self.get_filters_scroll())
        print("Scroll filters")
        time.sleep(1)

    def click_features_input_2(self):
        self.get_features_input_2().click()
        print("Feature App Compatible  clicked")
        time.sleep(1)

    def scroll_menu_3(self):
        self.driver.execute_script("arguments[0].scrollTop += 600;", self.get_filters_scroll())
        print("Scroll filters")
        time.sleep(1)

    def input_price_1(self, price):
        input_field = self.get_input_price_1()
        input_field.clear()
        input_field.send_keys(price)
        print(f"The minimum price has been entered: {price}")
        time.sleep(1)

    def input_price_2(self, price):
        input_field = self.get_input_price_2()
        input_field.clear()
        input_field.send_keys(price)
        print(f"The maximum price has been entered: {price}")
        time.sleep(1)

    def click_button_enter_price(self):
        self.get_button_enter_price().click()
        print("Button apply price clicked")
        time.sleep(2)

    def scroll_menu_4(self):
        self.driver.execute_script("arguments[0].scrollTop += 500;", self.get_filters_scroll())
        print("Scroll filters")
        time.sleep(1)

    def click_max_speed_button(self):
        self.get_max_speed_button().click()
        print("Speed button clicked")
        time.sleep(1)

    def click_brand_button(self):
        self.get_brand_button().click()
        print("Brand button clicked")
        time.sleep(1)

    def click_scooter_cart_button(self):
        button = self.get_scooter_cart_button()
        self.driver.execute_script("arguments[0].click();", button)
        print("Scooter cart clicked")
        time.sleep(2)

    def click_helmet_button(self):
        button = self.get_helmet_button()
        self.driver.execute_script("arguments[0].click();", button)
        print("Scooter helmet button clicked")
        time.sleep(2)

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print("Button Go To Cart clicked")
        time.sleep(1)

    # Methods
    def filters(self):
        self.get_current_url()
        self.scroll_menu_1()
        self.click_features_input_1()
        self.scroll_menu_2()
        self.click_features_input_2()
        self.scroll_menu_3()
        self.input_price_1(700)
        self.input_price_2(1000)
        self.click_button_enter_price()
        self.scroll_menu_4()
        self.click_max_speed_button()
        self.click_brand_button()
        self.click_scooter_cart_button()
        self.click_helmet_button()
        self.click_go_to_cart_button()

