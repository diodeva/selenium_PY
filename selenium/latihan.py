import unittest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())

 
    def test_b_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        data = driver.find_element(By.CLASS_NAME, 'title').text
        self.assertIn("Products", data)
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_checkout(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.CLASS_NAME, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        data = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertIn("Sauce Labs Backpack", data)


    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()