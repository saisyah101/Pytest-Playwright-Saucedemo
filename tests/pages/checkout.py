from playwright.sync_api import Page,expect

from tests import test_data


class Checkout:
    def __init__(self, page: Page):
        self.page = page

        # Locator
        self.catalogue_title = page.locator("[data-test='title']")
        self.cart_page_title = page.locator("[data-test='title']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
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
        self.qty_label = page.locator("[data-test='cart-quantity-label']")
        self.description_label = page.locator("[data-test='cart-desc-label']")
        self.cart_qty = page.locator("[data-test='item-quantity']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.checkout_form_title = page.locator("[data-test='title']")
        self.firstname_field = page.locator("[data-test='firstName']")
        self.lastname_field = page.locator("[data-test='lastName']")
        self.postalcode_field = page.locator("[data-test='postalCode']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.continue_button = page.locator("[data-test='continue']")
        self.checkout_overview_title = page.locator("[data-test='title']")
        self.payment_info_label = page.locator("[data-test='payment-info-label']")
        self.payment_info_value = page.locator("[data-test='payment-info-value']")
        self.shipping_info_label = page.locator("[data-test='shipping-info-label']")
        self.shipping_info_value = page.locator("[data-test='shipping-info-value']")
        self.total_info_label = page.locator("[data-test='total-info-label']")
        self.subtotal_label = page.locator("[data-test='subtotal-label']")
        self.tax_label = page.locator("[data-test='tax-label']")
        self.total_label = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")
        self.checkout_complete_title = page.locator("[data-test='title']")
        self.ponyexpress_image = page.locator("[data-test='pony-express']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.complete_text = page.locator("[data-test='complete-text']")
        self.back_home_button = page.locator("[data-test='back-to-products']")
        self.error_msg = page.locator("[data-test='error']")
        self.close_error_button = page.locator("[data-test='error-button']")
        self.error_firstname_text = "Error: First Name is required"
        self.error_lastname_text = "Error: Last Name is required"
        self.error_postalcode_text = "Error: Postal Code is required"


    def goto_cart_page(self):
        self.cart_icon.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        return self

    def verify_item_visibility(self, locator, products: list, visible=True):
        actual_count = locator.count()
        expected_count = len(products)
        assert actual_count == expected_count, f"Expected {expected_count} items, but found {actual_count}"

        for i, expected_value in enumerate(products):
            if visible:
                expect(locator.nth(i)).to_be_visible()
            else:
                expect(locator.nth(i)).not_to_be_visible()
        return self

    def verify_item_text(self, locator, products: list, expected_text):
        actual_count = locator.count()
        expected_count = len(products)
        assert actual_count == expected_count, f"Expected {expected_count} items, but found {actual_count}"

        for i, expected_value in enumerate(products):
                expect(locator.nth(i)).to_have_text(expected_text)
        return self

    def verify_button_visibility(self, locator_map, products:list, visible=True):
        for product in products:
            assert product in locator_map, f"not found for product: '{product}'"
            product_locator = locator_map[product]
            if visible:
                expect(product_locator).to_be_visible()
            else:
                expect(product_locator).not_to_be_visible()
        return self

    def verify_cart_item_visible(self, products: list):
        return self.verify_item_visibility(self.item_label_name, products, visible=True)

    def verify_remove_button_visible(self, products: list):
        return self.verify_button_visibility(self.remove_buttons, products, visible=True)

    def verify_add_button_visible(self, products: list):
        return self.verify_button_visibility(self.add_buttons, products, visible=True)

    def verify_remove_button_not_visible(self, products: list):
        return self.verify_button_visibility(self.remove_buttons, products, visible=False)

    def verify_add_button_not_visible(self,products: list):
        return self.verify_button_visibility(self.add_buttons, products, visible=False)

    def verify_cart_qty(self, products: list):
        return self.verify_item_visibility(self.cart_qty, products, visible = True)

    def verify_qty_text(self, products: list):
        return self.verify_item_text(self.cart_qty, products, "1")

    def verify_element_visibility_and_text(self, locator, text):
        expect(locator).to_be_visible()
        expect(locator).to_have_text(text)
        return self

    def verify_subtotal_price(self):
        price_elements = self.item_price
        total_calculated = 0

        for i in range(price_elements.count()):
            price_element = price_elements.nth(i)
            price_text = price_element.inner_text().strip()
            if price_text.startswith('$'):
                price_value = float(price_text.replace('$',''))
                total_calculated += price_value
            else:
                print(f"Warning: Price format unexpected: '{price_text}'")

        self.calculated_subtotal = total_calculated
        expected_value = f"Item total: ${self.calculated_subtotal:.2f}"
        actual_value = self.subtotal_label.inner_text()
        assert actual_value == expected_value, f"Expected: '{expected_value}' but got Actual: '{actual_value}'"
        return self

    def verify_tax(self):
        tax_rate = 0.08
        expected_tax = round(tax_rate*self.calculated_subtotal,2)
        self.calculated_tax = expected_tax
        expected_value = f"Tax: ${self.calculated_tax:.2f}"
        actual_value = self.tax_label.inner_text()
        assert actual_value==expected_value, f"Expected: {expected_value} but got Actual:{actual_value}"
        return self

    def verify_total_price(self):
        expected_total_price = round(self.calculated_subtotal+self.calculated_tax,2)
        expected_value = f"Total: ${expected_total_price:.2f}"
        actual_value = self.total_label.inner_text()
        assert actual_value == expected_value, f"Expected: {expected_value} but got Actual:{actual_value}"
        return self

    def verify_cart_page(self):
        self.verify_element_visibility_and_text(self.cart_page_title, "Your Cart")
        expect(self.sidebar_menu).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.cart_badge).to_be_visible()
        expect(self.qty_label).to_be_visible()
        expect(self.description_label).to_be_visible()
        expect(self.continue_shopping_button).to_be_visible()
        expect(self.checkout_button).to_be_visible()
        return self

    def continue_shopping(self):
        self.continue_shopping_button.click()
        self.verify_element_visibility_and_text(self.catalogue_title, "Products")
        expect(self.page.locator("text=Your Cart")).not_to_be_visible()
        expect(self.qty_label).not_to_be_visible()
        return self

    def goto_checkout_form(self):
        self.checkout_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
        return self

    def verify_checkout_form(self):
        expect(self.checkout_form_title).to_be_visible()
        self.verify_element_visibility_and_text(self.checkout_form_title, "Checkout: Your Information")
        expect(self.firstname_field).to_be_visible()
        expect(self.lastname_field).to_be_visible()
        expect(self.postalcode_field).to_be_visible()
        expect(self.cancel_button).to_be_visible()
        expect(self.continue_button).to_be_visible()
        expect(self.page.locator("text=Your Cart")).not_to_be_visible()
        expect(self.qty_label).not_to_be_visible()
        return self

    def fill_checkout_form(self, first_name, last_name, postal_code):
        #Fill First Name field
        self.firstname_field.fill(first_name)
        #Fill Last Name field
        self.lastname_field.fill(last_name)
        #Fill Postal code field
        self.postalcode_field.fill(postal_code)
        #Click button continue
        self.continue_button.click()
        return self

    def verify_firstname_error_message(self):
        return self.verify_element_visibility_and_text(self.error_msg,self.error_firstname_text)

    def verify_lastname_error_message(self):
        return self.verify_element_visibility_and_text(self.error_msg,self.error_lastname_text)

    def verify_postalcode_error_message(self):
        return self.verify_element_visibility_and_text(self.error_msg,self.error_postalcode_text)

    def close_error_message(self):
        self.close_error_button.click()
        expect(self.error_msg).not_to_be_visible()
        return self

    def verify_checkout_overview_page(self):
        self.verify_element_visibility_and_text(self.checkout_overview_title, "Checkout: Overview")
        expect(self.sidebar_menu).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.cart_badge).to_be_visible()
        expect(self.qty_label).to_be_visible()
        expect(self.description_label).to_be_visible()
        self.verify_element_visibility_and_text(self.payment_info_label,"Payment Information:")
        self.verify_element_visibility_and_text(self.payment_info_value,"SauceCard #31337")
        self.verify_element_visibility_and_text(self.shipping_info_label,"Shipping Information:")
        self.verify_element_visibility_and_text(self.shipping_info_value,"Free Pony Express Delivery!")
        self.verify_element_visibility_and_text(self.total_info_label, "Price Total")
        expect(self.cancel_button).to_be_visible()
        expect(self.finish_button).to_be_visible()
        return self

    def finish_checkout(self):
        self.finish_button.click()
        self.verify_element_visibility_and_text(self.checkout_complete_title, "Checkout: Complete!")
        return self

    def verify_complete_page(self):
        expect(self.ponyexpress_image).to_be_visible()
        self.verify_element_visibility_and_text(self.complete_header,"Thank you for your order!")
        self.verify_element_visibility_and_text(self.complete_text,"Your order has been dispatched, and will arrive just as fast as the pony can get there!")
        expect(self.back_home_button).to_be_visible()
        return self

    def back_to_home(self):
        self.back_home_button.click()
        self.verify_element_visibility_and_text(self.catalogue_title,"Products")
        expect(self.cart_badge).not_to_be_visible()
        self.verify_remove_button_not_visible(test_data.CatalogueData.all_products)
        return self

    def cancel_checkout(self):
        self.cancel_button.click()
        expect()




















