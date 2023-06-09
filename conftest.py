import pytest

from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()  # инстанс драйвера для FF
def driver():
    driver = webdriver.WebDriver(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
