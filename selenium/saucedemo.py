import unittest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.Chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())
        # wedriver.Chrome(ChromeDriverManager())


    def test_a_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_saucew")
        driver.find_element(By.ID, "login-button").click()

        data = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", data)
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/")

    
    def test_b_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        data = driver.find_element(By.CLASS_NAME, 'title').text
        self.assertIn("Products", data)
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_c_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        # implicit wait
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, "[data-test=username]").send_keys("problem_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test=password]").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        # explicit wait
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test=error]")))
        data = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", data)
        driver.minimize_window()

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()