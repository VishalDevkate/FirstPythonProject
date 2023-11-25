from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    __expected_logged_in_page_url = "https://practicetestautomation.com/logged-in-successfully/"
    __successful_msg_element = (By.XPATH, "//h1")
    __expected_successful_msg = "Logged In Successfully"
    __logout_button_locator = (By.LINK_TEXT, "Log out")
    __expected_logout_button_locator_link = "https://practicetestautomation.com/practice-test-login/"
    __expected_logout_button_text = "Log out"

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_logged_in_page_url(self) -> str:
        return self.__expected_logged_in_page_url

    def if_successful_msg_element_displayed(self) -> bool:
        try:
            return self._driver.find_element(*self.__successful_msg_element).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def successful_msg_element_text(self) -> str:
        return self._driver.find_element(*self.__successful_msg_element).text

    @property
    def expected_successful_msg_element_text(self) -> str:
        return self.__expected_successful_msg

    @property
    def logout_button_text(self) -> str:
        return self._driver.find_element(*self.__logout_button_locator).text

    @property
    def expected_logout_button_text(self) -> str:
        return self.__expected_logout_button_text

    @property
    def logout_button_link(self) -> str:
        return self._driver.find_element(*self.__logout_button_locator).get_property("href")

    @property
    def expected_logout_button_link(self) -> str:
        return self.__expected_logout_button_locator_link
