import pytest
from tests.pages.login_page import LoginPage
from tests.test_data import LoginTestData


#Ensure the user fails to log in with an invalid username
@pytest.mark.parametrize ("invalid_username", LoginTestData.INVALID_USERNAMES)
@pytest.mark.parametrize ("password", LoginTestData.ANY_PASSWORDS)
def test_login_invalid_username(goto_login_page, invalid_username, password) -> None:
    login_page = LoginPage(goto_login_page)
    login_page.login_flow(invalid_username,password)
    login_page.verify_invalid_credentials_error()


#Ensure the user fails to log in with an invalid password
@pytest.mark.parametrize ("valid_username", LoginTestData.VALID_USERNAMES)
@pytest.mark.parametrize ("invalid_password", LoginTestData.INVALID_PASSWORDS)
def test_login_invalid_password(goto_login_page, valid_username, invalid_password) -> None:
    login_page = LoginPage(goto_login_page)
    login_page.login_flow(valid_username,invalid_password)
    login_page.verify_invalid_credentials_error()


#Ensure the user fails to log in with emptying username
@pytest.mark.parametrize ("password", LoginTestData.ANY_PASSWORDS)
def test_login_empty_username(goto_login_page, password) -> None:
    login_page = LoginPage(goto_login_page)
    login_page.login_flow("",password)
    login_page.verify_invalid_empty_username()

#Ensure the user fails to log in with emptying password
@pytest.mark.parametrize ("username", LoginTestData.VALID_USERNAMES)
def test_login_empty_password(goto_login_page, username) -> None:
    login_page = LoginPage(goto_login_page)
    login_page.login_flow(username,"")
    login_page.verify_invalid_empty_password()



