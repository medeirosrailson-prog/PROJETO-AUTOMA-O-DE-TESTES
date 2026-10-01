from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage


class RemoveFromCartTransaction(AbstractTransaction):
    def do(self) -> int:
        return CartPage(self._driver).remove_backpack()
