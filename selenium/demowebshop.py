import unittest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())


    def test_empty_firstname(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()

    def test_empty_lastname(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("")
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()

    def test_empty_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()

    def test_wrong_format_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("superQAgmailcom")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()

    def test_empty_confirmpassword(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()

    def test_password_not_match(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("suer123")
        driver.find_element(By.ID, "register-button").click()

    def test_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.ID, "FirstName").send_keys("Tester")
        driver.find_element(By.ID, "LastName").send_keys("One")
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("super123")
        driver.find_element(By.ID, "register-button").click()


    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()