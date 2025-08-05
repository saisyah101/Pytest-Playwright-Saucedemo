import pytest
from tests.conftest import problem_user_login, error_user_login
from tests.pom.problem_user import KnownBug

def test_bug_catalogue_problem_user(problem_user_login):
    """
    Known bug: When login using problem user,
    user can't add or remove products to cart on catalogue page
    and the sorting doesn't work properly
    """
    catalogue_page = KnownBug(problem_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.verify_bug_cant_remove_backpack()
    catalogue_page.verify_bug_cant_remove_bike()
    catalogue_page.verify_bug_cant_remove_onsie()
    catalogue_page.verify_bug_cant_add_bolt_tshirt()
    catalogue_page.verify_bug_cant_add_jacket()
    catalogue_page.verify_bug_cant_add_red_tshirt()
    catalogue_page.verify_bug_sorting()

@pytest.mark.parametrize("index, expected_name, unexpected_name, button_type",[
                        (0,"Sauce Labs Backpack","Sauce Labs Fleece Jacket","bug add"),
                        (1,"Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","bug add"),
                        (2,"Sauce Labs Bolt T-Shirt","Sauce Labs Onesie","bug remove"),
                        (3,"Sauce Labs Fleece Jacket","ITEM NOT FOUND","bug remove"),
                        (4,"Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)","bug add"),
                        (5,"Test.allTheThings() T-Shirt (Red)","Sauce Labs Backpack","bug remove")])
def test_bug_product_detail_problem_user(problem_user_login, index, expected_name, unexpected_name, button_type):
    """
    Known bug: When login using problem user,
    user can't add or remove products to cart on product detail page
    and the wrong product detail is displayed
    """
    catalogue_page = KnownBug(problem_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.goto_product_detail_page(index)
    catalogue_page.verify_bug_product_detail_page_problem_user(expected_name, unexpected_name)
    catalogue_page.bug_button(button_type)


def test_bug_checkout_problem_user(problem_user_login):
    """
    Known bug: When login using problem user, user can't fill lastname
    so user can't successfully do checkout
    """
    catalogue_page = KnownBug(problem_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.add_product("backpack")
    catalogue_page.add_product("bike")
    catalogue_page.add_product("onsie")
    catalogue_page.goto_cart_page()
    catalogue_page.verify_cart_page()
    catalogue_page.goto_checkout_form()
    catalogue_page.verify_checkout_form()
    catalogue_page.verify_bug_cant_fill_lastname_problem_user("firstname", "lastname", "223424")
    catalogue_page.verify_lastname_error_message()

def test_bug_catalogue_error_user(error_user_login):
    """
    Known bug: user can't add or remove products to cart on catalogue page
    and the sorting doesn't work properly
    """
    catalogue_page = KnownBug(error_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.verify_bug_cant_remove_backpack()
    catalogue_page.verify_bug_cant_remove_bike()
    catalogue_page.verify_bug_cant_remove_onsie()
    catalogue_page.verify_bug_cant_add_bolt_tshirt()
    catalogue_page.verify_bug_cant_add_jacket()
    catalogue_page.verify_bug_cant_add_red_tshirt()

@pytest.mark.parametrize("index, expected_name, button_type",[
                        (0,"Sauce Labs Backpack","bug remove"),
                        (1,"Sauce Labs Bike Light","bug remove"),
                        (2,"Sauce Labs Bolt T-Shirt","bug add"),
                        (3,"Sauce Labs Fleece Jacket","bug add"),
                        (4,"Sauce Labs Onesie","bug remove"),
                        (5,"Test.allTheThings() T-Shirt (Red)","bug add")])
def test_bug_product_detail_error_user(error_user_login, index, expected_name, button_type):
    """
    Known bug: When login using error user,
    user can't add or remove products to cart on product detail page
    """
    catalogue_page = KnownBug(error_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.goto_product_detail_page(index)
    catalogue_page.verify_bug_product_detail_page_error_user(expected_name)
    catalogue_page.bug_button(button_type)

def test_bug_checkout_error_user(error_user_login):
    """
    Known bug: When login using error user, user can access checkout overview page
    even if the lastname field is empty
    and user can't complete checkout after click finish button,
    nothing happens and the user remains on the checkout overview page
    """
    catalogue_page = KnownBug(error_user_login)
    catalogue_page.verify_catalogue_page_element()
    catalogue_page.add_product("backpack")
    catalogue_page.add_product("bike")
    catalogue_page.add_product("onsie")
    catalogue_page.goto_cart_page()
    catalogue_page.verify_cart_page()
    catalogue_page.goto_checkout_form()
    catalogue_page.verify_checkout_form()
    catalogue_page.verify_bug_cant_fill_lastname_error_user("firstname", "lastname", "223424")
    catalogue_page.verify_checkout_overview_page()
    catalogue_page.verify_subtotal_price()
    catalogue_page.verify_tax()
    catalogue_page.verify_total_price()
    catalogue_page.bug_finish_checkout()

