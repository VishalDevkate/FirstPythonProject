from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __expected_logged_in_page_url = "https://practicetestautomation.com/logged-in-successfully/"
    __successful_msg_element = (By.XPATH, "//h1")
    __expected_successful_msg = "Logged In Successfully"
    __expected_logout_button_text = "Log out"
    __logout_button_locator = (By.LINK_TEXT, "Log out")
    __expected_logout_button_locator_link = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_logged_in_page_url(self) -> str:
        return self.__expected_logged_in_page_url

    def if_successful_msg_element_displayed(self) -> bool:
        return super()._is_displayed(self.__successful_msg_element)

    def if_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_button_locator)

    @property
    def expected_successful_msg_element_text(self) -> str:
        return self.__expected_successful_msg

    @property
    def successful_msg_element_text(self, ) -> str:
        return super()._text_of_element(self.__successful_msg_element)

    @property
    def expected_logout_button_text(self) -> str:
        return self.__expected_logout_button_text

    @property
    def logout_button_text(self) -> str:
        return super()._text_of_element(self.__logout_button_locator)

    @property
    def expected_logout_button_link(self) -> str:
        return self.__expected_logout_button_locator_link

    @property
    def logout_button_link(self) -> str:
        return super()._link_of_element(self.__logout_button_locator)

    '''
    @property
    def current_url(self) -> str:
        return super()._current_url
    '''