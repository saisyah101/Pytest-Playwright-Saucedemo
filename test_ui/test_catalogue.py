import time

import pytest

import test_data
from conftest import normal_login
from pom.catalogue_page import CataloguePage
from test_data import CatalogueData

def test_catalogue_page_layout(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_catalogue_page_design()

def test_catalogue_items_content(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_item_name(test_data.CatalogueData.expected_name_list)
    catalogue_page.verify_item_price(test_data.CatalogueData.expected_price_list)
    catalogue_page.verify_item_image(test_data.CatalogueData.all_products)
    catalogue_page.verify_add_button_visible(test_data.CatalogueData.all_products)
    catalogue_page.verify_add_remove_product(test_data.CatalogueData.all_products)