import pytest

from tests import test_data


@pytest.fixture
def goto_login_page(page):
    page.goto("https://www.saucedemo.com/")
    return page

@pytest.fixture
def normal_login(goto_login_page):
    page = goto_login_page
    page.locator("[data-test=\"username\"]").fill(test_data.LoginTestData.STD_USERNAME)
    page.locator("[data-test=\"password\"]").fill(test_data.LoginTestData.VALID_PASSWORD)
    page.locator("[data-test=\"login-button\"]").click()
    return page

@pytest.fixture
def problem_user_login(goto_login_page):
    page = goto_login_page
    page.locator("[data-test=\"username\"]").fill(test_data.LoginTestData.PROBLEM_USER)
    page.locator("[data-test=\"password\"]").fill(test_data.LoginTestData.VALID_PASSWORD)
    page.locator("[data-test=\"login-button\"]").click()
    return page

@pytest.fixture
def error_user_login(goto_login_page):
    page = goto_login_page
    page.locator("[data-test=\"username\"]").fill(test_data.LoginTestData.ERR_USER)
    page.locator("[data-test=\"password\"]").fill(test_data.LoginTestData.VALID_PASSWORD)
    page.locator("[data-test=\"login-button\"]").click()
    return page