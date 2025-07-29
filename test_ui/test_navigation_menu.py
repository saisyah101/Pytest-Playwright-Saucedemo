import test_data
from conftest import normal_login
from pom.catalogue_page import CataloguePage

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