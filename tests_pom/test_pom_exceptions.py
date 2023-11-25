import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.exceptions_page import ExceptionsPage


class TestPOMExceptions:
    @pytest.mark.pom_exceptions
    def test_no_such_element_exception(self, driver: WebDriver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_button()
        assert exceptions_page.verify_row2_present(), "Row2 input field is not present"  # Exception without wait in verify_row2_present()

    @pytest.mark.pom_exceptions
    def test_element_not_interactable_exception(self, driver: WebDriver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_button()
        exceptions_page.type_in_row2_input_field("ABC")
        exceptions_page.click_row2_save_button()
        assert exceptions_page.confirmation_msg_text == exceptions_page.row2_saved_expected_conformation_msg, "Row2 confirmation message is not as expected"

    @pytest.mark.pom_exceptions
    def test_invalid_element_state_exception(self, driver: WebDriver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.clear_row1_input_field()
        new_text = "XYZ"
        exceptions_page.type_in_row1_input_field(new_text)
        exceptions_page.click_row1_save_button()
        print("exceptions_page.confirmation_msg_text: ", exceptions_page.confirmation_msg_text)
        print("exceptions_page.row1_expected_confirmation_msg: ", exceptions_page.row1_expected_confirmation_msg)
        assert exceptions_page.confirmation_msg_text == exceptions_page.row1_expected_confirmation_msg, "Row1 Confirmation message is not as expected"
        print(f"{exceptions_page.row1_input_field_text = }")
        assert exceptions_page.row1_input_field_text == new_text, f"{new_text} is not saved in row1 input field"

    @pytest.mark.pom_exceptions
    def test_stale_element_reference_exception(self, driver: WebDriver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        instructions_field = exceptions_page.instructions_field()
        print(f"instructions text before add button click = {instructions_field.text}")
        exceptions_page.click_add_button()
        '''
        #below code raises StaleElementReferenceException
        print(f"instructions text after add button click = {instructions_field.text}")
        '''
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.invisibility_of_element(instructions_field)), "instructions text should not have been displayed, but it is displayed"

    @pytest.mark.debug
    @pytest.mark.pom_exceptions
    def test_timeout_exception(self, driver: WebDriver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_button()
        assert exceptions_page.verify_row2_present(), "Row2 input field element is not displayed"  #verify_row2_present(3) gives TimeoutException
'''
Test case 5: TimeoutException
Open page
Click Add button
Wait for 3 seconds for the second input field to be displayed
Verify second input field is displayed
'''
