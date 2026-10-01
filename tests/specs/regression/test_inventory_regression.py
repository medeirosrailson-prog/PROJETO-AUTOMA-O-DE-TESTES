import pytest
from guara import it

from tests.transactions.sort_products_transaction import SortProductsTransaction


@pytest.mark.regression
@pytest.mark.products
def test_ordenar_produtos_por_preco_crescente(logged_in_app):
    result = logged_in_app.at(SortProductsTransaction, option="lohi")
    expected_order = (
        "Sauce Labs Onesie, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt, "
        "Test.allTheThings() T-Shirt (Red), Sauce Labs Backpack, "
        "Sauce Labs Fleece Jacket"
    )
    result.asserts(it.IsEqualTo, expected_order)


@pytest.mark.regression
@pytest.mark.products
def test_ordenar_produtos_por_nome(logged_in_app):
    result = logged_in_app.at(SortProductsTransaction, option="az")
    expected_order = (
        "Sauce Labs Backpack, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt, "
        "Sauce Labs Fleece Jacket, Sauce Labs Onesie, "
        "Test.allTheThings() T-Shirt (Red)"
    )
    result.asserts(it.IsEqualTo, expected_order)
