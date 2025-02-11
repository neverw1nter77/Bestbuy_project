from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Choose_country(Base):
    # The URL for the BestBuy website
    url = "https://www.bestbuy.com/"

    COUNTRY_BUTTON = '//a[@class="us-link"]'

    # Getters

    def get_country_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.COUNTRY_BUTTON)))

    # Actions

    def click_country_button(self):
        self.get_country_button().click()
        print("Country button clicked")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_country_button()