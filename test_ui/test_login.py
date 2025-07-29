import pytest

from pom.login_page import LoginPage
from pom.catalogue_page import CataloguePage
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


#Ensure the user fails to log in with an invalid username
@pytest.mark.parametrize ("invalid_username", LoginTestData.INVALID_USERNAMES)
@pytest.mark.parametrize ("password", LoginTestData.ANY_PASSWORDS)
def test_login_invalid_username(goto_login_page, invalid_username, password) -> None:
    # Given the user is on SwagLabs login page
    login_page = LoginPage(goto_login_page)
    # When the user enters invalid username
    # And the user enters any password
    # And clicks the login button
    login_page.login_flow(invalid_username,password)
    #Then the user should be failed logged in
    #And verify error message for invalid login is displayed
    #And user not directed to product catalogue page
    login_page.verify_invalid_credentials_error()


#Ensure the user fails to log in with an invalid password
@pytest.mark.parametrize ("valid_username", LoginTestData.VALID_USERNAMES)
@pytest.mark.parametrize ("invalid_password", LoginTestData.INVALID_PASSWORDS)
def test_login_invalid_password(goto_login_page, valid_username, invalid_password) -> None:
    # Given the user is on SwagLabs login page
    login_page = LoginPage(goto_login_page)
    # When the user enters invalid username
    # And the user enters valid password
    # And clicks the login button
    login_page.login_flow(valid_username,invalid_password)
    #Then the user should be failed logged in
    #And verify error message for invalid login is displayed
    #And user not directed to product catalogue page
    login_page.verify_invalid_credentials_error()


#Ensure the user fails to log in with emptying username
@pytest.mark.parametrize ("password", LoginTestData.ANY_PASSWORDS)
def test_login_empty_username(goto_login_page, password) -> None:
    # Given the user is on SwagLabs login page
    login_page = LoginPage(goto_login_page)
    # When the user not enters any username
    # And the user enters valid password
    # And clicks the login button
    login_page.login_flow("",password)
    #Then the user should be failed logged in
    #And verify error message for empty username is displayed
    #And user not directed to product catalogue page
    login_page.verify_invalid_empty_username()

#Ensure the user fails to log in with emptying password
@pytest.mark.parametrize ("username", LoginTestData.VALID_USERNAMES)
def test_login_empty_password(goto_login_page, username) -> None:
    # Given the user is on SwagLabs login page
    login_page = LoginPage(goto_login_page)
    # When the user enters valid username
    # And the user not enters any password
    # And clicks the login button
    login_page.login_flow(username,"")
    #Then the user should be failed logged in
    #And verify error message for empty username is displayed
    #And user not directed to product catalogue page
    login_page.verify_invalid_empty_password()



