import pytest
from tests import test_data
from tests.conftest import normal_login
from tests.pom.checkout import Checkout
from tests.pom.catalogue_page import CataloguePage


#Ensure user failed to checkout, miscalculation of subtotal price
@pytest.mark.xfail(reason="BUG: Subtotal price miscalculation(not rounded) for some sets of products combination")
def test_bug_checkout(normal_login):
    catalogue_page = CataloguePage(normal_login)
    checkout_page = Checkout(normal_login)
    products = test_data.CheckOutData.get_failed_product_set()
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
    checkout_page.fill_checkout_form("firstname","lastname", "4224424")
    checkout_page.verify_checkout_overview_page()
    checkout_page.verify_subtotal_price()
    checkout_page.verify_tax()
    checkout_page.verify_total_price()
    checkout_page.finish_checkout()
    checkout_page.verify_complete_page()
    checkout_page.back_to_home()