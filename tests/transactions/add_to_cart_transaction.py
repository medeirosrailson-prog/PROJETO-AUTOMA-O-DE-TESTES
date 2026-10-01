from guara.transaction import AbstractTransaction

from tests.pages.inventory_page import InventoryPage


class AddToCartTransaction(AbstractTransaction):
    def do(self, product_id: str = "sauce-labs-backpack") -> str:
        return InventoryPage(self._driver).add_product(product_id)
