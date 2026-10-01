import pytest
from guara import it

from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction
from tests.transactions.open_cart_transaction import OpenCartTransaction


@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.regression
def test_compra_de_produto_com_sucesso(logged_in_app, checkout_data):
    customer = checkout_data["valid_customer"]
    logged_in_app.when(AddToCartTransaction).asserts(it.IsEqualTo, "1")
    logged_in_app.when(OpenCartTransaction).asserts(it.Contains, "Sauce Labs Backpack")
    logged_in_app.when(CheckoutTransaction, **customer).asserts(
        it.Contains, "checkout-step-two.html"
    )
    logged_in_app.when(FinishOrderTransaction).asserts(
        it.Contains, "Thank you for your order"
    )
