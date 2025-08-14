from playwright.sync_api import Page,expect

class CataloguePage:
    def __init__(self, page: Page):
        self.page = page

        #Locator
        self.products_title = page.locator("[data-test='title']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.inventory_item = page.locator("[data-test='inventory-item']")
        self.item_label_name = page.locator("[data-test='inventory-item-name']")
        self.item_price = page.locator("[data-test='inventory-item-price']")
        self.add_button_pdp = page.locator("[data-test='add-to-cart']")
        self.remove_button_pdp = page.locator("[data-test='remove']")
        self.desc_pdp = page.locator("[data-test='inventory-item-desc']")
        self.image_products = {
            "backpack": self.page.locator("[data-test='inventory-item-sauce-labs-backpack-img']"),
            "bike": self.page.locator("[data-test='inventory-item-sauce-labs-bike-light-img']"),
            "bolt_tshirt": self.page.locator("[data-test='inventory-item-sauce-labs-bolt-t-shirt-img']"),
            "jacket": self.page.locator("[data-test='inventory-item-sauce-labs-fleece-jacket-img']"),
            "onsie": self.page.locator("[data-test='inventory-item-sauce-labs-onesie-img']"),
            "red_tshirt": self.page.locator("[data-test='inventory-item-test.allthethings()-t-shirt-(red)-img']")
        }
        self.add_buttons = {
            "backpack": self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']"),
            "bike": self.page.locator("[data-test='add-to-cart-sauce-labs-bike-light']"),
            "bolt_tshirt": self.page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"),
            "jacket": self.page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']"),
            "onsie": self.page.locator("[data-test='add-to-cart-sauce-labs-onesie']"),
            "red_tshirt": self.page.locator("[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
        }
        self.remove_buttons = {
            "backpack": self.page.locator("[data-test='remove-sauce-labs-backpack']"),
            "bike": self.page.locator("[data-test='remove-sauce-labs-bike-light']"),
            "bolt_tshirt": self.page.locator("[data-test='remove-sauce-labs-bolt-t-shirt']"),
            "jacket": self.page.locator("[data-test='remove-sauce-labs-fleece-jacket']"),
            "onsie": self.page.locator("[data-test='remove-sauce-labs-onesie']"),
            "red_tshirt": self.page.locator("[data-test='remove-test.allthethings()-t-shirt-(red)']")
        }
        self.sidebar_menu = page.get_by_role("button", name="Open Menu")
        self.sidebar_close = page.get_by_role("button", name="Close Menu")
        self.sidebar_inventory = page.locator("[data-test='inventory-sidebar-link']")
        self.sidebar_about = page.locator("[data-test='about-sidebar-link']")
        self.sidebar_logout = page.locator("[data-test='logout-sidebar-link']")
        self.login_button = page.locator("[data-test='login-button']")
        self.sidebar_reset= page.locator("[data-test='reset-sidebar-link']")
        self.sort_container = page.locator("[data-test='product-sort-container']")
        self.dropdown = page.locator("select.product_sort_container")
        self.back_button = page.locator("[data-test='back-to-products']")


###Catalogue Page
    def verify_catalogue_page_element(self):
        """
        To verify products title, cart icon, sort container, and sidebar menu are visible
        And to verify cart badge is not visible in the initial state
        """
        expect(self.products_title).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.cart_badge).not_to_be_visible()
        expect(self.sort_container).to_be_visible()
        expect(self.sidebar_menu).to_be_visible()
        return self

    def verify_specific_element(self, locator, expected_value, element_type):
        """
        To verify text of specific element is as expected
        """
        actual_count = locator.count()
        expected_count = len(expected_value)
        assert actual_count == expected_count, f"Expected {expected_count} {element_type} items, but found {actual_count}"

        for i, expected_value in enumerate(expected_value):
            actual_value = locator.nth(i).inner_text()
            expect(locator.nth(i)).to_have_text(expected_value), f"Item {i + 1}: Expected '{expected_value}', got '{actual_value}'"
        return self

    def verify_item_name(self, expected_name: list):
        """
        To verify text of every item label name is as expected
        """
        return self.verify_specific_element(self.item_label_name, expected_name, "name")

    def verify_item_price(self, expected_price:list ):
        """
        To verify text of every item price is as expected
        """
        return self.verify_specific_element(self.item_price, expected_price, "price")

    def verify_specific_item_visible(self, products:list, locator_map, element_type):
        for product in products:
            assert product in locator_map, f"{element_type} not found for product: '{product}'"
            product_locator = locator_map[product]
            expect(product_locator).to_be_visible()
        return self

    def action_button_clicks(self, products:list, locator_map, element_type):
        for product in products:
            assert product in locator_map, f"Cannot click {element_type} for product: '{product}'"
            locator_map[product].click()
        return self

    def verify_item_image(self, products:list):
        return self.verify_specific_item_visible(products, self.image_products, "Image products")

    def verify_add_button_visible(self, products: list):
        return self.verify_specific_item_visible(products, self.add_buttons, "Add button")

    def verify_remove_button_visible(self, products: list):
        return self.verify_specific_item_visible(products, self.remove_buttons, "Remove button")

    def add_button_clicks(self, products: list):
        return self.action_button_clicks(products, self.add_buttons, "Add button")

    def remove_button_clicks(self, products: list):
        return self.action_button_clicks(products, self.remove_buttons, "Remove button")

    def add_all_products(self, products: list):
        self.verify_add_button_visible(products)
        self.add_button_clicks(products)
        self.verify_remove_button_visible(products)
        expect(self.cart_badge).to_have_text("6")

    def verify_add_remove_products(self, products: list):
        self.add_all_products(products)
        self.remove_button_clicks(products)
        self.verify_add_button_visible(products)
        return self

###Sidebar Menu
    def verify_sidebar_menu(self):
        expect(self.sidebar_menu).to_be_visible()
        self.sidebar_menu.click()
        expect(self.sidebar_inventory).to_be_visible()
        expect(self.sidebar_inventory).to_have_text("All Items")
        expect(self.sidebar_about).to_be_visible()
        expect(self.sidebar_about).to_have_text("About")
        expect(self.sidebar_logout).to_be_visible()
        expect(self.sidebar_logout).to_have_text("Logout")
        expect(self.sidebar_reset).to_be_visible()
        expect(self.sidebar_reset).to_have_text("Reset App State")
        expect(self.sidebar_close).to_be_visible()
        self.sidebar_close.click()
        expect(self.sidebar_inventory).not_to_be_visible()
        expect(self.sidebar_about).not_to_be_visible()
        expect(self.sidebar_logout).not_to_be_visible()
        expect(self.sidebar_reset).not_to_be_visible()

        return self

    def sidebar_menu_directs(self, target):
        self.sidebar_menu.click()

        if target == "All Items":
            self.sidebar_inventory.click()
            expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        elif target == "About":
            self.sidebar_about.click()
            expect(self.page).to_have_url("https://saucelabs.com/")
        elif target == "Logout":
            self.sidebar_logout.click()
            expect(self.login_button).to_be_visible()
        elif target == "Reset":
            self.sidebar_reset.click()
            expect(self.cart_badge).not_to_be_visible()
        else:
            raise ValueError(f"Invalid sidebar target: {target}")

        return self

    def goto_sidebar_inventory(self):
        return self.sidebar_menu_directs("All Items")

    def goto_sidebar_about(self):
        return self.sidebar_menu_directs("About")

    def goto_sidebar_logout(self):
        return self.sidebar_menu_directs("Logout")

    def goto_sidebar_reset(self):
        return self.sidebar_menu_directs("Reset")


###Sorting Catalogue
    def verify_sort_dropdown_options(self):
        expect(self.sort_container).to_be_visible()
        self.sort_container.click()

        option_az = self.dropdown.locator("option[value='az']")
        expect(option_az).to_have_text("Name (A to Z)")

        option_za = self.dropdown.locator("option[value='za']")
        expect(option_za).to_have_text("Name (Z to A)")

        option_lohi = self.dropdown.locator("option[value='lohi']")
        expect(option_lohi).to_have_text("Price (low to high)")

        option_hilo = self.dropdown.locator("option[value='hilo']")
        expect(option_hilo).to_have_text("Price (high to low)")
        return self

    ## get text of products name
    def get_product_names(self):
        return self.item_label_name.all_inner_texts()

    ##get text of product prices (remove the $$$)
    def get_product_prices(self):
        price_texts = self.item_price.all_inner_texts()
        return [float(price.replace('$', '')) for price in price_texts]

    ##select option sort a-z
    def select_option_az(self):
        self.dropdown.select_option("az")
        self.page.wait_for_timeout(500)
        return self

    ##select option sort z-a
    def select_option_za(self):
        self.dropdown.select_option("za")
        self.page.wait_for_timeout(500)
        return self

    ##select option sort price low-high
    def select_option_lohi(self):
        self.dropdown.select_option("lohi")
        self.page.wait_for_timeout(500)
        return self

    ##select option sort price high-low
    def select_option_hilo(self):
        self.dropdown.select_option("hilo")
        self.page.wait_for_timeout(500)
        return self

    ##verify name sorting result is correct
    def verify_name_sorting(self, ascending=True):
        names = self.get_product_names()
        expected = sorted(names, reverse=not ascending)
        assert names == expected, f"Name sorting failed. Expected: {expected}, Got: {names}"
        return self

    ##verify price sorting result is correct
    def verify_price_sorting(self, ascending=True):
        prices = self.get_product_prices()
        expected = sorted(prices, reverse=not ascending)
        assert prices == expected, f"Name sorting failed. Expected: {expected}, Got: {prices}"
        return self

    def goto_product_detail_page(self, i):
        self.item_label_name.nth(i).click()
        expect(self.back_button).to_be_visible()
        return self

    def verify_product_detail_page(self, product_name, price, desc):
        expect(self.item_label_name).to_have_text(product_name)
        expect(self.item_price).to_have_text(price)
        expect(self.desc_pdp).to_have_text(desc)
        expect(self.add_button_pdp).to_be_visible()
        return self

    def add_product_pdp_click(self):
        self.add_button_pdp.click()
        expect(self.add_button_pdp).not_to_be_visible()
        expect(self.remove_button_pdp).to_be_visible()
        expect(self.cart_badge).to_be_visible()
        expect(self.cart_badge).to_have_text("1")
        return self

    def remove_product_pdp_click(self):
        self.remove_button_pdp.click()
        expect(self.remove_button_pdp).not_to_be_visible()
        expect(self.add_button_pdp).to_be_visible()
        expect(self.cart_badge).not_to_be_visible()
        return self

    def back_to_products_page(self):
        self.back_button.click()
        expect(self.back_button).not_to_be_visible()
        expect(self.add_button_pdp).not_to_be_visible()
        expect(self.remove_button_pdp).not_to_be_visible()
        expect(self.sort_container).to_be_visible()
        return self


