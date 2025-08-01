import pytest
import test_data
from conftest import normal_login
from pom.catalogue_page import CataloguePage

def test_catalogue_page_layout(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_catalogue_page_design()

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

def test_goto_pdp_add_remove_back(normal_login):
    catalogue_page = CataloguePage(normal_login)
    product_name = "Test.allTheThings() T-Shirt (Red)"
    price = "$15.99"
    desc = "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."
    catalogue_page.select_option_za()
    catalogue_page.goto_product_detail_page(product_name,price,desc)
    catalogue_page.add_product_pdp_click()
    catalogue_page.remove_product_pdp_click()
    catalogue_page.back_to_products_page()

