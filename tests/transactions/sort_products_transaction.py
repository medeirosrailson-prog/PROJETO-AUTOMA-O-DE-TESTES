from guara.transaction import AbstractTransaction

from tests.pages.inventory_page import InventoryPage


class SortProductsTransaction(AbstractTransaction):
    def do(self, option: str) -> str:
        return InventoryPage(self._driver).sort_products(option)
