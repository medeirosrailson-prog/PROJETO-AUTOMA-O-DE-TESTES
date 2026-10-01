from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


class CheckoutValidationTransaction(AbstractTransaction):
    def do(self, first_name: str, last_name: str, postal_code: str) -> str:
        CartPage(self._driver).start_checkout()
        checkout_page = CheckoutPage(self._driver)
        checkout_page.enter_customer_details(first_name, last_name, postal_code)
        checkout_page.continue_checkout()
        return checkout_page.error_message()
