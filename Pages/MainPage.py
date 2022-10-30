from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    NAME = "PRODUCTS"


class MainPageLocators:
    NAME_MAIN_PAGE = (By.XPATH, "//span[@class='title']")
    LIST_OF_ITEMS = (By.XPATH, "//div[@class='inventory_item_description']")
