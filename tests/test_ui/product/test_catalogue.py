import pytest
from tests import test_data
from tests.conftest import normal_login
from tests.pages.catalogue_page import CataloguePage

def test_catalogue_page_layout(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_catalogue_page_element()

def test_catalogue_items_content(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_item_name(test_data.CatalogueData.expected_name_list)
    catalogue_page.verify_item_price(test_data.CatalogueData.expected_price_list)
    catalogue_page.verify_item_image(test_data.CatalogueData.all_products)
    catalogue_page.verify_add_button_visible(test_data.CatalogueData.all_products)
    catalogue_page.verify_add_remove_products(test_data.CatalogueData.all_products)

def test_sort(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_sort_dropdown_options()

def test_sort_name_az(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.select_option_az()
    catalogue_page.verify_name_sorting(ascending=True)

def test_sort_name_za(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.select_option_za()
    catalogue_page.verify_name_sorting(ascending=False)

def test_sort_name_lohi(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.select_option_lohi()
    catalogue_page.verify_price_sorting(ascending=True)

def test_sort_name_hilo(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.select_option_hilo()
    catalogue_page.verify_price_sorting(ascending=False)

@pytest.mark.parametrize("index, product_name, price, desc",[
                        (0,"Test.allTheThings() T-Shirt (Red)","$15.99","This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."),
                        (1,"Sauce Labs Onesie","$7.99","Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel."),
                        (2,"Sauce Labs Fleece Jacket","$49.99","It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office."),
                        (3,"Sauce Labs Bolt T-Shirt","$15.99","Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt."),
                        (4,"Sauce Labs Bike Light","$9.99","A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included."),
                        (5,"Sauce Labs Backpack","$29.99","carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")])
def test_goto_pdp_add_remove_back(normal_login, index, product_name, price, desc):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.select_option_za()
    catalogue_page.goto_product_detail_page(index)
    catalogue_page.verify_product_detail_page(product_name,price,desc)
    catalogue_page.add_product_pdp_click()
    catalogue_page.remove_product_pdp_click()
    catalogue_page.back_to_products_page()

