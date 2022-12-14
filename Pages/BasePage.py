from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    list of the methods:
        init
        get_title
        get_current_url
        go_to_page
        click
        clear
        is_visible
        is_clickable
        get_element
        get_element_text
        get_wait
        do_send_keys
        scroll_to_bottom
        js_click
        hover_over_element
        hover_element1_and_click_element2
        get_name_current_window
        get_names_open_windows
        switch_to_window
    """

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_to_page(self, url: str):
        self.driver.get(url)
        return self

    def click(self, locator: tuple):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def clear(self, locator: tuple):
        element = self.driver.find_element(locator[0], locator[1])
        element.clear()

    def is_visible(self, locator: tuple):
        condition = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return bool(element)

    def is_clickable(self, locator: tuple):
        condition = ec.element_to_be_clickable(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return bool(element)

    def is_disabled(self, locator: tuple):
        element = self.driver.find_element(locator[0], locator[1])
        attribute = element.get_attribute("class")
        return attribute == "disabled"

    def is_enabled(self, locator: tuple):
        element = self.driver.find_element(locator[0], locator[1])
        attribute = element.get_attribute("class")
        return attribute == ""

    def is_element_not_present(self, locator: tuple):
        try:
            self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return True
        return False

    def is_element_present(self, locator: tuple):
        try:
            self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return False
        return True

    def get_element(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def get_elements(self, locator):
        elements = self.driver.find_elements(locator[0], locator[1])
        return elements

    def get_elements_text(self, locator):
        elements = self.get_elements(locator)
        text_elements = []
        for el in elements:
            text_elements.append(el.text)
        return text_elements

    def get_elements_attribute(self, locator, attribute):
        elements = self.get_elements(locator)
        attr_elements = []
        for el in elements:
            attr_elements.append(el.get_attribute(attribute))
        return attr_elements

    def get_element_attribute(self, locator, attribute):
        element = self.get_element(locator)
        return element.get_attribute(attribute)

    def get_element_text(self, locator):
        condition = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return element.text

    def get_wait(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def get_wait_and_click(self, locator):
        self.get_wait(locator)
        self.click(locator)

    def get_wait_is_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    def get_wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present())

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def js_click(self, locator):
        self.driver.execute_script("arguments[0].click();", self.click(locator))

    def hover_over_element(self, locator: tuple):
        action = ActionChains(self.driver)
        element = self.driver.find_element(locator[0], locator[1])
        action.move_to_element(element).perform()

    def hover_element1_and_click_element2(self, locator1: tuple, locator2: tuple):
        action = ActionChains(self.driver)
        element_to_hover_over = self.driver.find_element(locator1[0], locator1[1])
        element_to_click = self.driver.find_element(locator2[0], locator2[1])
        action.move_to_element(element_to_hover_over).click(element_to_click).perform()

    def get_name_current_window(self):
        return self.driver.current_window_handle

    def get_names_open_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def do_send_keys_script(self, element, text):
        self.driver.execute_script('arguments[0].CodeMirror.setValue("' + text + '");', element)
