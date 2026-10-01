from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage


class ViewCartTransaction(AbstractTransaction):
    def do(self) -> int:
        InventoryPage(self._driver).open_cart()
        return CartPage(self._driver).product_count()
