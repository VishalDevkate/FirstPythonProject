from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _wait_for_element_to_be_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, txt: str):
        self._wait_for_element_to_be_visible(locator)
        self._find(locator).send_keys(txt)

    def _click_button(self, locator: tuple):
        self._wait_for_element_to_be_visible(locator)
        self._find(locator).click()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _text_of_element(self, locator: tuple) -> str:
        self._wait_for_element_to_be_visible(locator)
        return self._find(locator).text

    def _link_of_element(self, locator: tuple) -> str:
        return self._find(locator).get_property("href")
