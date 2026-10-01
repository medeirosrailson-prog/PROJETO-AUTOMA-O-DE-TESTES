from guara.transaction import AbstractTransaction

from tests.pages.inventory_page import InventoryPage


class AddToCartTransaction(AbstractTransaction):
    def do(self) -> str:
        return InventoryPage(self._driver).add_backpack()
