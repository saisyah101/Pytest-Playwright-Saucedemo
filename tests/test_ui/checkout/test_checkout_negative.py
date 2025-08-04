import test_data
import pytest
from conftest import normal_login
from tests.pom.checkout import Checkout
from tests.pom.catalogue_page import CataloguePage


#Ensure the user fails to continue checkout with emptying firstname
@pytest.mark.parametrize("firstname, lastname, postalcode",
                         [("","",""),
                          ("","","320022"),
                          ("","Last",""),
                          ("","Last","544332")])
def test_invalid_firstname_checkout_form(normal_login, firstname, lastname, postalcode):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CheckOutData.get_random_combination()
    print(products)
    catalogue_page.add_button_clicks(products)
    checkout_page.goto_cart_page()
    checkout_page.verify_cart_page()
    checkout_page.verify_cart_item_visible(products)
    checkout_page.verify_remove_button_visible(products)
    checkout_page.verify_add_button_not_visible(products)
    checkout_page.verify_qty_text(products)
    checkout_page.goto_checkout_form()
    checkout_page.verify_checkout_form()
    checkout_page.fill_checkout_form(firstname,lastname, postalcode)
    checkout_page.verify_firstname_error_message()
    checkout_page.close_error_message()

#Ensure the user fails to continue checkout with emptying lastname
@pytest.mark.parametrize("firstname, lastname, postalcode",
                         [("First","",""),
                          ("First","","350395")])
def test_invalid_lastname_checkout_form(normal_login, firstname, lastname, postalcode):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CheckOutData.get_random_combination()
    print(products)
    catalogue_page.add_button_clicks(products)
    checkout_page.goto_cart_page()
    checkout_page.verify_cart_page()
    checkout_page.verify_cart_item_visible(products)
    checkout_page.verify_remove_button_visible(products)
    checkout_page.verify_add_button_not_visible(products)
    checkout_page.verify_qty_text(products)
    checkout_page.goto_checkout_form()
    checkout_page.verify_checkout_form()
    checkout_page.fill_checkout_form(firstname,lastname, postalcode)
    checkout_page.verify_lastname_error_message()
    checkout_page.close_error_message()


#Ensure the user fails to continue checkout with emptying postalcode
def test_invalid_postalcode_checkout_form(normal_login):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CheckOutData.get_random_combination()
    print(products)
    catalogue_page.add_button_clicks(products)
    checkout_page.goto_cart_page()
    checkout_page.verify_cart_page()
    checkout_page.verify_cart_item_visible(products)
    checkout_page.verify_remove_button_visible(products)
    checkout_page.verify_add_button_not_visible(products)
    checkout_page.verify_qty_text(products)
    checkout_page.goto_checkout_form()
    checkout_page.verify_checkout_form()
    checkout_page.fill_checkout_form("First","Last", "")
    checkout_page.verify_postalcode_error_message()
    checkout_page.close_error_message()