from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage


class OpenCartTransaction(AbstractTransaction):
    def do(self) -> str:
        InventoryPage(self._driver).open_cart()
        return CartPage(self._driver).product_names()
