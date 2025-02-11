import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.adress_page import Address_page
from pages.cart_page import Cart_page
from pages.choose_country_page import Choose_country
from pages.customer_page import Customer_page
from pages.final_page import Final_page
from pages.main_page import Main_page
from pages.product_page import Product_page

def wait():
    """Random delay from 2 to 5 seconds"""
    time.sleep(random.uniform(2, 5))

def test_buy_product():
    """Test of purchasing an item with anti-ban protection"""

    # Browser settings
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--incognito")

    # Driver initialization
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    try:
        wait()  # Pause before starting

        # Selecting the country
        choose_country = Choose_country(driver)
        choose_country.authorization()
        wait()

        # Opening the menu
        main_page = Main_page(driver)
        main_page.menu()
        wait()

        # Filtering products
        product_page = Product_page(driver)
        product_page.filters()
        wait()

        # Entering the cart
        cart_page = Cart_page(driver)
        cart_page.cart()
        wait()

        # Selecting product purchase options
        customer_page = Customer_page(driver)
        customer_page.guest()
        wait()

        # Enter the address.
        address_page = Address_page(driver)
        address_page.personal_data()

        # Check the correctness of the product.
        final = Final_page(driver)
        final.final()



    except Exception as e:
        print(f" Error in the test.: {e}")



if __name__ == "__main__":
    test_buy_product()






























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# from pages.choose_country_page import Choose_country
# from pages.main_page import Main_page
# from pages.product_page import Product_page
#
#
# def test_buy_product():
#     # Инициализация драйвера
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)  # Чтобы не закрывалось сразу
#     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#
#
#     # Выбираем страну
#     choose_country = Choose_country(driver)
#     choose_country.authorization()
#
#     main_page = Main_page(driver)
#     main_page.menu()
#
#     product_page = Product_page(driver)
#     product_page.filters()



