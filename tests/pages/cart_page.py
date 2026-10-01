from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def product_names(self) -> str:
        products = self.driver.find_elements(*self.PRODUCT_NAMES)
        return ", ".join(product.text for product in products)

    def product_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_NAMES))

    def remove_backpack(self) -> int:
        self.click(self.REMOVE_BACKPACK)
        return self.product_count()

    def start_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self) -> str:
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        return self.driver.current_url
