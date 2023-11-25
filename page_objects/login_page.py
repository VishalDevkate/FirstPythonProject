from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __login_page_url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.ID, "username")
    __password_locator = (By.NAME, "password")
    __submit_button_locator = (By.ID, "submit")
    __error_msg_element = (By.XPATH, "//div[@id=\"error\"]")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__login_page_url)

    def execute_login(self, username, password):
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click_button(self.__submit_button_locator)

    @property
    def error_message(self) -> str:
        return super()._text_of_element(self.__error_msg_element)