import test_data
import pytest
from conftest import normal_login
from pom.checkout import Checkout
from pom.catalogue_page import CataloguePage


#Ensure user successfully checkout using valid products and valid data input
@pytest.mark.parametrize("firstname, lastname, postalcode",
                         [("Test", "Checkout", "33221"),
                          ("Test", "0001", "Z4242I"),
                          ("0002", "Test", "POSTAL"),
                          ("Some_Thing", "@Test", "2-3-4-2-1")])
def test_valid_checkout(normal_login, firstname, lastname, postalcode):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CatalogueData.get_random_combination()
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
    checkout_page.verify_checkout_overview_page()
    checkout_page.verify_subtotal_price()
    checkout_page.verify_tax()
    checkout_page.verify_total_price()
    checkout_page.finish_checkout()
    checkout_page.verify_complete_page()
    checkout_page.back_to_home()

#Ensure the user fails to continue checkout with emptying firstname
@pytest.mark.parametrize("firstname, lastname, postalcode",
                         [("","",""),
                          ("","","320022"),
                          ("","Last",""),
                          ("","Last","544332")])
def test_invalid_firstname_checkout_form(normal_login, firstname, lastname, postalcode):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CatalogueData.get_random_combination()
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
    products = test_data.CatalogueData.get_random_combination()
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
    products = test_data.CatalogueData.get_random_combination()
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


