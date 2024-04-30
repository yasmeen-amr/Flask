import unittest
from selenium import webdriver

class TestAPIUI(unittest.TestCase):
    def setUp(self):
        # Set up Selenium WebDriver
        self.driver = webdriver.Chrome()

    def test_add_to_cart(self):
        # Open the web page
        self.driver.get('http://localhost:5000')  # Replace with the URL of your application

        # Find the "Add to Cart" button and click it
        add_to_cart_button = self.driver.find_element_by_xpath('//button[text()="Add to Cart"]')
        add_to_cart_button.click()

        # Verify that the product is added to the cart
        cart_items = self.driver.find_elements_by_xpath('//div[@class="cart-item"]')
        self.assertEqual(len(cart_items), 1)  # Check if there is one item in the cart

    # Add more UI test cases as needed

    def tearDown(self):
        # Quit Selenium WebDriver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
