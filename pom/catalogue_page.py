from playwright.sync_api import Page,expect

class CataloguePage:
    def __init__(self, page: Page):
        self.page = page

        #Locator
        self.products_title = page.locator("[data-test='title']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.sort_container = page.locator("[data-test='product-sort-container']")
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


    def verify_catalogue_page_design(self):
        expect(self.products_title).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.cart_badge).not_to_be_visible()
        expect(self.sort_container).to_be_visible()
        return self

    def verify_element(self, locator, expected_value, element_type):
        actual_count = locator.count()
        expected_count = len(expected_value)
        assert actual_count == expected_count, f"Expected {expected_count} {element_type} items, but found {actual_count}"

        for i, expected_value in enumerate(expected_value):
            actual_value = locator.nth(i).inner_text()
            expect(locator.nth(i)).to_have_text(expected_value), f"Item {i + 1}: Expected '{expected_value}', got '{actual_value}'"
        return self

    def verify_item_name(self, expected_name: list):
        #verify all item name
        return self.verify_element(self.item_label_name, expected_name, "name")

    def verify_item_price(self, expected_price:list ):
        #verify all item price
        return self.verify_element(self.item_price, expected_price, "price")

    def verify_item_visible(self, products:list, locator_map, element_type):
        for product in products:
            assert product in locator_map, f"{element_type} not found for product: '{product}'"
            product_locator = locator_map[product]
            expect(product_locator).to_be_visible()
        return self

    def button_clicks(self, products:list, locator_map, element_type):
        for product in products:
            assert product in locator_map, f"Cannot click {element_type} for product: '{product}'"
            locator_map[product].click()
        return self

    def verify_item_image(self, products:list):
        return self.verify_item_visible(products, self.image_products,"Image products")

    def verify_add_button_visible(self, products: list):
        return self.verify_item_visible(products, self.add_buttons, "Add button")

    def verify_remove_button_visible(self, products: list):
        return self.verify_item_visible(products, self.remove_buttons, "Remove button")

    def add_button_clicks(self, products: list):
        return self.button_clicks(products, self.add_buttons, "Add button")

    def remove_button_clicks(self, products: list):
        return self.button_clicks(products, self.remove_buttons, "Remove button")

    def verify_add_remove_product(self, products: list):
        self.verify_add_button_visible(products)
        self.add_button_clicks(products)
        self.verify_remove_button_visible(products)
        self.remove_button_clicks(products)
        self.verify_add_button_visible(products)
        return self
