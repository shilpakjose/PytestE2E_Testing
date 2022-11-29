import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope ="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver =driver
    yield
    driver.close()




