from tests import test_data
from tests.conftest import normal_login
from tests.pages.catalogue_page import CataloguePage

def test_sidebar_menu(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.verify_sidebar_menu()

def test_about_page(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.goto_sidebar_about()

def test_reset_page(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.add_all_products(test_data.CatalogueData.all_products)
    catalogue_page.goto_sidebar_reset()

#Login then Logout
def test_login_logout(normal_login) -> None:
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.goto_sidebar_logout()

def test_sidebar_from_pdp(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.goto_product_detail_page(0)
    catalogue_page.verify_sidebar_menu()

def test_about_page_form_pdp(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.goto_product_detail_page(0)
    catalogue_page.goto_sidebar_about()

def test_reset_page_form_pdp(normal_login):
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.add_all_products(test_data.CatalogueData.all_products)
    catalogue_page.goto_product_detail_page(0)
    catalogue_page.goto_sidebar_reset()

#Login then Logout
def test_login_pdp_logout(normal_login) -> None:
    catalogue_page = CataloguePage(normal_login)
    catalogue_page.goto_product_detail_page(0)
    catalogue_page.goto_sidebar_logout()