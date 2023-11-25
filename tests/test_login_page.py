import time
import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # open browser
        # driver = webdriver.Chrome()
        # time.sleep(5)

        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # username
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        time.sleep(2)

        # submit
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # verify new page URL
        actual_url = driver.current_url
        print(actual_url)
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        successful_msg_element = driver.find_element(By.XPATH, "//h1")
        assert successful_msg_element.is_displayed(), "Successful message not displayed, so test failed"

        actual_text = successful_msg_element.text
        print(actual_text)
        assert actual_text == "Logged In Successfully", "Success message is not as expected"

        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.text == "Log out"
        actual_link = logout_button_locator.get_property("href")
        print(actual_link)
        assert actual_link == "https://practicetestautomation.com/practice-test-login/"
