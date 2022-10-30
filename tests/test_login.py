from Pages import BasePage
from Pages.MainPage import MainPage, MainPageLocators
from selenium import webdriver


class TestMainPage:

    def test_name(self):
        driver = MainPage(self.driver)
        list_items = driver.get_elements(MainPageLocators.LIST_OF_ITEMS)
        assert driver.get_element_text(MainPageLocators.NAME_MAIN_PAGE) == MainPage.NAME
        assert len(list_items) == 6
