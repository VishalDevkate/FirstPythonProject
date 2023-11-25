import pytest

from page_objects.login_page import LoginPage


class TestNegativeLogin:
    @pytest.mark.pom_login
    @pytest.mark.pom_negative_login
    @pytest.mark.parametrize("username_value , password_value, expected_error_message",
                             [("stu", "Password123", "Your username is invalid!"),
                              ("student", "Password1", "Your password is invalid!"),
                              ("stu", "Password123", "Your1 username is invalid!"),
                              ("student", "Password1", "Your1 password is invalid!")])
    def test_negative_login(self, driver, username_value, password_value, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username_value, password_value)
        assert login_page.error_message == expected_error_message, "Error message displayed is not as expected"