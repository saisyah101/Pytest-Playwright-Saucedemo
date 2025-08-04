import pytest
from tests.pom.login_page import LoginPage
from test_data import LoginTestData


#Ensure the user can log in with valid credentials
# @pytest.mark.positive
@pytest.mark.parametrize ("valid_username", LoginTestData.VALID_USERNAMES)
def test_login_valid(goto_login_page, valid_username) -> None:
    # Given the user is on SwagLabs login page
    login_page = LoginPage(goto_login_page)
    # When the user enters valid username
    # And the user enters valid password
    # And clicks the login button
    login_page.login_flow(valid_username,LoginTestData.VALID_PASSWORD)
    #Then the user should be successfully logged in
    #And user directs to product catalogue page
    login_page.verify_login_success()