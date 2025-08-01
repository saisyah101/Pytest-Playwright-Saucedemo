import random
from itertools import combinations

class LoginTestData:

    # Valid credentials
    VALID_USERNAMES = ["standard_user", "visual_user"]
    VALID_PASSWORD = "secret_sauce"

    # Invalid usernames
    INVALID_USERNAMES = ["standarduser", "invalid_username"]

    # Invalid passwords
    INVALID_PASSWORDS = ["secretsauce", "secret_sauce1"]

    # Any passwords
    ANY_PASSWORDS = ["secret_sauce", "secret_tomato"]

    # Standard User
    STD_USERNAME = "standard_user"


class CatalogueData:
    #expected name
    expected_name_list = ["Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"]

    #expected prices
    expected_price_list = ["$29.99",
                           "$9.99",
                           "$15.99",
                           "$49.99",
                           "$7.99",
                           "$15.99"]

    #all products
    all_products = ["backpack","bike","bolt_tshirt","jacket","onsie","red_tshirt"]

    # selected products
    selected_products = ["backpack","bike","bolt_tshirt","onsie","red_tshirt"]

    #combine selected products
    @classmethod
    def generate_ordered_combinations(cls):
        result = []
        n = len(cls.selected_products)
        for i in range(n):
            for j in range(i + 1, n + 1):
                result.append(cls.selected_products[i:j])
        return result

    # get combination
    @classmethod
    def get_random_combination(cls):
        all_combos = cls.generate_ordered_combinations()
        return random.choice(all_combos)