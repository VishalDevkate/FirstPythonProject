from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __exceptions_page_url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_Locator = (By.ID, "add_btn")
    __row2_added_successful_msg_locator = (By.XPATH, "//div[@id='confirmation']")
    __row2_saved_successful_msg = "Row 2 was saved"
    __row2_input_field_locator = (By.XPATH, "//div[@id='row2']/input")
    __row2_save_button_locator = (
    By.XPATH, "(//button[@name='Save'])[2]")  # (By.NAME, "Save") gives ElementNotInteractableException
    __confirmation_msg_locator = (By.XPATH, "//div[@id='confirmation']")
    __row1_input_field_locator = (By.XPATH, "//div[@id='row1']/input")
    __edit_button_locator = (By.XPATH, "//div[@id='row1']/button[@name='Edit']")
    __row1_save_button_locator = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row1_saved_successful_msg = "Row 1 was saved"
    __instructions_field_locator = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__exceptions_page_url)

    def click_add_button(self):
        super()._click_button(self.__add_button_Locator)

    def verify_row2_present(self, time: int = 10) -> bool:
        super()._wait_for_element_to_be_visible(self.__row2_input_field_locator, time)
        return super()._is_displayed(self.__row2_input_field_locator)

    def type_in_row2_input_field(self, input_text: str):
        super()._type(self.__row2_input_field_locator, input_text)

    def click_row2_save_button(self):
        super()._click_button(self.__row2_save_button_locator)

    @property
    def confirmation_msg_text(self) -> str:
        return super()._text_of_element(self.__confirmation_msg_locator)

    @property
    def row2_saved_expected_conformation_msg(self) -> str:
        return self.__row2_saved_successful_msg

    def clear_row1_input_field(self):
        # super()._find(self.__row1_input_field_locator).clear()  #exception
        super()._click_button(self.__edit_button_locator)
        super()._find(self.__row1_input_field_locator).clear()

    def type_in_row1_input_field(self, input_txt: str):
        super()._type(self.__row1_input_field_locator, input_txt)

    def click_row1_save_button(self):
        super()._click_button(self.__row1_save_button_locator)

    @property
    def row1_expected_confirmation_msg(self) -> str:
        return self.__row1_saved_successful_msg

    @property
    def row1_input_field_text(self) -> str:
        return super()._find(self.__row1_input_field_locator).get_attribute("value")

    @property
    def instructions_field_text(self) -> str:
        return super()._text_of_element(self.__instructions_field_locator)

    # def verify_if_instructions_field_displayed(self) -> bool:
    #     return super()._is_displayed(self.__instructions_field_locator)

    @property
    def instructions_field_text_after_add_button_click(self) -> str:
        return super()._find(self.__instructions_field_locator).text

    def instructions_field(self) -> WebElement:
        return super()._find(self.__instructions_field_locator)

    def row2_input_field_is_displayed(self) -> bool:
        return super()._find(self.__row2_input_field_locator).is_displayed()