from guara.transaction import AbstractTransaction

from tests.pages.inventory_page import InventoryPage


class ResetCartTransaction(AbstractTransaction):
    def do(self) -> str:
        return InventoryPage(self._driver).reset_cart()
