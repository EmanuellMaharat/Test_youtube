import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from retry import retry

@pytest.mark.usefixtures("setup")
class Testyoutube:
    @retry()
    def test_setup(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))
        element.send_keys("Emanuel")
        element.send_keys(Keys.ENTER)
    @retry()
    def test_two(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))
        element.send_keys("two")
        element.send_keys(Keys.ENTER)

    def teardown_method(self):
        self.driver.close()
        sleep(1)
        self.driver.quit()

