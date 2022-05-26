from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    request.cls.driver = driver



