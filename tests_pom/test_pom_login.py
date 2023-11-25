import pytest

from page_objects.logged_in_successfully_page import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


@pytest.mark.pom_login
@pytest.mark.pom_positive_login
class TestPositiveLogin:
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()

        login_page.execute_login("student", "Password123")

        logged_in_successfully_page = LoggedInSuccessfullyPage(driver)

        print("actual_successful_msg_text: ", logged_in_successfully_page.successful_msg_element_text)
        assert logged_in_successfully_page.successful_msg_element_text == logged_in_successfully_page.expected_successful_msg_element_text, "Success message is not as expected"

        print("actual_logout_button_link: ", logged_in_successfully_page.logout_button_link)
        assert logged_in_successfully_page.expected_logout_button_link == logged_in_successfully_page.logout_button_link, "logout button link is not as expected"

        print("actual logout_button_text: ", logged_in_successfully_page.logout_button_text)
        assert logged_in_successfully_page.logout_button_text == logged_in_successfully_page.expected_logout_button_text, "logout button text is not as expected"

        assert logged_in_successfully_page.if_logout_button_displayed(), "Logout button not displayed"

        print("Actual current url: ", logged_in_successfully_page.current_url)
        assert logged_in_successfully_page.current_url == logged_in_successfully_page.expected_logged_in_page_url, "actual url is not as expected"
