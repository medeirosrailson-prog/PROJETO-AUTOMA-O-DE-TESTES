from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage


class ContinueShoppingTransaction(AbstractTransaction):
    def do(self) -> str:
        return CartPage(self._driver).continue_shopping()
