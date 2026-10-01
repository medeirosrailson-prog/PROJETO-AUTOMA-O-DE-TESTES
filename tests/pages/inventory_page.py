from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_CONTROL = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_backpack(self) -> str:
        self.click(self.ADD_BACKPACK)
        return self.cart_badge_count()

    def cart_badge_count(self) -> str:
        badges = self.driver.find_elements(*self.CART_BADGE)
        return badges[0].text if badges else "0"

    def open_cart(self) -> None:
        self.click(self.CART_LINK)

    def product_names(self) -> str:
        names = self.elements(self.PRODUCT_NAMES)
        return ", ".join(element.text for element in names)

    def product_prices(self) -> list[float]:
        prices = self.elements(self.PRODUCT_PRICES)
        return [float(element.text.removeprefix("$")) for element in prices]

    def sort_products(self, option: str) -> str:
        control = self.wait.until(EC.visibility_of_element_located(self.SORT_CONTROL))
        Select(control).select_by_value(option)

        def selected_option_matches(browser):
            return (
                browser.find_element(*self.SORT_CONTROL).get_attribute("value")
                == option
            )

        self.wait.until(selected_option_matches)
        return self.product_names()

    def logout(self) -> str:
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
        return self.driver.current_url

    def reset_cart(self) -> str:
        self.click(self.MENU_BUTTON)
        self.click(self.RESET_LINK)
        return self.cart_badge_count()
