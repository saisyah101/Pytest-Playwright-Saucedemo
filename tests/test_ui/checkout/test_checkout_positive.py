import test_data
import pytest
from conftest import normal_login
from tests.pom.checkout import Checkout
from tests.pom.catalogue_page import CataloguePage


#Ensure user successfully checkout using valid products and valid data input
@pytest.mark.parametrize("firstname, lastname, postalcode",
                         [("Test", "Checkout", "33221"),
                          ("Test", "0001", "Z4242I"),
                          ("0002", "Test", "POSTAL"),
                          ("Some_Thing", "@Test", "2-3-4-2-1")])
def test_valid_checkout(normal_login, firstname, lastname, postalcode):
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
    checkout_page.verify_checkout_overview_page()
    checkout_page.verify_subtotal_price()
    checkout_page.verify_tax()
    checkout_page.verify_total_price()
    checkout_page.finish_checkout()
    checkout_page.verify_complete_page()
    checkout_page.back_to_home()

#Ensure user successfully checkout using valid products from product detail page and valid data input
def test_checkout_from_product_page(normal_login):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    product_name = "Sauce Labs Backpack"
    product = ["backpack"]
    price = "$29.99"
    desc = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    catalogue_page.goto_product_detail_page(0)
    catalogue_page.verify_product_detail_page(product_name,price,desc)
    catalogue_page.add_product_pdp_click()
    checkout_page.goto_cart_page()
    checkout_page.verify_cart_page()
    checkout_page.verify_cart_item_visible(product)
    checkout_page.verify_remove_button_visible(product)
    checkout_page.verify_add_button_not_visible(product)
    checkout_page.verify_qty_text(product)
    checkout_page.goto_checkout_form()
    checkout_page.verify_checkout_form()
    checkout_page.fill_checkout_form("firstname", "lastname", "4424242")
    checkout_page.verify_checkout_overview_page()
    checkout_page.verify_subtotal_price()
    checkout_page.verify_tax()
    checkout_page.verify_total_price()
    checkout_page.finish_checkout()
    checkout_page.verify_complete_page()
    checkout_page.back_to_home()

