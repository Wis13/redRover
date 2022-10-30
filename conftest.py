import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.TestData import TestData as TD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def init_driver_chrome():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return driver


def init_driver_firefox():

    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1600")
    options.add_argument("--height=1080")
    options.headless = True
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    return driver


@pytest.fixture(params=['chrome', 'firefox'], scope='class', autouse=True)
def init_driver(request):
    if request.param == 'chrome':
        driver = init_driver_chrome()
    elif request.param == 'firefox':
        driver = init_driver_firefox()
    else:
        print('Please pass the correct browser name: {}'.format(request.param))
        raise Exception('driver is not found')

    driver.get(TD.BASE_URL)
    if driver.title == "Swag Labs":
        WebDriverWait(driver, 90).until(ec.presence_of_element_located((By.ID, 'user-name'))).send_keys(TD.LOGIN)
        driver.find_element(By.ID, 'password').send_keys(TD.PASSWORD)
        driver.find_element(By.ID, 'login-button').click()
    request.cls.driver = driver
    yield driver

    driver.quit()
