from guara.transaction import AbstractTransaction

from tests.pages.inventory_page import InventoryPage


class LogoutTransaction(AbstractTransaction):
    def do(self) -> str:
        return InventoryPage(self._driver).logout()
