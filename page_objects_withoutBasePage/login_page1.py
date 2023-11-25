from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.ID, "username")
    __password_locator = (By.NAME, "password")
    __submit_button_locator = (By.ID, "submit")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        #self._driver = driver
        print("in execute_login")
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__username_locator))
        self._driver.find_element(*self.__username_locator).send_keys(username)

        wait.until(ec.visibility_of_element_located(self.__password_locator))
        self._driver.find_element(*self.__password_locator).send_keys(password)

        wait.until(ec.visibility_of_element_located(self.__submit_button_locator))
        self._driver.find_element(*self.__submit_button_locator).click()


