import time
import pytest
from selenium.webdriver.common.by import By

from page_objects_withoutBasePage.logged_in_successfully1 import LoggedInSuccessfullyPage
from page_objects_withoutBasePage.login_page1 import LoginPage


class TestPositiveScenarios:

    @pytest.mark.pom_login1
    @pytest.mark.pom_positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        # go to webpage
        login_page.open()

        # username
        login_page.execute_login("student", "Password123")

        # verify new page URL
        logged_in_successfully_page = LoggedInSuccessfullyPage(driver)
        actual_url = logged_in_successfully_page.current_url
        print("actual_url: ", actual_url)
        assert actual_url == logged_in_successfully_page.expected_logged_in_page_url, "actual url is not as expected"

        assert logged_in_successfully_page.if_successful_msg_element_displayed(), "Successful message not displayed, so test failed"

        actual_successful_msg_text = logged_in_successfully_page.successful_msg_element_text
        print("actual_successful_msg_text: ", actual_successful_msg_text)
        assert actual_successful_msg_text == logged_in_successfully_page.expected_successful_msg_element_text, "Success message is not as expected"

        # assert actual_successful_msg_text == "NegativeTest", "Success message is not as expected"

        assert logged_in_successfully_page.logout_button_text == logged_in_successfully_page.expected_logout_button_text, "logout button text is not as expected"

        actual_logout_button_link = logged_in_successfully_page.logout_button_link
        print("actual_logout_button_link: ", actual_logout_button_link)
        assert actual_logout_button_link == logged_in_successfully_page.expected_logout_button_link, "logout button link is not as expected"
