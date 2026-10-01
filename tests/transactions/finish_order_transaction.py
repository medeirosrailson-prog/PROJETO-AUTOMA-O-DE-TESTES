from guara.transaction import AbstractTransaction

from tests.pages.checkout_page import CheckoutPage


class FinishOrderTransaction(AbstractTransaction):
    def do(self) -> str:
        return CheckoutPage(self._driver).finish_order()
