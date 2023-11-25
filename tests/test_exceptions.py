import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        wait = WebDriverWait(driver, 10)
        row2_locator = wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # row2_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_locator.is_displayed(), "Row2 input field not displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        row2_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")

        row2_locator.send_keys("ABC")
        # row2_locator.send_keys(Keys.TAB)

        # save_button = driver.find_element(By.NAME, "Save") #ElementNotInteractableException since looks for 1st save button (i.e. of row1)
        # save_button.click()
        # save_button = wait.until(expected_conditions.element_to_be_clickable((By.NAME, "Save")))
        # ActionChains(driver).move_to_element(save_button).click(save_button).perform()
        """
        CSS selector of button present in class = "some-class":
        div.some-class > button
        To verify CSS selector in Console:
        $$("div.row > button")
        $$("div.row > button")[3]
        $$("button#save_btn.btn")
        $$("button#save_btn.btn")[1]
        
        Alternately by xpath:
        $x("//div[@id='row2']/button")
        $x("//div[@id='row2']/button[1]")
        $x("//div[@id='row2']/button")[0]
        """
        save_button = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        # save_button = driver.find_elements(By.XPATH, "//button[@name='Save']")[1]
        # save_button = driver.find_elements(By.CSS_SELECTOR, "div.row > button")[3] # gives 6 buttons, then select 4th button by subscript [3]
        # save_button = driver.find_elements(By.CSS_SELECTOR, "button#save_btn.btn")[1]  # gives 2 buttons, then select 2nd button by subscript [1]
        # save_button = driver.find_element(By.XPATH, "//div[@id='row2']/button[1]")
        # save_button = driver.find_elements(By.XPATH, "//div[@id='row2']/button")[0]
        # save_button = driver.find_elements(By.NAME, "Save")[1]

        save_button.click()

        # confirmation_message = driver.find_element(By.ID, "confirmation") # If this gives exception, use below
        confirmation_message = wait.until(expected_conditions.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message_text = confirmation_message.text
        print(confirmation_message_text)
        assert confirmation_message_text == "Row 2 was saved", "Row2 confirmation message is not as expected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        input_field = driver.find_element(By.XPATH, "//div[@id='row1']/input[@value='Pizza']")
        # input_field.clear()   # InvalidElementStateException
        # time.sleep(2)

        # Type text into the input field
        new_text_given = "XYZ"
        # input_field.send_keys(new_text)  #ElementNotInteractableException
        edit_button = driver.find_element(By.ID, "edit_btn")
        edit_button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(
            input_field))  # because input_field may not be immediately clickable/editable after edit button click
        input_field.clear()
        input_field.send_keys(new_text_given)
        save_button = driver.find_element(By.ID, "save_btn")
        save_button.click()

        # Verify text changed
        confirmation_message = wait.until(expected_conditions.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message_text = confirmation_message.text
        assert confirmation_message_text == "Row 1 was saved", "Confirmation message is not as expected"

        new_text_saved = input_field.get_attribute("value")
        print(new_text_saved)
        assert new_text_given == new_text_saved, f"new text given was {new_text_given}, but {new_text_saved} got saved"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instructions_text = driver.find_element(By.ID, "instructions")

        # Push add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        # Verify instruction text element is no longer displayed
        # below line throws StaleElementReferenceException
        # assert instructions_text.is_displayed() == False, "instructions_text element should not have displayed, but it is displayed"
        """
        try:
            assert instructions_text.is_displayed() == False, "instructions_text element should not have displayed, but it is displayed"
        except StaleElementReferenceException:
            print("instructions_text element is no longer displayed")
        """

        wait = WebDriverWait(driver, 10)
        # assert wait.until(expected_conditions.staleness_of(instructions_text)) == True, "instructions_text element should not have displayed, but it is displayed"

        # assert wait.until(expected_conditions.invisibility_of_element(instructions_text)), "instructions_text element should not have displayed, but it is displayed"

        assert wait.until(expected_conditions.invisibility_of_element_located((
            By.ID, "instructions"))), "instructions_text element should not have displayed, but it is displayed"

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        wait = WebDriverWait(driver, 10)   #3 seconds gives TimeoutException
        row2_locator = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Failed waiting for row2 input element to be displayed")
        
        assert row2_locator.is_displayed(), "Row2 input field not displayed"
