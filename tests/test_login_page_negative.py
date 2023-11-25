import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username_value , password_value, expected_error_message",
                             [("stu", "Password123", "Your1 username is invalid!"),
                              ("student", "Password1", "Your password is invalid!")])
    def test_negative_login(self, driver, username_value, password_value, expected_error_message):
        # open browser
        # driver = webdriver.Chrome()

        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # username
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username_value)

        # password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password_value)

        # submit
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # verify error message
        error_msg_element = driver.find_element(By.XPATH, "//div[@id=\"error\"]")
        assert error_msg_element.is_displayed(), "Invalid Error message is not displayed so test failed"

        actual_text = error_msg_element.text
        print(actual_text)
        assert actual_text == expected_error_message, "Error message displayed is not as expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_username(self, driver):
        # open browser
        # driver = webdriver.Chrome()

        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # username
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("stu")

        # password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # submit
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # verify error message
        error_msg_element = driver.find_element(By.XPATH, "//div[@id=\"error\"]")
        assert error_msg_element.is_displayed(), "Invalid username Error message is not displayed so test failed"

        actual_text = error_msg_element.text
        print(actual_text)
        assert actual_text == "Your1 username is invalid!", "Error message is not as expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_password(self, driver):
        # open browser
        # driver = webdriver.Chrome()

        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # username
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password1")

        # submit
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # verify error message
        error_msg_element = driver.find_element(By.XPATH, "//div[@id=\"error\"]")
        assert error_msg_element.is_displayed(), "Invalid Password Error message is not displayed so test failed"

        actual_text = error_msg_element.text
        print(actual_text)
        assert actual_text == "Your password is invalid!", "Error message is not as expected"
