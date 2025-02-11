import datetime


class Base():

    # Constructor to initialize the driver
    def __init__(self, driver):
        self.driver = driver

    """ Method to get the current URL """
    def get_current_url(self):
        print("Current url " + self.driver.current_url)


    """ Method to take a screenshot """

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"./Screen/{name_screenshot}")
        print("Screenshot done")

    """ Method to assert the URL matches the expected URL """
    def assert_url(self, expected_url):
        current_url = self.driver.current_url
        assert expected_url in current_url, f"Expected part '{expected_url}', but got '{current_url}'"
        print("URL is correct")

    """ Method to assert the product name matches the expected text """
    def assert_product(self, element, expected_text):
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        print("Product name is correct")
