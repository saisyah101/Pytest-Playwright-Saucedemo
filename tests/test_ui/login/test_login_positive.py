import pytest
from tests.pages.login_page import LoginPage
from tests.test_data import LoginTestData


#Ensure the user can log in with valid credentials
@pytest.mark.parametrize ("valid_username", LoginTestData.VALID_USERNAMES)
def test_login_valid(goto_login_page, valid_username) -> None:
    login_page = LoginPage(goto_login_page)
    login_page.login_flow(valid_username,LoginTestData.VALID_PASSWORD)
    login_page.verify_login_success()