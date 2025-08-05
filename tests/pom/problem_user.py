from playwright.sync_api import Page,expect

class KnownBug:
    def __init__(self, page: Page):
        self.page = page

######Locator
        self.products_title = page.locator("[data-test='title']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.inventory_item = page.locator("[data-test='inventory-item']")
        self.item_label_name = page.locator("[data-test='inventory-item-name']")
        self.item_price = page.locator("[data-test='inventory-item-price']")
        self.add_button_pdp = page.locator("[data-test='add-to-cart']")
        self.remove_button_pdp = page.locator("[data-test='remove']")
        self.desc_pdp = page.locator("[data-test='inventory-item-desc']")
        self.add_button_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_button_bike = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.add_button_bolt_tshirt = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.add_button_jacket = page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']")
        self.add_button_onsie = page.locator("[data-test='add-to-cart-sauce-labs-onesie']")
        self.add_button_red_tshirt = page.locator("[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
        self.remove_button_backpack = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.remove_button_bike = page.locator("[data-test='remove-sauce-labs-bike-light']")
        self.remove_button_bolt_tshirt = page.locator("[data-test='remove-sauce-labs-bolt-t-shirt']")
        self.remove_button_jacket = page.locator("[data-test='remove-sauce-labs-fleece-jacket']")
        self.remove_button_onsie = page.locator("[data-test='remove-sauce-labs-onesie']")
        self.remove_button_red_tshirt = page.locator("[data-test='remove-test.allthethings()-t-shirt-(red)']")
        self.sidebar_menu = page.get_by_role("button", name="Open Menu")
        self.sidebar_close = page.get_by_role("button", name="Close Menu")
        self.sort_container = page.locator("[data-test='product-sort-container']")
        self.dropdown = page.locator("select.product_sort_container")
        self.back_button = page.locator("[data-test='back-to-products']")
        self.cart_page_title = page.locator("[data-test='title']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.item_label_name = page.locator("[data-test='inventory-item-name']")
        self.item_price = page.locator("[data-test='inventory-item-price']")
        self.add_button_pdp = page.locator("[data-test='add-to-cart']")
        self.remove_button_pdp = page.locator("[data-test='remove']")
        self.desc_pdp = page.locator("[data-test='inventory-item-desc']")
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

    def verify_bug_cant_remove_product(self, product_name):
        """
        Known bug: When the user clicks the 'Add' button on the specific item,
        the item cannot be removed by clicking the 'Remove' button (nothing happens)
        """

        add_button = getattr(self, f"add_button_{product_name}")
        remove_button = getattr(self, f"remove_button_{product_name}")

        #initial state, add button visible
        expect(add_button).to_be_visible()

        # clicks add backpack
        add_button.click()

        # remove button visible, add button not visible
        expect(remove_button).to_be_visible()
        expect(add_button).not_to_be_visible()

        # clicks remove backpack
        remove_button.click()

        # Known bug: remove button still visible, add button not visible
        expect(remove_button).to_be_visible()
        expect(add_button).not_to_be_visible()
        return self

    def verify_bug_cant_add_product(self, product_name):
        """
        Known bug: When the user clicks the 'Add' button on specific item, nothing happens
        the cart number is not updated, the 'Add' button remains visible, and the 'Remove' button is not displayed.
        """
        add_button = getattr(self, f"add_button_{product_name}")
        remove_button = getattr(self, f"remove_button_{product_name}")
        cart_number = self.cart_page_title.inner_text().strip()

        #initial state, add button visible
        expect(add_button).to_be_visible()

        # clicks add backpack
        add_button.click()
        after_click_number = self.cart_page_title.inner_text().strip()

        # Known bug: add button still visible, remove button not visible
        expect(add_button).to_be_visible()
        expect(remove_button).not_to_be_visible()
        assert after_click_number == cart_number, f"Cart count changed from {cart_number} to {after_click_number}"
        return self

    def verify_bug_cant_remove_backpack(self):
        """
        Known bug: When the user clicks the 'Add' button on the Backpack item,
        the item cannot be removed by clicking the 'Remove' button (nothing happens)
        """
        return self.verify_bug_cant_remove_product("backpack")

    def verify_bug_cant_remove_bike(self):
        """
        Known bug: When the user clicks the 'Add' button on the Bike item,
        the item cannot be removed by clicking the 'Remove' button (nothing happens)
        """
        return self.verify_bug_cant_remove_product("bike")

    def verify_bug_cant_remove_onsie(self):
        """
        Known bug: When the user clicks the 'Add' button on the Onsie item,
        the item cannot be removed by clicking the 'Remove' button (nothing happens)
        """
        return self.verify_bug_cant_remove_product("onsie")

    def verify_bug_cant_add_bolt_tshirt(self):
        """
        Known bug: When the user clicks the 'Add' button on the Bolt T-shirt item, nothing happens
        the cart number is not updated, the 'Add' button remains visible, and the 'Remove' button is not displayed.
        """
        return self.verify_bug_cant_add_product("bolt_tshirt")

    def verify_bug_cant_add_jacket(self):
        """
        Known bug: When the user clicks the 'Add' button on the Jacket item, nothing happens
        the cart number is not updated, the 'Add' button remains visible, and the 'Remove' button is not displayed.
        """
        return self.verify_bug_cant_add_product("jacket")

    def verify_bug_cant_add_red_tshirt(self):
        """
        Known bug: When the user clicks the 'Add' button on the Red T-shirt item, nothing happens
        the cart number is not updated, the 'Add' button remains visible, and the 'Remove' button is not displayed.
        """
        return self.verify_bug_cant_add_product("red_tshirt")

###Sorting
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

    def verify_bug_sorting(self):
        #verify sort dropdown options
        self.verify_sort_dropdown_options()
        #verify sort name a-z
        self.select_option_az()
        self.verify_name_sorting(ascending=True)
        """
        Known bug: when user selects option sort "Name (Z to A) nothing happens
        """
        self.select_option_za()
        self.verify_name_sorting(ascending=True)
        """
        Known bug: when user selects option sort "Price (Low to High) nothing happens
        """
        self.select_option_lohi()
        self.verify_name_sorting(ascending=True)
        """
        Known bug: when user selects option sort "Price (High to Low) nothing happens
        """
        self.select_option_hilo()
        self.verify_name_sorting(ascending=True)
        return self

###Product Detail Page
    def goto_product_detail_page(self, i):
        self.item_label_name.nth(i).click()
        expect(self.back_button).to_be_visible()
        return self

    def verify_bug_product_detail_page_problem_user(self, expected_name, unexpected_name):
        """
        Known bug: When the user tries to access a specific product detail,
        the wrong product detail is displayed.
        """
        expect(self.item_label_name).not_to_have_text(expected_name)
        expect(self.item_label_name).to_have_text(unexpected_name)
        expect(self.add_button_pdp).to_be_visible()
        return self

    def bug_add_product_pdp_click(self):
        """
        Known bug: user can't add products to cart on product detail page
        """
        self.add_button_pdp.click()
        expect(self.add_button_pdp).to_be_visible()
        expect(self.remove_button_pdp).not_to_be_visible()
        expect(self.cart_badge).not_to_be_visible()
        return self

    def bug_remove_product_pdp_click(self):
        """
        Known bug: user can't add products to cart on product detail page
        """
        #init clicks add button
        self.add_button_pdp.click()
        expect(self.add_button_pdp).not_to_be_visible()
        #product added
        expect(self.cart_badge).to_be_visible()
        expect(self.cart_badge).to_have_text("1")

        #clicks remove button
        self.remove_button_pdp.click()

        #known bug nothing removed
        expect(self.remove_button_pdp).to_be_visible()
        expect(self.add_button_pdp).not_to_be_visible()
        expect(self.cart_badge).to_be_visible()
        expect(self.cart_badge).to_have_text("1")
        return self

    def bug_button(self, button_type):
        if button_type== "bug add":
            return self.bug_add_product_pdp_click()
        elif button_type== "bug remove":
            return self.bug_remove_product_pdp_click()
        else:
            raise ValueError(f"Invalid button_type:{button_type}")

###Checkout
    def verify_element_visibility_and_text(self, locator, text):
        expect(locator).to_be_visible()
        expect(locator).to_have_text(text)
        return self

    def add_product(self, product_name):
        add_button = getattr(self, f"add_button_{product_name}")
        add_button.click()
        return self

    def goto_cart_page(self):
        self.cart_icon.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
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

    def verify_bug_cant_fill_lastname_problem_user(self, firstname, lastname, postalcode):
        #Fill First Name field
        self.firstname_field.fill(firstname)
        assert self.firstname_field.input_value() == firstname

        #Fill Last Name field
        self.lastname_field.fill(lastname)
        assert self.lastname_field.input_value() == ""
        #Fill Postal code field
        self.postalcode_field.fill(postalcode)
        assert self.postalcode_field.input_value() == postalcode
        #Click button continue
        self.continue_button.click()
        return self

    def verify_lastname_error_message(self):
        return self.verify_element_visibility_and_text(self.error_msg,self.error_lastname_text)

###Error User
    def verify_bug_product_detail_page_error_user(self, expected_name):
        """
        Known bug: When the user tries to access a specific product detail,
        the wrong product detail is displayed.
        """
        expect(self.item_label_name).to_have_text(expected_name)
        expect(self.add_button_pdp).to_be_visible()
        return self

    def verify_bug_cant_fill_lastname_error_user(self, firstname, lastname, postalcode):
        """
        Known bug: When login using error user, the last name text replaces the first name field,
        and the user can access the checkout overview page even if the last name field is empty
        """
        #Fill First Name field
        self.firstname_field.fill(firstname)
        assert self.firstname_field.input_value() == firstname

        #Fill Last Name field
        self.lastname_field.fill(lastname)
        assert self.lastname_field.input_value() == ""

        #Fill Postal code field
        self.postalcode_field.fill(postalcode)
        assert self.postalcode_field.input_value() == postalcode
        #Click button continue
        self.continue_button.click()
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

    def bug_finish_checkout(self):
        """
        Known bug: When login using error user, user can't complete checkout
        after click finish button, nothing happens and the user remains on the checkout overview page
        """
        self.finish_button.click()
        expect(self.page.locator("text=Checkout: Complete!")).not_to_be_visible()
        expect(self.page.locator("text=Checkout: Overview")).to_be_visible()
        return self